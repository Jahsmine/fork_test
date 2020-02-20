from bs4 import BeautifulSoup
import mymodule

line_1 = []
line_2 = []

# files = ['index.html', 'index_2.html']
# read similar html files and put each data to each array
# SOURCE 1
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
            'data': total,
        }

        line_1.append(data)
# SOURCE 2
with open('index_2.html', 'r') as f:
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
            'data': total,  
        }

        line_2.append(data)

# FIXME: !!!!!!!!!!!!!!!!!!!!!!!!
# filter arrays to set common events
result = []
i = 0
for element in line_1:
    if element['title'] == line_2[:][i]['title']:
        event = []
        event.append(element)
        event.append(line_2[:][i])
        result.append(event)
    i = i + 1
print(result)

a = mymodule.check_fork(result)
print(a)