from project.logic.services.daily_weather import DailyWeatherClass
from project.logic.services.Messagecreate import MessageCreateClass
from project.agent.CreateAgent import CreateClient
from project.agent.Createmessage import CreateMessageClass
from project.agent.LLMService import LLMServiceClass
from project.mail.GmailService import GmailService
import markdown


class MakeAnswer():

    async def make_answers(self):

        daily_weather = DailyWeatherClass()
        message_create = MessageCreateClass()

        weather_data = await daily_weather.getWeather()

        prompt = message_create.create_messages_model(weather_data)

        final_message = "\n\n\n".join(prompt)

        client = CreateClient().make_client()

        message = CreateMessageClass().create_daily_weather_message(final_message)

        ai_message = LLMServiceClass().Chatservice(client, message)

        html_message = markdown.markdown(
            ai_message.choices[0].message.content,
            extensions=["tables"]
        )

        GmailService.send_email(
            subject="🌤️ Mai időjárás-jelentés",
            content=html_message
        )

        return ai_message.choices[0].message.content
    