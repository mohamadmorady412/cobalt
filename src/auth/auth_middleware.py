from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from auth.jwt import verify_token


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if "authorization" not in request.headers:
            return JSONResponse(status_code=401, content={"detail": "Missing token"})

        token = request.headers.get("authorization").replace("Bearer ", "")
        verify_token(token)
        return await call_next(request)
