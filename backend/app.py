from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.mongo_instance import mongoDB
from routes import auth, chat, ws
from middleware.auth_middleware import AuthMiddleware
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    mongoDB.connect()
    yield
    mongoDB.disconnect()

app = FastAPI(lifespan=lifespan)

app.add_middleware(AuthMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(ws.router)


@app.get('/')
def details():
    return {
        "Application": "ChatApp"
    }
