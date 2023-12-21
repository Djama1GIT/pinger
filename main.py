import asyncio

import aiohttp as aiohttp
from aiohttp import ClientSession

from logger import logger
from config import settings
import telebot

bot = telebot.TeleBot(settings.TOKEN)
updates = bot.get_updates()


async def ping_site(session: ClientSession, url: str):
    try:
        async with session.get(url) as response:
            logger.info(response)
            return response.status == 200
    except:
        return False


async def send_notification(site: str, available=True):
    bot.send_message(
        settings.CHAT_ID,
        '```Внимание!\n'
        f'Сайт {site} {"" if available else "не"}доступен!\n'
        '```',
        parse_mode="markdown"
    )


async def check_sites():
    prev_states: dict[str, bool] = {}
    async with aiohttp.ClientSession() as session:
        while True:
            await asyncio.sleep(300)
            for site in settings.SITE:
                available = await ping_site(session, site)
                if not available or prev_states[site] != available:
                    await send_notification(site, available)
                prev_states[site] = available
            bot.send_message(settings.CHAT_ID, "=====================")


async def first_launch():
    async with aiohttp.ClientSession() as session:
        for site in settings.SITES:
            available = await ping_site(session, site)
            await send_notification(site, available)
        bot.send_message(settings.CHAT_ID, "=====================")


if __name__ == '__main__':
    asyncio.run(first_launch())
    asyncio.run(check_sites())
