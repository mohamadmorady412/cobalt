import httpx

from config import BACKEND_SERVICE_URL


async def forward_request(path: str, request):
    """
    Forwards the incoming request to the backend service.
    The `path` parameter is the target path of the request.
    """
    url = f"{BACKEND_SERVICE_URL}/{path}"
    async with httpx.AsyncClient() as client:
        # Sending the request to the backend server
        response = await client.request(
            method=request.method,
            url=url,
            headers=request.headers.raw,
            content=await request.body(),
        )
    return response
