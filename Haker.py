import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint


URL= 'https://news.ycombinator.com/'

#CSV='https://news.ycombinator.com.csv'
#HOST='https://news.ycombinator.com'

# #HEADERS={
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
# }

def get_html(URL):
    r = requests.get(URL)
    return r.content

def get_content(html):
    soup=BeautifulSoup(html,'html.parser')
    items=soup.findAll('tr', class_='athing')
    haker=[]
    for item in items:
        haker.append({
            'Title':  item.find('span', class_='titleline').get_text(),
            'Link':item.find('span', class_='titleline').find('a').get('href'),
             'Point': soup.find('span',class_='score').get_text(),
             'Hour': soup.find('span', class_='age').get_text(),
            'Comments':str(soup.find('span', class_='subline').get_text().split()[-2:]),
            'Comments link':'https://news.ycombinator.com/'+ soup.find('span', class_='age').find('a').get('href'),
        })
    return haker

def save(data):
    with open('data.json', 'w') as file:
        json.dump(data, file,indent=2)
        pprint(data)
save(get_content(get_html(URL)))
