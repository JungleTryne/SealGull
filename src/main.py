from typing import Optional

import discord
import logging
import os

from client.sealgull_client import SealgullClient

from loguru import logger

SEALGULL_TOKEN: Optional[str] = os.getenv("SEALGULL_TOKEN")
discord.utils.setup_logging(level=logging.INFO, root=False)

if __name__ == "__main__":
    if SEALGULL_TOKEN is None:
        logger.error("SEALGULL_TOKEN is not specified")
    else:
        SealgullClient().run(SEALGULL_TOKEN)
