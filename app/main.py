import asyncio
import time

from fastapi import FastAPI, HTTPException, Request, status
from app.api.elements import routers as elements_router
from app.api.users import routers as user_router
from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Leads Project')

@app.middleware("http")
async def timeout_middleware(request: Request, call_next):

    # Time in seconds
    REQUEST_TIMEOUT_ERROR = 10

    try:
        start_time = time.time()
        return await asyncio.wait_for(call_next(request), timeout=REQUEST_TIMEOUT_ERROR)

    except asyncio.TimeoutError:
        process_time = time.time() - start_time
        return JSONResponse({'detail': 'Request processing time excedeed limit',
                             'processing_time': process_time},
                            status_code=status.HTTP_504_GATEWAY_TIMEOUT)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    user_router.router,
    tags=['User'],
)


app.include_router(
    elements_router.router,
    prefix='/elements',
    tags=['Elements To Process'],
)
