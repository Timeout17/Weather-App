from project.logic.services.daily_weather import DailyWeatherClass


def test_create_weather_data():

    data = {
        "city": {
            "name": "Szeged",
            "country": "HU",
            "sunrise": 1000,
            "sunset": 2000
        },
        "list": [
            {
                "main": {
                    "temp": 30.5,
                    "feels_like": 31.2,
                    "temp_min": 29.0,
                    "temp_max": 32.0,
                    "humidity": 45,
                    "pressure": 1015
                },
                "weather": [
                    {
                        "description": "clear sky"
                    }
                ],
                "wind": {
                    "speed": 3.5,
                    "deg": 180
                },
                "clouds": {
                    "all": 20
                },
                "visibility": 10000
            }
        ]
    }

    daily_weather = DailyWeatherClass()

    result = daily_weather.create_weather_data(data)

    assert len(result) == 1

    weather = result[0]

    assert weather.city == "Szeged"
    assert weather.country == "HU"

    assert weather.temperature == 30.5
    assert weather.feels_like == 31.2
    assert weather.temp_min == 29.0
    assert weather.temp_max == 32.0

    assert weather.humidity == 45
    assert weather.pressure == 1015

    assert weather.description == "clear sky"

    assert weather.wind_speed == 3.5
    assert weather.wind_direction == 180

    assert weather.cloudiness == 20
    assert weather.visibility == 10000

    assert weather.sunrise == 1000
    assert weather.sunset == 2000

def test_create_weather_data_only_uses_first_five():

    weather_entries = []

    for i in range(7):
        weather_entries.append({
            "main": {
                "temp": i,
                "feels_like": i,
                "temp_min": i,
                "temp_max": i,
                "humidity": i,
                "pressure": i
            },
            "weather": [
                {
                    "description": "clear sky"
                }
            ],
            "wind": {
                "speed": i,
                "deg": i
            },
            "clouds": {
                "all": i
            },
            "visibility": i
        })

    data = {
        "city": {
            "name": "Szeged",
            "country": "HU",
            "sunrise": 1000,
            "sunset": 2000
        },
        "list": weather_entries
    }

    daily_weather = DailyWeatherClass()

    result = daily_weather.create_weather_data(data)

    assert len(result) == 5