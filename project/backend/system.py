import os

from fastapi import FastAPI
from pydantic import BaseModel
from project.logic.services.localizaton import LoocalizationClass
from project.logic.services.Weatherdata import  WeatherdataClass
from project.logic.services.WeatherdataCompilation import WeatherdataCompilationClass
from project.agent.CreateAgent import CreateClient
from project.agent.Createmessage import CreateMessageClass
from project.agent.LLMService import LLMServiceClass
from project.models.Message import MessageClass

app = FastAPI()



class DataResponse(BaseModel):
    city: str

loocalization: LoocalizationClass = LoocalizationClass()    
weather: WeatherdataClass = WeatherdataClass()


@app.post("/weather")
async def Getdata(city: str):
    adatok: tuple[int, int] =  await loocalization.getCoordinates(city)
    weather_data = await weather.getWeatherdata(adatok)
    actual_data = WeatherdataCompilationClass().make_Weather_data(weather_data)

    client = CreateClient().make_client()

    user_message: str = MessageClass().make_message(actual_data)

    message = CreateMessageClass().create_message(user_message)

    ai_message = LLMServiceClass().Chatservice(client, message)

    return ai_message.choices[0].message.content 