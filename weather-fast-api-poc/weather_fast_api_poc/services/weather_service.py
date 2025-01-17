import httpx
from weather_fast_api_poc.settings import get_settings
#from ..settings import get_settings

BASE_GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"
BASE_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
OPENWEATHER_API_KEY = "a37fd5f0fbfb4d081daec8f8b9eca030"


async def get_lat_long(city: str, state: str = None, country: str = None):
    settings = get_settings()

    location_parts = [city]
    if state:
        location_parts.append(state)
    if country:
        location_parts.append(country)

    query = ",".join(part for part in location_parts if part)

    params = {
        "q": query,
        "limit": 1,
        "appid": OPENWEATHER_API_KEY,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_GEOCODING_URL, params=params)
        response.raise_for_status()

        data = response.json()
        print(response.text)
        if not data:
            raise ValueError("Location not found")
        # Assuming the response is a list of locations, return the first one
        return data[0]["lat"], data[0]["lon"]


async def get_current_weather(lat: float, lon: float):
    settings = get_settings()
    params = {"lat": lat, "lon": lon, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_WEATHER_URL, params=params)
        response.raise_for_status()
        return response.json()

