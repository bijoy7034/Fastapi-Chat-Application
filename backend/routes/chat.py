from fastapi import APIRouter, Body, HTTPException, Request
from models.chat import CreateRoom
from db.mongo_instance import mongoDB
import uuid
from datetime import datetime

router = APIRouter(prefix="/chat")

@router.post("/create_room")
def create_room(request: Request, room: CreateRoom):
    room_collection = mongoDB.db['rooms']
    existing_room = room_collection.find_one({"room_name": room.room_name})
    if existing_room:
        raise HTTPException(status_code=400, detail="Room already exists")
    room_details = {
        "room_name" : room.room_name,
        "room_id" : str(uuid.uuid1()),
        "owner" : request.state.user['name'],
        "participants" : [request.state.user['username']],
        "created_at" : datetime.utcnow()
    }
    room_collection.insert_one(room_details)
    return {"message": "Room created successfully", "room_id": room_details["room_id"]}
