# Local Ollama LLM Infrastructure

This directory contains a containerized setup for hosting a local LLM API using **Ollama** and a **FastAPI** wrapper. It is designed to provide a high-performance, cost-effective alternative to cloud LLM APIs for tasks like job classification and text analysis.

## 🚀 Quick Start

### 1. Start Infrastructure
Run the following command to start both the Ollama engine and the FastAPI proxy:
```bash
docker-compose up -d
```

### 2. Download Model
The first time you run the setup, you must pull the model into the persistent volume:
```bash
docker exec ollama ollama pull qwen2.5:1.5b
```

### 3. Verify Setup
Check if the API is responding correctly:
```bash
# Health Check
curl http://localhost:8000/health

# Test Generation
curl -X POST http://localhost:8000/generate \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Hello", "model": "qwen2.5:1.5b"}'
```

---

## 🏗️ Architecture

- **Ollama Engine** (Port 11434): The core LLM engine.
- **FastAPI Wrapper** (Port 8000): Provides a simplified JSON interface and handles model orchestration.

## ⚙️ Configuration

### Docker Compose
- **Service `ollama`**: Hosts the LLM models. Data is persisted in the `ollama_data` volume.
- **Service `api`**: Built from `./ollama-api`. Connects to `ollama:11434`.

### Models
By default, the setup uses `qwen2.5:1.5b` for its excellent performance-to-size ratio. You can pull other models if needed:
```bash
docker exec ollama ollama pull llama3
```

---

## 🛠️ Troubleshooting

### 404 Model Not Found
If you get a 404 error when calling `/generate`, it means the model hasn't been pulled inside the container yet. Run the `ollama pull` command mentioned in the Quick Start.

### Connection Refused (Port 11434)
If you have the **Ollama Windows App** running on your host, it will bind to port 11434. The Docker container may fail to expose this port to the host, but the `api` container can still talk to the `ollama` container **internally** via the `ollama-net` network.

### Docker Desktop Issues
Ensure Docker Desktop is running and the "Linux Engine" is active. If you see errors about `//./pipe/dockerDesktopLinuxEngine`, restart Docker Desktop.