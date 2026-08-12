from dataclasses import dataclass


@dataclass
class WeatherdataModellClass():
    city: str
    country: str

    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float

    humidity: int
    pressure: int

    description: str

    wind_speed: float
    wind_direction: int

    cloudiness: int
    visibility: int

    sunrise: int
    sunset: int