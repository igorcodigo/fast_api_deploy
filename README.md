# Fast API Simple

Hello World com FastAPI rodando na porta 4050.

## Deploy na VPS

### 1. Instalar Python e dependências do sistema

```bash
sudo apt update && sudo apt install -y python3 python3-pip
```

### 2. Instalar o UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
```

### 3. Clonar e instalar

```bash
git clone <url-do-repo>
cd fast-api-simple
uv sync
```

### 4. Rodar

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 4050
```

Acesse `http://<IP-DA-VPS>:4050` no navegador.

> Se a porta estiver bloqueada: `sudo ufw allow 4050`

Para rodar em background (sobrevive ao fechar o terminal):

```bash
nohup uv run uvicorn main:app --host 0.0.0.0 --port 4050 > app.log 2>&1 &
```

Para parar: `kill $(lsof -t -i:4050)`

---

### Produção com systemd (opcional)

Crie `/etc/systemd/system/fastapi-hello.service`:

```ini
[Unit]
Description=FastAPI Hello World
After=network.target

[Service]
User=<USER>
WorkingDirectory=/home/<USER>/fast-api-simple
ExecStart=/home/<USER>/fast-api-simple/.venv/bin/uvicorn main:app --host 0.0.0.0 --port 4050
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable fastapi-hello
sudo systemctl start fastapi-hello
```

Comandos úteis:

```bash
sudo systemctl status fastapi-hello   # ver status
sudo journalctl -u fastapi-hello -f   # ver logs
sudo systemctl restart fastapi-hello   # reiniciar
```
# fast_api_deploy
