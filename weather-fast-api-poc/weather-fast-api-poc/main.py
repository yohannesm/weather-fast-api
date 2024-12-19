"""
Main file for weather-fast-api-poc.
This file is the entry point for the application.
"""

import logging
from typing import TYPE_CHECKING
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from .routers import routers
from .settings import get_settings, get_database
from .tools import migrate
from . import __version__


if TYPE_CHECKING:
    from databases import Database
    from .settings import Settings


settings: 'Settings' = get_settings()
app = FastAPI(
    debug=settings.debug,
    title='weather-fast-api-poc',
    description='simple webserver to process openweather api response',
    version=__version__,
    
    openapi_url='/openapi.json',
    
    
    docs_url='/docs',
    
    
    redoc_url='/redoc',
    
)

for router in routers:
    app.include_router(router)

app.add_middleware(GZipMiddleware, minimum_size=1000)

@app.on_event('startup')
async def startup():
    """
    Startup event.
    """
    logging.basicConfig(level=logging.DEBUG if settings.debug else logging.WARNING)
    logging.info('Starting up...')
    database: 'Database' = get_database()
    await database.connect()
    await migrate(database)

@app.on_event('shutdown')
async def shutdown():
    """
    Shutdown event.
    """
    logging.info('Shutting down...')
    database: 'Database' = get_database()
    await database.disconnect()