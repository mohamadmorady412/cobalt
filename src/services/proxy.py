import httpx

from config import BACKEND_SERVICE_URL


async def forward_request(path: str, request):
    url = f"{BACKEND_SERVICE_URL}/{path}"
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=url,
            headers=request.headers.raw,
            content=await request.body(),
        )
    return response
