from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from utils.token import decode_token
from jose import JWTError

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        header = request.headers.get('Authorization')
        if header and header.startswith("Bearer "):
            token = header.split(" ")[1]
            try:
                payload = decode_token(token=token)
                request.state.user = payload
            except JWTError as e:
                return JSONResponse(status_code=401, content={"detail": "Invalid token"})
        else:
            request.state.user = None
        response = await call_next
        return response
        