from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from .core.database import init_db
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from .users.routes import user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.mount("/frontend/static", StaticFiles(directory="frontend/static"), name="static")
#app.mount("/frontend/scripts", StaticFiles(directory="frontend/scripts"), name="scripts")
app.mount("/frontend/templates/assets", StaticFiles(directory="frontend/templates/assets"), name="assets")
templates = Jinja2Templates(directory="frontend/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500", "http://127.0.0.1:5000", "http://localhost:5000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(user_router, prefix=f"/user")

@app.get("/", response_class=HTMLResponse)
async def serve_root():
    return RedirectResponse(url="/signup.html")

@app.get("/signup.html", response_class=HTMLResponse)
async def serve_signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.get("/login.html", response_class=HTMLResponse)
async def serve_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/index.html", response_class=HTMLResponse)
async def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
