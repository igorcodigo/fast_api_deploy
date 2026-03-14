from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hello World</title>
<style>
  body { margin:0; height:100vh; display:flex; justify-content:center;
         align-items:center; background:linear-gradient(135deg,#667eea,#764ba2);
         font-family:system-ui; color:#fff; text-align:center; }
  h1 { font-size:4rem; margin:0; text-shadow:2px 4px 8px rgba(0,0,0,.3); }
  p { font-size:1.2rem; opacity:.8; }
</style>
</head>
<body>
<div><h1>Hello, World!</h1><p>FastAPI rodando na porta 4050</p></div>
</body>
</html>"""


@app.get("/", response_class=HTMLResponse)
async def root():
    return HTML
