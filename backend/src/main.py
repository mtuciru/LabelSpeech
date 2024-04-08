import uvicorn
from settings import settings
from db.initdb import initdb
from fastapi import FastAPI
from routers import router

app = FastAPI(debug=settings.SERVER_TEST)
app.include_router(router)
initdb()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.SERVER_ADDR,
        port=settings.SERVER_PORT,
        reload=settings.SERVER_TEST,
        log_level="debug" if settings.SERVER_TEST else "info",
    )
