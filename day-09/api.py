from fastapi import FastAPI

app = FastAPI(
    title="Project Api",
    description="This is api for internal project",
    version="1.0.0",
    docs_url="/doc",
    redoc_url="/redoc"
)

@app.get("/health")
def health():
    """
    This is health status check api
    """
    return {"message": "Application is health"}

@app.get("/logs")
def log():
    """
    This is log demonstrating api
    """
    return {"message": "All is well there is no Error"}
