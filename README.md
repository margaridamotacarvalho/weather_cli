# Weather CLI

## Description
A CLI program designed to accept latitude (--lat) and longitude (--lon) inputs, access the Open-Meteo API (https://open-meteo.com/), and return the temperature, wind speed, and weather conditions.
Written in Python using the requests library for API calls and the rich library for the CLI output.

## Requirements
- Python 3.12.3+

## Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python3 -m weather_cli.main --lat <latitude> --lon <longitude>
```

Example:
```bash
python3 -m weather_cli.main --lat 41.04 --lon -8.57
```

## Project Structure
```
weather_voltalia/
├── weather_cli/
│   ├── __init__.py
│   ├── main.py        # Entry point and argument parsing
│   ├── api.py         # Open-Meteo API client
│   ├── wmo_codes.py   # WMO weather code dictionary for descriptions
│   └── output.py      # CLI output formatting with rich help
├── requirements.txt
└── README.md
```