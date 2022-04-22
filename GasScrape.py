import requests
from bs4 import BeautifulSoup

URL = 'https://www.gasbuddy.com/gasprices/ohio/toledo'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
price = soup.find_all('div', class_ = 'grid__grid___1bWao grid__gridContainer___nyUt1')
while(True):
    for event in price:
        event_name = event.find_all('h3')
        event_list = event.find('a')
        event_div = event.find('div')
        print(event_name.text)
        continue
#Gas_Station_Name = price.find('h3', class_ = 'header__header3___1b1oq header__header___1zII0 header__midnight___1tdCQ header__snug___lRSNK StationDisplay-module__stationNameHeader___1A2q8')
#print(Gas_Station_Name)
