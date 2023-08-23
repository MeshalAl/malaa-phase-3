from fastapi import FastAPI
from uvicorn import run
from controllers.messaging_controller import router as MessagingRouter

def init_routes(app: FastAPI):
    app.include_router(MessagingRouter, prefix="/messaging", tags=["Messaging"])
    return app

app = init_routes(FastAPI())

if __name__ == "__main__":
    run("api:app", host="0.0.0.0", port=8001, reload=True)
