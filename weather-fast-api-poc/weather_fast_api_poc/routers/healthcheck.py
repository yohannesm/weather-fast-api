"""
Healthcheck router. Periodically checks if the application is healthy.
"""

from fastapi import APIRouter, status


router = APIRouter(
    prefix='/api/health_check',
    tags=['healthcheck']
)


@router.get('/', status_code=status.HTTP_200_OK)
async def health_check():
    """
    Healthcheck endpoint.
    @TODO: Implement healthcheck.
    """
    return "Server is healthy"
