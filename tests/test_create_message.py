from project.agent.Createmessage import CreateMessageClass
from project.models.UserEnum import UserType


def test_create_message():

    result = CreateMessageClass.create_message(
        "Budapesten 25 °C van."
    )

    assert isinstance(result, list)
    assert len(result) == 2

    assert result[0]["role"] == UserType.SYSTEM.value
    assert result[1]["role"] == UserType.USER.value

    assert result[1]["content"] == "Budapesten 25 °C van."

def test_create_daily_weather_message():

    result = CreateMessageClass.create_daily_weather_message(
        "Budapest: 25 °C"
    )

    assert isinstance(result, list)
    assert len(result) == 2

    assert result[0]["role"] == UserType.SYSTEM.value
    assert result[1]["role"] == UserType.USER.value

    assert result[1]["content"] == "Budapest: 25 °C"