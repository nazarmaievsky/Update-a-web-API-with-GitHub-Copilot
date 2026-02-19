from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/countries/{country_id}/cities")
async def get_cities(country_id: str):
    # Logic to fetch cities from database
    cities = db.query_cities_by_country(country_id)
    return {"country": country_id, "cities": cities}
    