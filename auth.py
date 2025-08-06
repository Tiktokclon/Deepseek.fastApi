from fastapi import Request, HTTPException

API_KEY = "123456789"  # Tu peux changer ça

def verify_api_key(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Clé API manquante")
    
    token = auth_header.split(" ")[1]
    if token != API_KEY:
        raise HTTPException(status_code=403, detail="Clé API invalide")
