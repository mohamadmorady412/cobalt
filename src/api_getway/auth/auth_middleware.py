from auth.jwt import verify_token
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class AuthMiddleware(BaseHTTPMiddleware):
    """
    This middleware is responsible for verifying the JWT token in the request.
    If the token is missing or invalid, a 401 Unauthorized response is returned.
    """

    async def dispatch(self, request: Request, call_next):
        # Check if the Authorization header is present
        if "authorization" not in request.headers:
            return JSONResponse(status_code=401, content={"detail": "Missing token"})

        # Extract the token from the Authorization header
        token = request.headers.get("authorization").replace("Bearer ", "")
        verify_token(token)  # Verifying the token

        # If the token is valid, proceed with the request
        return await call_next(request)
