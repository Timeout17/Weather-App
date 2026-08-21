import pytest

from project.logic.orchestrator.make_answer import MakeAnswer


@pytest.mark.anyio
async def test_make_answers(monkeypatch):

    async def fake_get_weather(self):
        return ["fake weather data"]

    monkeypatch.setattr(
        "project.logic.orchestrator.make_answer.DailyWeatherClass.getWeather",
        fake_get_weather
    )


    def fake_create_messages_model(self, weather_data):

        assert weather_data == ["fake weather data"]

        return [
            "system message"
        ]

    monkeypatch.setattr(
        "project.logic.orchestrator.make_answer.MessageCreateClass.create_messages_model",
        fake_create_messages_model
    )


    class FakeClient:
        pass


    monkeypatch.setattr(
        "project.logic.orchestrator.make_answer.CreateClient.make_client",
        lambda self: FakeClient()
    )

    def fake_create_daily_weather_message(self, message):

        assert message == "system message"

        return [
            {
                "role": "system",
                "content": "daily weather message"
            }
        ]

    monkeypatch.setattr(
        "project.logic.orchestrator.make_answer.CreateMessageClass.create_daily_weather_message",
        fake_create_daily_weather_message
    )


    class FakeMessage:
        class Choice:
            class Message:
                content = "# 🌤️ Mai időjárás\n\n| Idő | Hőmérséklet |\n|---|---:|\n| 12:00 | 25 °C |"

            message = Message()

        choices = [Choice()]


    def fake_chatservice(self, client, content):

        assert isinstance(client, FakeClient)

        assert content == [
            {
                "role": "system",
                "content": "daily weather message"
            }
        ]

        return FakeMessage()


    monkeypatch.setattr(
        "project.logic.orchestrator.make_answer.LLMServiceClass.Chatservice",
        fake_chatservice
    )


    sent_email = {}

    def fake_send_email(subject, content):

        sent_email["subject"] = subject
        sent_email["content"] = content


    monkeypatch.setattr(
        "project.logic.orchestrator.make_answer.GmailService.send_email",
        fake_send_email
    )


    result = await MakeAnswer().make_answers()


    assert result.startswith("# 🌤️ Mai időjárás")

    assert sent_email["subject"] == "🌤️ Mai időjárás-jelentés"

    assert "<table>" in sent_email["content"]