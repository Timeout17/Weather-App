import os
import httpx
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

class WeatherdataClass():

    async def getWeatherdata(self, coordinates: tuple[int, int]) -> json:


        async with httpx.AsyncClient() as client:

            response = await client.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={
                    "lat":coordinates[0],
                    "lon":coordinates[1],
                    "appid":API_KEY,
                    "units": "metric",
                    "lang": "hu"
                }
            )

            response.raise_for_status()

            data = response.json()

            return data

