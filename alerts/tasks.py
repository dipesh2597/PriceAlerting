import threading
import websocket
import json
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

lock = threading.Lock()


@shared_task()
def send_alert_mail(price, emails):
	send_mail(
		'Bitcoin Alert',
		f'Bitcoin price has reached the alert price {price}!',
		'alerts@tanX.fi',
		emails,
		fail_silently=False,
	)


def check_alert_price():
	ws_endpoint = "wss://stream.binance.com:9443/ws/btcusdt@aggTrade"

	def on_message(ws, message):
		data = json.loads(message)
		alerts = None
		if data['s'] == 'BTCUSDT':
			price = float(data['p'])
			if settings.LOG_PRICES:
				print(price)
			try:
				from alerts.models import Alert
				alerts = Alert.objects.select_for_update(nowait=True).filter(price=price, status='CREATED')
				if alerts:
					send_alert_mail.delay(price, list(alerts.values_list('user__email', flat=True).distinct()))
					alerts.update(status='TRIGGERED')
					print(f"Bitcoin price has reached the alert price {price}! has been sent to: { list(alerts.values_list('user__email', flat=True).distinct())}")
			except Exception as err:
				if alerts:
					alerts.update(trigger_in_progress=False)
				print("Encountered error in alert checking: ", err)

	ws = websocket.WebSocketApp(ws_endpoint, on_message=on_message)
	ws.run_forever()


@shared_task
def start_websocket():
	check_alert_price()
