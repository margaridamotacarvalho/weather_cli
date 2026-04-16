import argparse
from weather_cli.api import get_weather
from weather_cli.output import output_display

def main():
    parser = argparse.ArgumentParser(description="Weather CLI")
    parser.add_argument("--lat", type=float, required=True, help="Latitude")
    parser.add_argument("--lon", type=float, required=True, help="Longitude")
    args = parser.parse_args()

    try:
        data = get_weather(args.lat, args.lon)

        if data.get("error"):
            print(data["reason"])
        else:
            output_display(data)

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
