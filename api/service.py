import httpx
import os
import json
from fastapi import HTTPException
from .models import IMEICheckRequest
from .config import API_TOKEN_IMEI, IMEI_API_URL, SERVICES_API_URL


async def get_service_id():
    """Получает доступные serviceId и выбирает первый"""
    headers = {
        'Authorization': f'Bearer {API_TOKEN_IMEI}',
        'Accept-Language': 'en'
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(SERVICES_API_URL, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Ошибка при получении списка serviceId")

    services = response.json()

    if not services:
        raise HTTPException(status_code=404, detail="Нет доступных serviceId")

    return services[0]['id']


async def check_imei(imei: str):
    """Отправляет запрос к API IMEICheck и возвращает результат"""
    service_id = await get_service_id()

    payload = json.dumps({
        "deviceId": imei,
        "serviceId": service_id
    })

    headers = {
        'Authorization': f'Bearer {API_TOKEN_IMEI}',
        'Accept-Language': 'en',
        'Content-Type': 'application/json'
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(IMEI_API_URL, headers=headers, data=payload)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    result = response.json()

    return (result)
