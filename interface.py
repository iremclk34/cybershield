from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>CyberShield Tarama Arayüzü</h2>
    <form action="/tara" method="post">
        <label>Başlangıç IP (örn: 1):</label>
        <input name="baslangic" type="number" required><br><br>
        <label>Bitiş IP (örn: 10):</label>
        <input name="bitis" type="number" required><br><br>
        <button type="submit">Taramayı Başlat</button>
    </form>
    """

@app.post("/tara", response_class=HTMLResponse)
def tara(baslangic: int = 1, bitis: int = 10):
    subprocess.run(
        ["python", "network_scan.py", str(baslangic), str(bitis)],
        capture_output=True,
        text=True
    )

    with open("output.txt", "r", encoding="utf-8") as file:
        tarama_sonucu = file.read()

    return HTMLResponse(f"<h3>Tarama tamamlandı.</h3><pre>{tarama_sonucu}</pre>")
if _name_ == "_main_":
   import uvicorn
 uvicorn.run(app, host="127.0.0.1", port=8000)

