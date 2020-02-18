from bs4 import BeautifulSoup

line_1 = []

with open('index.html', 'r') as f:
    content = f.read()

    soup = BeautifulSoup(content, 'lxml')
    tables_bet = soup.find('div', class_='bets-table').find_all('div', class_='single-bet')

    for bet in tables_bet:
        try:
            title = bet.find('div', class_='bet-title').find('h3').text
        except AttributeError:
            pass
        try:
            time = bet.find('div', class_='bet-time').find('h3').text
        except AttributeError:
            pass
        try:
            bet_data = bet.find('div',  class_='bet-data').find_all('div')
            total = []
            for data in bet_data:
                coff = data.find('h4').text
                total.append(coff)
        except AttributeError:
            pass

        data = {
            'title': title,
            'time': time,
            'co': total,
        }

        line_1.append(data)

print(line_1)

for lino in line_1:
    if 'Завтра в 17:33' in lino['time']:
        print('ok')
        break
    else:
        print('no')
