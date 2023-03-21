import subprocess
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


def mainPage():
    html_content = """
    <html>
        <head>
            <title>Payload 2023 - Rover</title>
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body>
           <div class="flex h-screen items-center justify-center">
                <a href="http://raspberrypi.local:8000/record" class="rounded-full bg-red-700 py-4 px-8 font-bold text-white hover:bg-red-600"> Record </a>
            </div>
        </body>
        <style>
  .h-screen {
    height: 100vh;
  }
  
  @media (min-width: 640px) {
    /* Small screens */
    .py-4 {
      padding-top: 1rem;
      padding-bottom: 1rem;
    }
    .px-8 {
      padding-left: 2rem;
      padding-right: 2rem;
    }
  }
  
  @media (min-width: 768px) {
    /* Large screens */
    .py-6 {
      padding-top: 1.5rem;
      padding-bottom: 1.5rem;
    }
    .px-10 {
      padding-left: 2.5rem;
      padding-right: 2.5rem;
    }
  }
        </style>
    </html>

    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/")
def read_root():
    return mainPage()


@app.get("/record")
def recordData():
    return subprocess.run(["python3", "rover/mpu.py"])
