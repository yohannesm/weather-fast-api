# weather-fast-api-poc

simple webserver to process openweather api response


if you need to source the pyenv manually do: `source ~/.pyenv/versions/fastapi-template-env/bin/activate`

To run the webserver: 
- activate the environment : `poetry shell`
- run the app `uvicorn weather_fast_api_poc.main:app --reload`

Run the VENV: Instructions here: https://fastapi.tiangolo.com/virtual-environments/#create-a-virtual-environment
`source .fastapi_weather_venv/bin/activate`

To run the server using uvicorn, runs
`uvicorn weather_fast_api_poc.main:app --reload`


To hit the services there are 2 active endpoints now. Health check and weather query using city,(opt state), (opt country code). 
Example: 
`curl -L -XGET http://localhost:8000/api/health_check`
`curl -L -XGET http://localhost:8000/api/weather/\?q=Seattle`

-L is needed because there's redirect happening with the FastAPI
