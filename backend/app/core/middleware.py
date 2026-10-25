import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from backend.app.core.logging import logger


class RequestTimingAndLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware that attaches a unique request_id, calculates response processing time (X-Process-Time),
    and records structured request logs.
    """

    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        start_time = time.perf_counter()

        response = await call_next(request)

        process_time_ms = round((time.perf_counter() - start_time) * 1000, 2)
        response.headers["X-Process-Time"] = f"{process_time_ms}ms"
        response.headers["X-Request-ID"] = request_id

        logger.info(
            f"HTTP {request.method} {request.url.path} - {response.status_code} ({process_time_ms}ms)",
            extra={
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration_ms": process_time_ms,
            },
        )

        return response
