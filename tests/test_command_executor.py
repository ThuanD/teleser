import pytest
from unittest.mock import MagicMock
from teleser.executor import CommandExecutor


@pytest.mark.asyncio
async def test_execute_safe_command():
    validator = MagicMock()
    validator.is_command_safe.return_value = True
    message_handler = MagicMock()
    executor = CommandExecutor(validator, message_handler)

    result = await executor.execute_command("echo test")
    assert "test" in result


@pytest.mark.asyncio
async def test_execute_unsafe_command():
    validator = MagicMock()
    validator.is_command_safe.return_value = False
    message_handler = MagicMock()
    message_handler.get_message.return_value = "Command not allowed"
    executor = CommandExecutor(validator, message_handler)

    result = await executor.execute_command("rm -rf /")
    assert result == "Command not allowed"
