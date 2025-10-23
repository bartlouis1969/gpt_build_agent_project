import subprocess
import time
import pytest


@pytest.fixture(scope="session", autouse=True)
def start_fastapi_server():
    # Start de FastAPI server via uvicorn in de achtergrond
    server = subprocess.Popen(
        [
            "python",
            "-m",
            "uvicorn",
            "app.main:app",
            "--host",
            "127.0.0.1",
            "--port",
            "8000",
        ]
    )
    time.sleep(3)  # Geef de server tijd om op te starten
    yield
    server.terminate()
    server.wait()
