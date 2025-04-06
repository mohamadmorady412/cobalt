from fastapi import FastAPI
from slowapi.middleware import SlowAPIMiddleware

from auth.auth_middleware import AuthMiddleware
from middleware.rate_limiter import limiter
from routes import router

app = FastAPI()
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(AuthMiddleware)
app.include_router(router)
