from pydantic import BaseModel

class CreateRoom(BaseModel):
    room_name : str

class Message(BaseModel):
    room_id: str
    message: str