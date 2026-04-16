from rich import print
from rich.panel import Panel
from weather_cli.wmo_codes import WMO_CODES, WMO_EMOJIS

def output_display(data: dict) -> str:
    """
    Displays current weather data in a formatted CLI panel.

    :param dict data: Dictionary with current weather data from the Open-Meteo API. 
    
    :return: String with the final output.
    """
    
    current = data["current"]
    units = data["current_units"]
    
    temperature = current["temperature_2m"]
    wind_speed = current["wind_speed_10m"]
    weather_code = current["weather_code"]

    weather_desc = WMO_CODES.get(weather_code, "Unknown condition")
    weather_emoji = WMO_EMOJIS.get(weather_code, "☀️")

    output = f"{weather_emoji}  {weather_desc}\n🌡  Temperature: {temperature} {units['temperature_2m']}\n💨  Wind Speed: {wind_speed} {units['wind_speed_10m']}"
    print(Panel(output, title="Current Weather"))