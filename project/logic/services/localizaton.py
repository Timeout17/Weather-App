import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


class LoocalizationClass():

    async def getCoordinates(self, city_name: str) -> tuple[int, int]:

        async with httpx.AsyncClient() as client:

            response = await client.get(
                "http://api.openweathermap.org/geo/1.0/direct",
                params={
                        "q": city_name,
                        "appid": API_KEY
                        }
                    )
            response.raise_for_status()

            data = response.json()

            return (data[0]["lat"], data[0]["lon"])


if __name__ == "__main__":
    local = LoocalizationClass()
    print(local.getCoordinates("budapest"))