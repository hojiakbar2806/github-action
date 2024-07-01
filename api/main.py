from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(
    title="FastAPI",
    description="Test",
    version="0.0.1",
    contact={
        "name": "Hojiakbar",
        "email": "hojiakbarnasriddinov2006@gmail.com",
        "tel": "+998993250628"
    }
)


@app.get('/')
async def get():
    return {"message": "Hello World"}

handler = Mangum(app=app)
