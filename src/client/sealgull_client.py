import discord
from loguru import logger


class SealgullClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(intents=intents)

    async def on_ready(self):
        logger.info("Bot is ready! :)")
