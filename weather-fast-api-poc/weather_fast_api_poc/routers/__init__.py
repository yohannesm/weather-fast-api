"""
This module contains the routers for the application.
"""

from .healthcheck import router as healthcheck_router
from .weather import router as weather_router

routers = [
    healthcheck_router,
    weather_router,
]
