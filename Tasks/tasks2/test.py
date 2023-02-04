from typing import List


def double_char(name_file: str) -> str:
    new_name = ''
    for ch in name_file:
        if ch not in new_name:
            new_name += ch
    return new_name


def file_name(name_list: List[str]):
    name_list = [double_char(name) for name in name_list]
    max_len = max([len(x) for x in name_list])
    result_list = [x.ljust(max_len, '_') for x in name_list]
    print('Задача: Имя файла')
    print(result_list)
