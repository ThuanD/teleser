 # Remote Command Bot

A Telegram bot for remote command execution with optional user authorization, customizable command validation, and customizable messages.

## Installation
```
pip install teleser
```

## Usage

### With custom messages and user authorization:

```python
from teleser import TeleSerBot

AUTHORIZED_USERS = [123456789, 987654321]  # Replace with actual Telegram user IDs

CUSTOM_DANGEROUS_PATTERNS = [r"your_custom_pattern"]
CUSTOM_ALLOWED_COMMANDS = ["your_custom_command"]

CUSTOM_MESSAGES = {
    "start": "Welcome! You can use these commands: {allowed_commands}",
    "unauthorized": "Access denied. You are not authorized.",
    "command_result": "Here's the output:\n{result}",
}

def main():
    bot = TeleSerBot(
        "TELEGRAM_BOT_TOKEN",
        authorized_users=AUTHORIZED_USERS,
        dangerous_patterns=CUSTOM_DANGEROUS_PATTERNS,
        allowed_commands=CUSTOM_ALLOWED_COMMANDS,
        custom_messages=CUSTOM_MESSAGES
    )
    bot.run_sync()

if __name__ == '__main__':
    main()
```

### Without customization (default settings):
```python
from teleser import TeleSerBot

def main():
    bot = TeleSerBot("TELEGRAM_BOT_TOKEN")
    bot.run_sync()


if __name__ == '__main__':
    main()
```