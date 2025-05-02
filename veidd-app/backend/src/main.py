from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .core.config import settings
from .api import auth, users

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API for the VEIDD (Visual recognition, Evaluation, Intactness, Difficulty, Decisioning) system",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(users.router, prefix=f"{settings.API_V1_STR}/users", tags=["users"])

@app.get("/")
async def root():
    return JSONResponse(
        content={
            "message": "Welcome to VEIDD API",
            "version": "0.1.0",
            "status": "operational"
        }
    )

@app.get("/health")
async def health_check():
    return JSONResponse(
        content={
            "status": "healthy",
            "version": "0.1.0"
        }
    ) 