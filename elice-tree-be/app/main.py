from fastapi import FastAPI
import uvicorn
from app.routers import auth, mission


app = FastAPI()
app.include_router(auth.router, tags=["auth"])
app.include_router(mission.router, tags=["mission"])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
# uvicorn app.main:app --reload --host 127.0.0.1 --port 8080
