from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api import router

app = FastAPI(
    title="Email Classification API",
    description="Classifies support emails and masks PII",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def root():
    return RedirectResponse(url="/docs")
