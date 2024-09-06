from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from mylib.logistics import (
    # distance_between_two_points,
    cities_list,
    # get_coordinates,
    # travel_time,
)


app = FastAPI()


class City(BaseModel):
    name: str


@app.get("/")
async def root():
    """Home page with GET HTTP METHOD"""
    return {"message": "Hello Logistics INC"}


@app.get("/cities")
async def cities():
    """
    List cities with GETP HTTP Method

    Returns a list of cities that are available to get further information about"""
    return {"cities": cities_list}


if __name__ == "__main___":
    uvicorn.run(app, port=8080, host="0.0.0.0")
