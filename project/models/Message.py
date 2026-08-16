from project.models.WeatherdataModel import WeatherdataModellClass

class MessageClass():
    @staticmethod
    def make_message(weatherdata: WeatherdataModellClass) -> str:

        return f"""
            A város neve: {weatherdata.city} és az ország ahol vagyunk {weatherdata.country}.
            A az aktuális hőmérséklet: {weatherdata.temperature}°, és ennyinek érződik: {weatherdata.feels_like}°.
            A Minimális hőmérséklet: {weatherdata.temp_min}°, A maximális hőmérséklet: {weatherdata.temp_max}°.
            A pára tartalom: {weatherdata.humidity}, és a légnyomás: {weatherdata.pressure}.
            A szél sebesség: {weatherdata.wind_speed}, és az iránya: {weatherdata.wind_direction}.
            A felhősség: {weatherdata.cloudiness}, és a láthatóság: {weatherdata.visibility}.
            A nap felkelte: {weatherdata.sunrise}, és a naplemente: {weatherdata.sunset}

            Minimális leírás az időről: {weatherdata.description}.
            """
    
    