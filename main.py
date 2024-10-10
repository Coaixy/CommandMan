import time
from fastapi.responses import StreamingResponse

from fastapi import FastAPI

from routes import users

app = FastAPI()

# 服务器端推送Demo'
def event_stream():
    while True:
        time.sleep(1)
        yield f"data: 当前时间为 {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"


@app.get("/")
async def root():
    return StreamingResponse(event_stream(), media_type="text/event-stream")


app.include_router(users.router, prefix="/users", tags=["users"])