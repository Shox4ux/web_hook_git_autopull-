from fastapi import FastAPI, Request, HTTPException
import subprocess
import hmac
import hashlib
import os

app = FastAPI()

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
if not WEBHOOK_SECRET:
    raise RuntimeError("WEBHOOK_SECRET is not set")

DEPLOY_SCRIPT = "/opt/deploy/deploy.sh"


def verify_signature(payload: bytes, signature: str):
    mac = hmac.new(WEBHOOK_SECRET.encode(), msg=payload, digestmod=hashlib.sha256)
    expected = "sha256=" + mac.hexdigest()
    return hmac.compare_digest(expected, signature)


@app.post("/webhook")
async def webhook(request: Request):
    signature = request.headers.get("X-Hub-Signature-256")
    body = await request.body()

    print("SIGNATURE HEADER:", signature)
    print("RAW BODY:", body)

    if not signature:
        raise HTTPException(status_code=403, detail="Missing signature")

    if not verify_signature(body, signature):
        raise HTTPException(status_code=403, detail="Invalid signature")

    subprocess.Popen([DEPLOY_SCRIPT])
    return {"status": "deploy started"}


# @app.post("/webhook")
# async def webhook(request: Request):
#     signature = request.headers.get("X-Hub-Signature-256")
#     body = await request.body()

#     if not signature or not verify_signature(body, signature):
#         raise HTTPException(status_code=403, detail="Invalid signature")

#     subprocess.Popen(
#         [DEPLOY_SCRIPT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
#     )

#     return {"status": "deploy started"}
