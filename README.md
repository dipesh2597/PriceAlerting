# Pricing Trigger Alerting System

Welcome to the Pricing Trigger Alerting System! This system provides functionality to set alerts for specific price triggers in the cryptocurrency market and notifies users via email when these triggers are met.

## Installation

1. **Clone the repository:**
    ```bash
    git clone git@github.com:dipesh2597/Pricing-Trigger-Alerting-System.git
    ```

2. **Ensure Docker is installed on your system.** If not, you can follow the installation guide [here](https://docs.docker.com/desktop/install/mac-install/).

## Usage

### Running the Project

To start the project, run the following command:
```bash
docker-compose up -d --build
```

### Viewing Logs
To view logs from the running containers, use the following command:
```bash
docker-compose logs -f web
```

```bash
docker-compose logs -f celery
```

These commands display real-time logs from the application container.

### Testing Alerts
To test alerts immediately, follow these steps:

Inside settings.py, set `LOG_PRICES=True` to see live prices of BTCUSDT. This will enable logging of cryptocurrency prices to the console.
Create an alert for a specific price trigger.

OR use [TradingView Portal](https://in.tradingview.com/symbols/BTCUSDT/) to see live prices.

Once the alert price is reached, an email notification will be sent, and a confirmation message will be logged to the console, indicating the price at which the alert was triggered and the recipient's email address.

### API Documentation
For API usage and documentation, please refer to the [API Documentation](https://documenter.getpostman.com/view/32891689/2s9YyzdyFz#intro). This documentation provides detailed information on available endpoints and how to interact with them.