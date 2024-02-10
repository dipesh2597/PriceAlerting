import os
from celery import Celery
import redis

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pricingalert.settings')

app = Celery('pricingalert')


@app.on_after_configure.connect
def start_websocket(sender, **kwargs):
    # Execute start_websocket immediately after starting the worker
    sender.send_task('alerts.tasks.start_websocket')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
