from fastapi import APIRouter, Query
from datetime import datetime
from ..models import WeatherApiResponse

router = APIRouter()

@router.get("/api/weather", response_model=WeatherApiResponse)
async def get_weather(
    q: str = Query(..., description="City name, state code, and country code in the format: city,state,country")
):
    # Parse the input (basic example, improve as needed)
    parts = q.split(",")
    city = parts[0].strip()
    state = parts[1].strip() if len(parts) > 1 else None
    country = parts[2].strip() if len(parts) > 2 else None

    # Hardcoded response for demonstration
    return {
        "coord": {
            "lon": -122.3337,
            "lat": 47.606
        },
        "weather": {
            "main": "Clear",
            "description": "clear sky"
        },
        "temperature": {
            "measurements": 15.17,
            "description": "Mild",
            "currentDateTime": datetime.utcnow().isoformat()
        },
        "city": city,
        "state": state,
        "country": country
    }
