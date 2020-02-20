common_data = [
    # EVENT 1
    [
        {
            'title': 'Хоффенхайм — Вольфсбург',
            'time': '12.02.2020',
            'data': [
                '1.70',
                '6.50',
                '2.40'
            ]
        },

        {
            'title': 'Хоффенхайм — Вольфсбург',
            'time': '12.02.2020',
            'data': [
                '2.10',
                '3.60',
                '3.00'
            ]
        }
    ],
    # EVENT 2
    [
        {
            'title': 'Аугсбург — Фрайбург',
            'time': '12.02.2020',
            'data': [
                '2.10',
                '3.60',
                '3.40'
            ]
        },

        {
            'title': 'Аугсбург — Фрайбург',
            'time': '12.02.2020',
            'data': [
                '2.10',
                '3.60',
                '3.40'
            ]
        }
    ],
    # EVENT 3
    [
        {
            'title': 'Лейпциг — Вердер',
            'time': '12.02.2020',
            'data': [
                '1.27',
                '6.00',
                '11.00'
            ]
        },

        {
            'title': 'Лейпциг — Вердер',
            'time': '12.02.2020',
            'data': [
                '1.27',
                '6.00',
                '11.00'
            ]
        }
    ],
    # EVENT 4
    [
        {
            'title': 'Падерборн — Герта',
            'time': '12.02.2020',
            'data': [
                '2.85',
                '3.60',
                '2.40'
            ]
        },

        {
            'title': 'Падерборн — Герта',
            'time': '12.02.2020',
            'data': [
                '2.85',
                '3.60',
                '2.40'
            ]
        }
    ]
]


def fork_detection(data):
    fork_result = []
    for elem in data:
        elem_items = []
        for elem_elem in elem:
            for item in elem_elem['data']:
                elem_items.append(item)
        print('Condition 1:')
        print(1 / float(elem_items[0]) + 1 / float(elem_items[5]))
        print('Condition 2:')
        print(1 / float(elem_items[3]) + 1 / float(elem_items[2]))
        if 1 / float(elem_items[0]) + 1 / float(elem_items[5]) < 1 or 1 / float(elem_items[3]) + 1 / float(elem_items[2]) < 1:
            print('FORK!')
            fork_result.append(elem_elem['title'])
        else:
            print('Not Fork!')
    return fork_result


if __name__ == '__main__':
    print(fork_detection(common_data))
