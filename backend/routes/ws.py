from datetime import datetime
from typing import List
from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect, status
from jose import JWTError
from utils.token import decode_token
from db.mongo_instance import mongoDB

router = APIRouter(prefix='/ws')

connections = dict[str, List[WebSocket]] = {}

@router.websocket('/chat/{room_id}')
async def websocket_connection(request: Request, ws : WebSocket, room_id: str ):
    message_collection = mongoDB.db['messages']
    room_collection = mongoDB.db['rooms']
    username = request.state.user['username']
    if not username:
        raise ValueError("No username in token")
    

    print(f"User {username} connected to room {room_id}")
    room = room_collection.find_one({"room_id" : room_id, "participants" : username})
    if not room:
        await ws.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    
    await ws.accept()
        
    
    if room_id not in connections:
        connections[room_id] = []
    connections[room_id].append(ws)
    
    try:
        while True:
            data = await ws.receive_json()
            message_data = {
               "room_id": room_id,
                "sender": username, 
                "message": data.get("message"),
                "timestamp": datetime.utcnow()
            }
            message_collection.insert_one(message_data)
            for conn in connections[room_id]:
                if conn != ws:
                    await conn.send_json(message_data)
    except WebSocketDisconnect:
        connections[room_id].remove(ws)
                    
                