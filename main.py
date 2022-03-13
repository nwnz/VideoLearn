from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import users, courses, lessons, token

app = FastAPI()

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(lessons.router)
app.include_router(token.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "pong!"}
