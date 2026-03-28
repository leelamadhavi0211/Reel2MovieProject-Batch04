from fastapi import Request
from auth.jwt_handler import decode_token

def get_current_user(request: Request):
    auth = request.headers.get("Authorization")

    if not auth:
        return None  # ✅ allow guest

    try:
        token = auth.split(" ")[1]
        # decode token logic
        user = decode_token(token)
        return user
    except:
        return None