from project.models.Message import MessageClass
from project.models.WeatherdataModel import WeatherdataModellClass


class MessageCreateClass:

    def create_messages_model(self, data: list[list[WeatherdataModellClass]]):

        all_messages = []

        for city in data:

            city_weather = []

            for weather in city:
                message = MessageClass.make_message(weather)
                city_weather.append(message)

            city_message = "\n".join(city_weather)
            all_messages.append(city_message)

        return all_messages