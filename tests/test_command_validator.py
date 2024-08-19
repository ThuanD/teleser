from teleser.validator import CommandValidator


def test_is_command_safe():
    validator = CommandValidator()
    assert validator.is_command_safe("ls")
    # test command not in allowed command
    assert not validator.is_command_safe("rm -rf /")
    # test command in dangerous patterns
    assert not validator.is_command_safe("ls && ls")


def test_custom_patterns():
    validator = CommandValidator(dangerous_patterns=[r"custom_dangerous"])
    assert not validator.is_command_safe("custom_dangerous command")


def test_custom_allowed_commands():
    validator = CommandValidator(allowed_commands=["custom_command"])
    assert validator.is_command_safe("custom_command")
    assert not validator.is_command_safe("ls")
