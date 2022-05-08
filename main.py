import uvicorn
import os
from fastapi import FastAPI
from wraps import get_wallpapers


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "hooman"}

@app.get("/wall")
def wall_paper(q: str):
    return get_wallpapers(q)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", default=5000)), log_level="warning")
