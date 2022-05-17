# Panduza Python Platform

Panduza platform provides a simple way to create mqtt clients that match panduza specifications.

## Dependencies

```bash
pip install paho-mqtt loguru
```

## Install

Create the tree.json in /etc/panduza/

```bash
./package-build.sh
./package-monitor.sh

sudo ./service-deploy.sh

# To restart the service
sudo systemctl restart panduza-py-platform.service

# To monitor the platform run monitor in a separate terminal
service-monitor.sh
```

