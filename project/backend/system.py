import os

from fastapi import FastAPI
from pydantic import BaseModel
from project.logic.services.localizaton import LoocalizationClass
from project.logic.services.Weatherdata import  WeatherdataClass


app = FastAPI()



class DataResponse(BaseModel):
    city: str

loocalization: LoocalizationClass = LoocalizationClass()    
weather: WeatherdataClass = WeatherdataClass()


@app.post("/weather")
async def Getdata(city: str):
    adatok: tuple[int, int] =  await loocalization.getCoordinates(city)
    return await weather.getWeatherdata(adatok)


