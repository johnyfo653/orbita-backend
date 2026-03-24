from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# 🔥 CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "online"}

@app.get("/search")
def search(q: str):
    return {
        "results": [
            {"name": "Titanic", "lat": 41.7, "lon": -49.9},
            {"name": "MH370", "lat": -35, "lon": 92}
        ]
    }

@app.get("/scan")
def scan(lat: float, lon: float):
    return {
        "results": [
            {
                "lat": lat + random.uniform(-1, 1),
                "lon": lon + random.uniform(-1, 1)
            }
            for _ in range(10)
        ]
    } 
