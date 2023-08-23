import os, sys
from uvicorn import run
from fastapi import FastAPI

# adds investor_bulletin path to pythonpath.
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

from _config.config import load_env
load_env('../.env')

from api.routes import init_routes
app = init_routes(FastAPI())

if __name__ == "__main__":
    run("api.main:app", host="0.0.0.0", port=8000)
