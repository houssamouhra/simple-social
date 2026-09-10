import uvicorn


def main() -> None:
    uvicorn.run("simple_social.main:app", reload=True)
