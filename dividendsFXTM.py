import requests
from bs4 import BeautifulSoup

# Получаем список всех CFD
url = 'https://www.forextime.com/ru/forex-trading/contract-specifications'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

cfd_list = []
for item in soup.find_all('div', {'id': 'tab-cfd-us-shares'}):
	for link in item.find_all('a'):
		if link.text.strip('#') not in cfd_list:
			cfd_list.append(link.text.strip('#'))


dividend_date = input('Example(2017-Mar-29) ')
url2 = 'http://www.nasdaq.com/dividend-stocks/dividend-calendar.aspx?date={}'.format(dividend_date)

r2 = requests.get(url2)
soup2 = BeautifulSoup(r2.text, 'html.parser')

# Получаем список компаний выплачивающих дивиденд на заданное время
comp_names = []
for comp_name in soup2.find_all('tbody')[1].find_all('a'):
	comp_name = comp_name.text.split('\xa0')[-1]
	comp_name = comp_name.strip('(, )')
	comp_names.append(comp_name)


# Дивиденды на каждую компанию
lst = []
for i in soup2.find_all('tbody')[1].find_all('td'):
	lst.append(i.text)

dvdnd = []
for j in lst[2::7]:
	dvdnd.append(j)

# Результат
for comp, dvd in zip(comp_names, dvdnd):
	if comp in cfd_list:
		print(comp, dvd)