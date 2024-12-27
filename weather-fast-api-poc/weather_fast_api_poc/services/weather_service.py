import httpx
from ..settings import get_settings

BASE_GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"
BASE_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"

async def get_lat_long(city: str, state: str = None, country: str = None):
    settings = get_settings()
    params = {
        "q": f"{city},{state},{country}".strip(","),
        "limit": 1,
        "appid": settings.openweather_api_key,
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_GEOCODING_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if not data:
            raise ValueError("Location not found")
        return data[0]["lat"], data[0]["lon"]

async def get_current_weather(lat: float, lon: float):
    settings = get_settings()
    params = {"lat": lat, "lon": lon, "appid": settings.openweather_api_key, "units": "metric"}
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_WEATHER_URL, params=params)
        response.raise_for_status()
        return response.json()

