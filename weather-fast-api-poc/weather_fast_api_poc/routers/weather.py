from fastapi import APIRouter, Query
from datetime import datetime
from ..models import WeatherApiResponse

router = APIRouter()

def get_temp_description(temp):
    if temp < 0.0:
        return "Freezing"
    elif temp >= 0.0 and temp < 15.0:
        return "Cold"
    elif temp  >= 15.0 and temp < 25.0:
        return "Mild"
    elif temp >= 30.0 and temp < 40.0:
        return "Warm"
    elif temp >= 40.0:
        return "Hot"
    else:
        return "Extreme Temperature"

@router.get("/api/weather", response_model=WeatherApiResponse)
async def get_weather(
    q: str = Query(..., description="City name, state code, and country code in the format: city,state,country")
):
    # Parse the input
    parts = q.split(",")
    city = parts[0].strip()
    state = parts[1].strip() if len(parts) > 1 else None
    country = parts[2].strip() if len(parts) > 2 else None

    try:
        # Get latitude and longitude from the geocoding API
        coord = await get_lat_long(city, state, country)

        # Get current weather data using latitude and longitude
        weather_data = await get_current_weather(coord["lat"], coord["lon"])

        # Build and return the response
        return WeatherApiResponse(
            coord={
                "lon": coord["lon"],
                "lat": coord["lat"]
            },
            weather={
                "main": weather_data["weather"][0]["main"],
                "description": weather_data["weather"][0]["description"]
            },
            temperature={
                "measurements": weather_data["main"]["temp"],
                "description": get_temp_description(weather_data["main"]["temp"]),
                "currentDateTime": datetime.utcnow()
            },
            city=city,
            state=state,
            country=country
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
