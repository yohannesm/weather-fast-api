"""
Models module. The models are meant to directly interact with
the database (that's where the actual SQL queries are). The
routers will only interact with the models.
"""

from .WeatherAPIResponse import Coord, Weather, Temperature, WeatherApiResponse

__all__ = ["Coord", "Weather", "Temperature", "WeatherApiResponse"]