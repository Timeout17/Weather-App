from project.models.WeatherdataModel import WeatherdataModellClass
from datetime import datetime

class WeatherdataCompilationClass:

    @staticmethod
    def make_Weather_data(weather_data):

        data = WeatherdataModellClass(
            city=weather_data["name"],
            country=weather_data["sys"]["country"],

            temperature=weather_data["main"]["temp"],
            feels_like=weather_data["main"]["feels_like"],
            temp_min=weather_data["main"]["temp_min"],
            temp_max=weather_data["main"]["temp_max"],

            humidity=weather_data["main"]["humidity"],
            pressure=weather_data["main"]["pressure"],

            description=weather_data["weather"][0]["description"],

            wind_speed=weather_data["wind"]["speed"],
            wind_direction=weather_data["wind"]["deg"],

            cloudiness=weather_data["clouds"]["all"],
            visibility=weather_data["visibility"],

            sunrise = datetime.fromtimestamp(
                weather_data["sys"]["sunrise"]
            ).strftime("%H:%M"),

            sunset = datetime.fromtimestamp(
                weather_data["sys"]["sunset"]
            ).strftime("%H:%M")
        )

        return data