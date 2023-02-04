from typing import List, Dict


def service(technics: List):
    print('Задача: Сервисный центр')
    technic_dict = get_technic(technics)
    for customer, data in technic_dict.items():
        repairs = ';'.join([f' {name} - {price}' for name, price in data['repairs']])
        print(f'{customer} {data["phone"]}: {repairs}')


def get_technic(technics: List) -> Dict:
    result_dict = {}
    for name, price, customer, phone in technics:
        if customer not in result_dict:
            result_dict[customer] = {'phone': phone, 'repairs': [(name, price)]}
        else:
            result_dict[customer]['repairs'].append((name, price))
    return result_dict

