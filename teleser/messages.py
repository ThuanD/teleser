DEFAULT_MESSAGES = {
    "start": "Hi! You can execute the following commands:\n{allowed_commands}",
    "unauthorized": "Sorry, you are not authorized to use this bot.",
    "command_result": "{result}",
    "command_not_allowed": "Error: This command is not allowed for security reasons."
}


class TeleMessageHandler:
    def __init__(self, custom_messages=None):
        self.messages = DEFAULT_MESSAGES.copy()
        if custom_messages:
            self.messages.update(custom_messages)

    def get_message(self, key, **kwargs):
        return self.messages[key].format(**kwargs)
