from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from utils.token import decode_token
from jose import JWTError

ALLOWED_ROUTES = ["/auth/login/", "/auth/register/", "/auth/login", "/auth/register"]

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path in ALLOWED_ROUTES:
            return await call_next(request)

        header = request.headers.get('Authorization')
        if header and header.startswith("Bearer "):
            token = header.split(" ")[1]
            try:
                payload = decode_token(token=token)
                request.state.user = payload
            except JWTError:
                return JSONResponse(status_code=401, content={"message": "Invalid token"})
        else:
            return JSONResponse(status_code=401, content={"message": "Authorization header missing or invalid"})
        
        return await call_next(request)
