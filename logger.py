from datetime import datetime

from core import token_manager


def generate_log_file_name(token: str, command_name: str) -> str:
    """
    Generate log file name
    :param token: token
    :param command_name: command name
    :return: str
    """
    statue, user_name = token_manager.get_user(token)
    if not statue:
        return ''
    time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    return f"{user_name}_{command_name}_{time}.log"
