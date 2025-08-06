from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from auth import verify_api_key
from model import generate_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: Request, data: ChatRequest):
    verify_api_key(request)
    user_message = data.message
    response = generate_response(user_message)
    return {"response": response}
