technic = [('Ноутбук', 1500, 'Татьяна', '89002001020'),
           ('Смартфон', 500, 'Анна', '89202202325'),
           ('Проектор', 300, 'Андрей', '89505205656'),
           ('Принтер', 750, 'Игорь', '89303303236'),
           ('Планшет', 2300, 'Игорь', '89303303236'),
           ('Смартфон', 1000, 'Андрей', '89505205656'),
           ('Ноутбук', 4800, 'Татьяна', '89002001020'),
           ('Наушники', 780, 'Марина', '89562002350'),
           ('Сканер', 550, 'Сергей', '89808564559'),
           ('Планшет', 1200, 'Анна', '89202202325'),
           ('Ноутбук', 1100, 'Игорь', '89303303236'),
           ('Смартфон', 3500, 'Татьяна', '89002001020')]


def service():
    technic_dict = get_technic()
    for customer, data in technic_dict.items():
        repairs = ';'.join([f'{name}-{price}' for name, price in data['repairs']])
        print(f'{customer} {data["phone"]}: {repairs}')


def get_technic():
    result_dict = {}
    for name, price, customer, phone in technic:
        if customer not in result_dict:
            result_dict[customer] = {'phone': phone, 'repairs': [(name, price)]}
        else:
            result_dict[customer]['repairs'].append((name, price))
    return result_dict

