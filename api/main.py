from fastapi import FastAPI, HTTPException
from .models import IMEICheckRequest
from .service import check_imei
from .config import SECURE_API_TOKEN


app = FastAPI()


@app.post("/api/check-imei")
async def check_imei_api(request: IMEICheckRequest):
    """API для проверки IMEI"""
    print(request.token, SECURE_API_TOKEN)
    if request.token != SECURE_API_TOKEN:
        raise HTTPException(status_code=403, detail="Неверный токен")
    return await check_imei(request.imei)
