import hashlib
import time
# 登录 token 的 SALT
LOGIN_HASH = "CommandMan"

"""
    登录 token 映射表
    key: 用户名
    value: {
        'create_time': 创建时间
        'token': token
    }
"""
LOGIN_TOKEN_MAP = {
    'admin': {
        'create_time': 0,
        'token': ''
    },
}


def create_token(username: str) -> tuple[bool, str]:
    """
        创建一个 token
        :param username: 用户名
        :return: tuple[bool, str]
            bool: 是否创建成功
            str: token
    """
    md5 = hashlib.md5()
    md5.update(f"{username}{LOGIN_HASH}{time.time()}".encode())
    token = md5.hexdigest()
    if LOGIN_TOKEN_MAP.get(username) is not None:
        latest_time = LOGIN_TOKEN_MAP[username]['create_time']
        if time.time() - latest_time > 60 * 60 * 24:
            LOGIN_TOKEN_MAP[username]['create_time'] = time.time()
            LOGIN_TOKEN_MAP[username]['token'] = token
            return True, token
        else:
            return True, LOGIN_TOKEN_MAP[username]['token']
    else:
        LOGIN_TOKEN_MAP[username] = {
            'create_time': time.time(),
            'token': token
        }
        return True, token

