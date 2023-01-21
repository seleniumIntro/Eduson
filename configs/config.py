from typing import Any


def safe_dict_value_getter(d: dict, keys: list[str]) -> Any:
    value = d.get(keys[0], {})
    for key in keys[1:]:
        value = value.get(key, {})

    return value if value != {} else None


class GlobalConfig:
    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        assert attr is not None, \
            f'There was an attempt to use parameter "{name}" when it was not initialized in the json config file.' \
            f'\nPath to the config file: {self.cfg_path}.'
        return attr

    def __init__(self, data: any):
        self.base_url: str = safe_dict_value_getter(data, ['urls', 'store'])
        self.cart_url: str = safe_dict_value_getter(data, ['urls', 'cart'])
        self.login: str = safe_dict_value_getter(data, ['user', 'login'])
        self.password: str = safe_dict_value_getter(data, ['user', 'password'])
        self.goods_0: str = safe_dict_value_getter(data, ['goods', 'url_goods_0'])
        self.goods_1: str = safe_dict_value_getter(data, ['goods', 'url_goods_1'])