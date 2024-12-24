from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Coord(BaseModel):
    lon: float
    lat: float

class Weather(BaseModel):
    main: str
    description: str

class Temperature(BaseModel):
    measurements: float
    description: str
    currentDateTime: datetime

class WeatherApiResponse(BaseModel):
    coord: Coord
    weather: Weather
    temperature: Temperature
    city: str
    state: Optional[str] = None
    country: Optional[str] = None
