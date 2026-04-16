import requests

def get_weather(lat: float, lon: float) -> dict:
    """
    Fetches current weather data from the Open-Meteo API.

    :param float lat: Latitude of the location 
    :param float lon: Longitude of the location
    
    :return: Dictionary with current weather data, or error details if the request fails.
    """

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude":lat,
        "longitude":lon,
        "current":"temperature_2m,wind_speed_10m,weather_code"
    }

    response = requests.get(url, params=params)
    return response.json()
