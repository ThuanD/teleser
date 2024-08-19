from teleser.messages import TeleMessageHandler, DEFAULT_MESSAGES


def test_default_messages():
    handler = TeleMessageHandler()
    assert handler.get_message(
        "start",
        allowed_commands="ls, pwd"
    ) == DEFAULT_MESSAGES["start"].format(allowed_commands="ls, pwd")


def test_custom_messages():
    custom_messages = {"start": "Custom start message: {allowed_commands}"}
    handler = TeleMessageHandler(custom_messages)
    assert handler.get_message(
        "start", allowed_commands="ls, pwd") == "Custom start message: ls, pwd"
    assert handler.get_message("unauthorized") == DEFAULT_MESSAGES["unauthorized"]
