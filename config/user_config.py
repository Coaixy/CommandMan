import configparser
from typing import KeysView

config = configparser.ConfigParser()
config.read('config.ini')


def verify_password(user_name: str, user_pwd: str) -> bool:
    # 从配置文件中获取用户密码
    pwd = config['users'].get(user_name)
    # 为空创建新用户
    if pwd is None:
        return create_new_user(user_name, user_pwd)
    # 验证用户密码
    return pwd == user_pwd


def create_new_user(user_name: str, user_pwd: str) -> bool:
    # 如果用户已存在，返回 False
    if config['users'].get(user_name) is not None:
        return False
    # 创建新用户
    config['users'][user_name] = user_pwd
    config['coins'][user_name] = '0'
    with open('config.ini', 'w', encoding='utf-8') as configfile:  # type: SupportsWrite[str]
        config.write(configfile)
    return True


def get_coins(user_name: str) -> int:
    return int(config['coins'].get(user_name))


def add_coins(user_name: str, coins: int) -> bool:
    current_coins = get_coins(user_name)
    config['coins'][user_name] = str(current_coins + coins)
    with open('config.ini', 'w', encoding='utf-8') as configfile:  # type: SupportsWrite[str]
        config.write(configfile)
    return True

def pay_coins(user_name: str, coins: int) -> bool:
    current_coins = get_coins(user_name)
    if current_coins < coins:
        return False
    config['coins'][user_name] = str(current_coins - coins)
    with open('config.ini', 'w', encoding='utf-8') as configfile:  # type: SupportsWrite[str]
        config.write(configfile)
    return True

def get_all_users() -> KeysView[str]:
    return config['users'].keys()

