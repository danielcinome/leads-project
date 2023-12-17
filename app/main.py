from fastapi import FastAPI
from app.api.elements import routers as elements_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Leads Prject')


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    elements_router.router,
    prefix='/elements',
    tags=['Elements To Process'],
)
