
import shlex


def parse_command(command_line):
    """Разделяет командную строку на команду и аргументы."""
    return shlex.split(command_line)
