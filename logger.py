from datetime import datetime

from config import login_token


def generate_log_file_name(token: str, command_name: str) -> str:
    """
    Generate log file name
    :param token: token
    :param command_name: command name
    :return: str
    """
    statue, user_name = login_token.get_user(token)
    if not statue:
        return ''
    time = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    return f"{user_name}_{command_name}_{time}.log"
