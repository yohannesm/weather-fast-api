from pydantic import BaseModel, Field

class LocationRequest(BaseModel):
    city: str
    state: str = Field(default=None)
    country: str = Field(default=None)

