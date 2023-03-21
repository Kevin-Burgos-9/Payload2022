import subprocess
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

def mainPage():
    html_content= """
    <html>
        <head>
            <title>Payload 2023 - Rover</title>
        </head>
        <body>
            <a href="http://raspberrypi.local:8000/record">Record MPU data </a>
        </body>

    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/")
def read_root():
    return mainPage()


@app.get("/record")
def recordData():
    return subprocess.run(["python3", "/rover/mpu.py"])
