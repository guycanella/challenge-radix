from fastapi import Request, Response
from fastapi.responses import JSONResponse
from typing import Callable

async def not_allowed(req: Request, call_next: Callable[[Request], Response]):
    response = await call_next(req)

    if response.status_code == 404:
        return JSONResponse(
            status_code = 404,
            content = { "message": "Route not allowed." }
        )

    return response