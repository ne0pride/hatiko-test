import httpx
import os

# Загрузить API ключ из переменных окружения (или вставь вручную)
API_TOKEN_IMEI = 'e4oEaZY1Kom5OXzybETkMlwjOCy3i8GSCGTHzWrhd4dc563b'

# URL API
SERVICES_API_URL = "https://api.imeicheck.net/v1/services"


async def get_service_ids():
    """Запрашивает список доступных serviceId с API IMEICheck.net"""
    headers = {
        'Authorization': f'Bearer {API_TOKEN_IMEI}',
        'Accept-Language': 'en'
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(SERVICES_API_URL, headers=headers)

    if response.status_code == 200:
        return response.json()  # ✅ Возвращает список serviceId
    else:
        print(f"Ошибка {response.status_code}: {response.text}")
        return None


# Асинхронный запуск (если в обычном скрипте)
import asyncio

services = asyncio.run(get_service_ids())
print(services)
