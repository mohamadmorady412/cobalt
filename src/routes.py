from fastapi import APIRouter, Request

from services.proxy import forward_request

router = APIRouter()


@router.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_route(full_path: str, request: Request):
    return await forward_request(full_path, request)
