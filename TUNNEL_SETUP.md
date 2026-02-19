# Exposing Your Local API to the Internet

## Option A: Cloudflare Tunnel (Recommended)

1.  **Install `cloudflared`**:
    Download from [Cloudflare Downloads](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/).

2.  **Login**:
    ```powershell
    cloudflared tunnel login
    ```

3.  **Start Tunnel**:
    ```powershell
    cloudflared tunnel --url http://localhost:8000
    ```
    You will get a URL like `https://random-name.trycloudflare.com`.

## Option B: ngrok

1.  **Install ngrok**:
    [Sign up and download](https://ngrok.com/download).

2.  **Start Tunnel**:
    ```powershell
    ngrok http 8000
    ```
    You will get a URL like `https://random-id.ngrok-free.app`.

## Usage
Once you have the public URL:
```bash
curl -X POST https://your-public-url/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello via internet"}'
```
