import pprint

my_dict = {
    'ключ1': 'значение1',
    'ключ2': 'значение2',
    'ключ3': 'значение3',
    'ключ4': 'значение4',
    'ключ5': 'значение5',
    'ключ6': 'значение6',
    'ключ7': 'значение7',
    'ключ8': 'значение8',
    'ключ9': 'значение9',
    'ключ10': 'значение10'
}

pp = pprint.PrettyPrinter(sort_dicts=False)

pp.pprint(my_dict)