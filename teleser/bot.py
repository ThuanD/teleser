import logging
import nest_asyncio
from typing import List, Optional, Dict
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from .executor import CommandExecutor
from .messages import TeleMessageHandler
from .validator import CommandValidator

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

nest_asyncio.apply()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    allowed_commands = ", ".join(context.bot_data["validator"].allowed_commands)
    message = context.bot_data["message_handler"].get_message(
        "start",
        allowed_commands=allowed_commands)
    await update.message.reply_text(message)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    authorized_users = context.bot_data.get("authorized_users")

    if authorized_users is not None and user_id not in authorized_users:
        message = context.bot_data["message_handler"].get_message("unauthorized")
        await update.message.reply_text(message)
        return

    command = update.message.text
    result = await context.bot_data["executor"].execute_command(command)
    message = context.bot_data["message_handler"].get_message(
        "command_result",
        result=result)
    await update.message.reply_text(message)


class TeleSerBot:
    def __init__(
            self,
            token: str,
            authorized_users: Optional[List[int]] = None,
            dangerous_patterns: Optional[List[str]] = None,
            allowed_commands: Optional[List[str]] = None,
            custom_messages: Optional[Dict[str, str]] = None,
    ):
        self.application = Application.builder().token(token).build()

        if authorized_users is not None:
            self.application.bot_data["authorized_users"] = authorized_users

        message_handler = TeleMessageHandler(custom_messages)
        validator = CommandValidator(dangerous_patterns, allowed_commands)
        executor = CommandExecutor(validator, message_handler)

        self.application.bot_data["message_handler"] = message_handler
        self.application.bot_data["validator"] = validator
        self.application.bot_data["executor"] = executor

        self.application.add_handler(CommandHandler("start", start))
        self.application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    async def run(self):
        await self.application.run_polling()

    def run_sync(self):
        import asyncio
        asyncio.run(self.run())
