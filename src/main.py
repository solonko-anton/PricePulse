import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from src.routes import get_apps_router
from src.app_instance import app
from src.config.project_config import settings


app.title = settings.PROJECT_NAME
app.debug = settings.DEBUG
app.version = settings.VERSION

app.include_router(get_apps_router())

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
