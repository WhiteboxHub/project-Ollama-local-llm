import httpx
import os

# Use environment variable for flexibility, default to Docker service name
OLLAMA_URL = os.getenv("OLLAMA_HOST", "http://ollama:11434")

async def generate(prompt: str, model="qwen2.5:1.5b"):
    try:
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json().get("response", "")
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {e.request.url!r}.")
        raise
    except httpx.HTTPStatusError as e:
        print(f"Error response {e.response.status_code} while requesting {e.request.url!r}.")
        raise
