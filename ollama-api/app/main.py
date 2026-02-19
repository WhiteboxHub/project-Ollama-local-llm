from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.ollama_client import generate

app = FastAPI(title="Local Ollama API")

class PromptRequest(BaseModel):
    prompt: str
    model: str | None = "qwen2.5:1.5b"

@app.post("/generate")
async def generate_text(req: PromptRequest):
    try:
        output = await generate(req.prompt, req.model)
        return {"output": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "ok"}
