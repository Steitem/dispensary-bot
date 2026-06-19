import asyncio
from aiogram import Bot
from aiogram.types import BotCommand
from config import TOKEN

async def set_commands():
    bot = Bot(token=TOKEN)
    
    commands = [
        BotCommand(command="start", description="Запустить бота / Главное меню"),
        BotCommand(command="back", description="Вернуться в главное меню"),
    ]
    
    await bot.set_my_commands(commands)
    print("✅ Команды установлены: /start и /back")
    
    # Проверяем, что установилось
    current_commands = await bot.get_my_commands()
    print(f"📋 Текущие команды: {[cmd.command for cmd in current_commands]}")
    
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(set_commands())