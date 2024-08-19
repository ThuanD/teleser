import re

DEFAULT_DANGEROUS_PATTERNS = [
    r"rm\s+-rf",  # Remove recursively and force
    r"mkfs",  # Make file system
    r"dd",  # Disk Destroyer
    r">|<",  # Redirection
    r"\|",  # Pipes
    r"&",  # Background execution
    r";",  # Command chaining
    r"`",  # Command substitution
    r"\$\(",  # Command substitution
    r"sudo",  # Superuser do
    r"su\s+",  # Switch user
    r"chmod",  # Change mode
    r"chown",  # Change owner
    r"passwd",  # Change password
    r"useradd",  # Add user
    r"usermod",  # Modify user
    r"groupadd",  # Add group
    r"groupmod",  # Modify group
]

DEFAULT_ALLOWED_COMMANDS = [
    "ls", "pwd", "echo", "cat", "date", "whoami", "uname", "hostname", "cd",
]


class CommandValidator:
    def __init__(self, dangerous_patterns=None, allowed_commands=None):
        self.dangerous_patterns = dangerous_patterns or DEFAULT_DANGEROUS_PATTERNS
        self.allowed_commands = allowed_commands or DEFAULT_ALLOWED_COMMANDS

    def is_command_safe(self, command: str) -> bool:
        # Check if the command is in the allowed list
        if not any(command.startswith(cmd) for cmd in self.allowed_commands):
            return False

        # Check for dangerous patterns
        for pattern in self.dangerous_patterns:
            if re.search(pattern, command):
                return False

        return True
