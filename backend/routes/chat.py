from fastapi import APIRouter, HTTPException, Request
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
        "room_id" : str(uuid.uuid4()),
        "owner" : request.state.user['name'],
        "participants" : [request.state.user['username']],
        "created_at" : datetime.utcnow()
    }
    room_collection.insert_one(room_details)
    return {"message": "Room created successfully", "room_id": room_details["room_id"]}


@router.get("/rooms")
def get_rooms(request: Request):
    room_collection = mongoDB.db['rooms']
    rooms = list(room_collection.find({"participants": request.state.user['username']}))
    for room in rooms:
        room["_id"] = str(room["_id"]) 
    return {"rooms": rooms}

@router.post("/join_room/{room_id}")
def join_room(request: Request, room_id: str):
    room_collection = mongoDB.db['rooms']
    room = room_collection.find_one({"room_id" : room_id})
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    if request.state.user['username'] in  room.get('participants'):
        raise HTTPException(status_code=400 , detail="User already a member")
    room_collection.update_one({
        "room_id": room_id
    }, {
        "$push" : {
            "participants" : request.state.user['username']
        }
    })
    return {"message": f"Joined room {room['room_name']}"}

