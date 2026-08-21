from project.backend.utils.city_loader import CityLoaderClass
from project.logic.services.localizaton import LoocalizationClass
from project.logic.services.Weatherdata import WeatherdataClass
from project.models.WeatherdataModel import WeatherdataModellClass


loocalization: LoocalizationClass = LoocalizationClass()
weather: WeatherdataClass = WeatherdataClass()


class DailyWeatherClass:

    async def getWeather(self):

        all_weather = []

        city_loader = CityLoaderClass()
        cities = city_loader.loadfile("citynames.txt")

        for city in cities:

            adatok = await loocalization.getCoordinates(city)

            weather_data = await weather.getWeatherdataforecast(adatok)

            city_weather = self.create_weather_data(weather_data)

            all_weather.append(city_weather)

        return all_weather

    def create_weather_data(self, data):

        weather_data_list = []

        for actual_data in data["list"][:5]:

            weather_data = WeatherdataModellClass(
                city=data["city"]["name"],
                country=data["city"]["country"],

                temperature=actual_data["main"]["temp"],
                feels_like=actual_data["main"]["feels_like"],
                temp_min=actual_data["main"]["temp_min"],
                temp_max=actual_data["main"]["temp_max"],

                humidity=actual_data["main"]["humidity"],
                pressure=actual_data["main"]["pressure"],

                description=actual_data["weather"][0]["description"],

                wind_speed=actual_data["wind"]["speed"],
                wind_direction=actual_data["wind"]["deg"],

                cloudiness=actual_data["clouds"]["all"],
                visibility=actual_data["visibility"],

                sunrise=data["city"]["sunrise"],
                sunset=data["city"]["sunset"]
            )

            weather_data_list.append(weather_data)

        return weather_data_list


if __name__ == "__main__":

    import asyncio

    async def main():

        daily_weather = DailyWeatherClass()

        result = await daily_weather.getWeather()

        print(result)

    asyncio.run(main())