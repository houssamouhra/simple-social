import uvicorn


def main() -> None:
    uvicorn.run("media_manager.main:app", reload=True)
