import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def get_commands_map():
    commands = {}
    for section in config['commands']:
        commands[section] = config['commands'][section]
    return commands


def get_command_by_name(name):
    # 从命令映射中获取命令字符串
    command = get_commands_map().get(name)
    if command is None:
        return None

    # 初始化左括号和右括号的位置列表
    left_position = []
    right_position = []

    # 遍历命令字符串，记录每个左括号和右括号的位置
    for i in range(len(command)):
        char = command[i]
        if char == '[':
            left_position.append(i)
        if char == ']':
            right_position.append(i)

    # 如果左括号和右括号的数量不一致，返回 None
    if len(left_position) != len(right_position):
        return None

    # 返回命令字符串、左括号位置列表和右括号位置列表
    return command, left_position, right_position


def parse_command(command_name, args: list[str]):
    command_str, left_position, right_position = get_command_by_name(command_name)

    print(command_str, left_position, right_position)

    if command_str is None:
        return None

    # 确保传入的 args 长度与位置列表长度一致
    if len(args) != len(left_position) or len(args) != len(right_position):
        return None

    # 从右往左替换，防止索引被替换影响
    for i in range(len(left_position) - 1, -1, -1):
        start = left_position[i]
        end = right_position[i]

        # 确保索引范围有效
        if start < 0 or end >= len(command_str) or start > end:
            return None

        # 替换占位符部分为 args 对应的值
        command_str = command_str[:start] + args[i] + command_str[end + 1:]

    return command_str

