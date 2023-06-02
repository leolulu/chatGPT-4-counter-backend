import os


def get_env_var(name, defualt_value=None):
    value = os.environ.get(name)
    if value:
        return value
    elif defualt_value:
        return defualt_value
    else:
        raise UserWarning(f"找不到环境变量：{name}")
