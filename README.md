# Panduza Python Platform

Panduza platform provides a simple way to create mqtt clients that match panduza specifications.

## Dependencies

```bash
pip install paho-mqtt pyserial loguru
```

## Usage

The panduza platform instanciates interfaces described into the tree.json

```bash
# To run the platform
python3 src/pza_platform -l --tree /etc/panduza/tree.json
```

