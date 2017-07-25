import requests
from bs4 import BeautifulSoup

#Set up URL to send request and get response from
url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content


soup = BeautifulSoup(html)
#Find our table body elements
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows = []
#Find table rows in table, then table data tags and structure them
for row in table.findAll('tr'):
	list_of_cells = []
	for cell in row.findAll('td'):
		text = cell.text.replace('&nbsp;','')
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)

print list_of_rows
