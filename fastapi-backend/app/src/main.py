from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI()


@app.get("/")
def read_home():
    return RedirectResponse(url="/home")


@app.get("/home")
def home():
    return {"page": "home"}


@app.get("/about")
def about():
    return {"page": "about"}


@app.get("/contact")
def contact():
    return {"page": "contact"}


@app.get("/")
def root():
    return {"message": "Hello, Welcome to our project!"}


@app.get("/framing", response_class=HTMLResponse)
async def read_framing():
    with open("framing.md", "r") as file:
        content = file.read()
    return Response(content=content, media_type="text/markdown")


@app.get("/effects_of_war")
def root():
    return {"message": "Hello,Effects of War!"}


@app.get("/visible")
def root():
    return {"message": "Hello, visible!"}


@app.get("/invisible")
def root():
    return {"message": "Hello, invisible!"}


# if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=8000)
