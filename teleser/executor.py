import asyncio
from .validator import CommandValidator


class CommandExecutor:
    def __init__(self, validator: CommandValidator, message_handler):
        self.validator = validator
        self.message_handler = message_handler

    async def execute_command(self, command: str) -> str:
        if not self.validator.is_command_safe(command):
            return self.message_handler.get_message("command_not_allowed")

        try:
            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()

            if process.returncode == 0:
                return stdout.decode()
            else:
                return f"Error: {stderr.decode()}"
        except Exception as e:
            return f"Error: {str(e)}"
