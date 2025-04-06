from auth.auth_middleware import AuthMiddleware
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from middleware.rate_limiter import limiter
from routes import router
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI()

# Setting up security layers and rate-limiting for the application.
# Requests are verified through the AuthMiddleware,
# and rate-limiting is handled via SlowAPIMiddleware and Limiter.
app.state.limiter = limiter

# Adding middlewares to the app
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(AuthMiddleware)

# Including the routes for the application
app.include_router(router)
