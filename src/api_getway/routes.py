from fastapi import APIRouter, Request
from services.proxy import forward_request

router = APIRouter()


# This route forwards requests to the backend server.
# The path is dynamic, handling methods like GET, POST, PUT, and DELETE.
@router.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_route(full_path: str, request: Request):
    """
    This function forwards the requests to the backend service.
    The `full_path` parameter captures the dynamic path from the incoming request.
    """
    return await forward_request(full_path, request)
