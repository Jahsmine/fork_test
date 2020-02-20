# [ {'title': 'Аугсбург — Фрайбург', 'time': 'Завтра в 17:30', 'co': ['2.10', '3.60', '3.40']}, {'title': 'Лейпциг — Вердер', 'time': 'Завтра в 17:30', 'co': ['1.27', '6.00', '11.00']}, {'title': 'Падерборн — Герта', 'time': 'Завтра в 17:30', 'co': ['2.85', '3.60', '2.40']}]
# {'title': 'Хоффенхайм — Вольфсбург', 'time': 'Завтра в 17:30', 'co': ['1.70', '6.50', '2.40']}
html_ds_1 = [
    {
        'title': 'Milano - Italy',
        'time': '12.02.2020',
        'data': [
            '1.70',
            '6.50',
            '2.40'
        ]
    }
]

html_ds_2 = [
    {
        'title': 'Milano - Italy',
        'time': '12.02.2020',
        'data': [
            '2.10',
            '3.60',
            '3.00'
        ]
    }
]
# VERSION 1
# fork = []
# for event in html_ds_1:
#     result = []
#     for data_s in event['data']:
#         result.append(data_s)
#     for event_2 in html_ds_2:
#         for data_s_2 in event_2['data']:
#             result.append(data_s_2)
#     if 1 / float(result[0]) + 1 / float(result[5]) < 1 or 1 / float(result[3]) + 1 / float(result[2]) < 1:
#         print('FORK!')
#         fork.append(event['title'])
#     else:
#         pass
#
# print(fork)

# VERSION 2

html_ds_ss = [
    [
        {
            'title': 'Milano - Italy',
            'time': '12.02.2020',
            'data': [
                '1.70',
                '6.50',
                '2.40'
            ]
        },

        {
            'title': 'Milano - Italy',
            'time': '12.02.2020',
            'data': [
                '2.10',
                '3.60',
                '3.00'
            ]
        }
    ],
    [
        {
            'title': 'Milano - Roma',
            'time': '12.02.2020',
            'data': [
                '1.70',
                '6.50',
                '2.40'
            ]
        },

        {
            'title': 'Milano - Roma',
            'time': '12.02.2020',
            'data': [
                '2.10',
                '3.60',
                '3.00'
            ]
        }
    ]
]

# fork_2 = []
# for elem in html_ds_ss:
#     result = []
#     for elem_elem in elem:
#         for data_1 in elem_elem['data']:
#             result.append(data_1)
#     if 1 / float(result[0]) + 1 / float(result[5]) < 1 or 1 / float(result[3]) + 1 / float(result[2]) < 1:
#         print('FORK!')
#         fork_2.append(elem_elem['title'])
#     else:
#         pass
# print(fork_2)


"""
TEST MODULE STARTS HERE!!!!!!!!!!!!
main fucntion 
"""

def check_fork(data):
    fork_2 = []
    for elem in data:
        result = []
        for elem_elem in elem:
            for data_1 in elem_elem['data']:
                result.append(data_1)
        print('Condition 1:')
        print(1 / float(result[0]) + 1 / float(result[5]))
        print('Condition 2:')
        print(1 / float(result[3]) + 1 / float(result[2]))
        if 1 / float(result[0]) + 1 / float(result[5]) < 1 or 1 / float(result[3]) + 1 / float(result[2]) < 1:
            print('FORK!')
            fork_2.append(elem_elem['title'])
        else:
            print('Not Fork!')
    return fork_2


if __name__ == '__main__':
   a = check_fork(html_ds_ss)
   print(a)
