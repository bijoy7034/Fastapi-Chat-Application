from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.mongo_instance import mongoDB
from routes import auth, chat
from middleware.auth_middleware import AuthMiddleware



@asynccontextmanager
async def lifespan(app: FastAPI):
    mongoDB.connect()
    yield
    mongoDB.disconnect()

app = FastAPI(lifespan= lifespan)

app.add_middleware(AuthMiddleware)

app.include_router(auth.router)
app.include_router(chat.router)


@app.get('/')
def details():
    return {
        "Application" : "ChatApp"
    }
