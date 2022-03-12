from fastapi import FastAPI

from routers import users, courses, lessons

app = FastAPI()

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(lessons.router)


@app.get("/")
async def root():
    return {"message": "pong!"}
