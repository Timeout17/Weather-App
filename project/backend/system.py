from fastapi import FastAPI
from pydantic import BaseModel
from project.logic.services.localizaton import LoocalizationClass

app = FastAPI()


class DataResponse(BaseModel):
    city: str

loocalization: LoocalizationClass = LoocalizationClass()    

@app.post("/weather")
async def Getdata(city: str):
    return await loocalization.getCoordinates(city)


