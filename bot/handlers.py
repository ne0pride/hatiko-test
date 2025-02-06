import json

import httpx
from aiogram import Router, types
from aiogram.filters import Command
from config import API_URL, SECURE_API_TOKEN, ALLOWED_USERS

router = Router()

@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Отправьте IMEI для проверки.")

@router.message()
async def handle_imei(message: types.Message):
    user_id = message.from_user.id
    if user_id not in ALLOWED_USERS:
        await message.answer("У вас нет доступа к боту.")
        return

    imei = message.text.strip()
    if not imei.isdigit() or len(imei) not in {14, 15}:
        await message.answer("Неверный формат IMEI. Введите 14-15 цифр.")
        return

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(API_URL, json={"imei": imei, "token": SECURE_API_TOKEN})
            data = response.json()
        details = json.loads(data.get("detail", "{}"))
        print(data)
        inf = "Информация недоступна."
        if "properties" in details:
            props = details["properties"]
            inf = (f"✅ Данные по IMEI:\n"
                    f"📱 Устройство: {props.get('deviceName', 'Неизвестно')}\n"
                    f"🌍 Регион: {props.get('apple/region', 'Неизвестно')}\n"
                    f"📦 Модель: {props.get('apple/modelName', 'Неизвестно')}\n"
                    f"🔢 IMEI: {props.get('imei', 'Неизвестно')}\n"
                    f"📶 Сеть: {props.get('network', 'Неизвестно')}\n"
                    f"🔄 Заменённый: {'Да' if props.get('replaced') else 'Нет'}\n"
                    f"⚠️ Блокировка в США: {props.get('usaBlockStatus', 'Неизвестно')}\n"
                    f"🛠 Поддержка: {'Активна' if props.get('technicalSupport') else 'Нет'}\n"
                    f"🆔 Серийный номер: {props.get('serial', 'Неизвестно')}\n"
                    f"📸 Изображение: [Посмотреть]({props.get('image', '#')})")
        await message.answer(inf)
    except Exception:
        await message.answer("Ошибка при проверке IMEI. Попробуйте позже.")
