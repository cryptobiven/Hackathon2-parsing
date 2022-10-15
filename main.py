
import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html,'lxml')
    return soup

def get_data(soup):
    catalog = soup.find('div', class_="list-view")
    phones =catalog.find_all('div', class_='item product_listbox oh')
    
    for phone in phones:
        title = phone.find('div', class_='listbox_title oh').text.strip()
        image = 'kivano.kg' + phone.find('div', class_='listbox_img').find('a').find('img').get('src')

        price = phone.find('div', class_='listbox_price text-center').text.strip()

        write_csv({
            'title': title,
            'image': image,
            'price': price
        })

def write_csv(data):
    with open('phones.csv', 'a') as file:
        names = ['title', 'price', 'image']
        write = csv.DictWriter(file, delimiter=' ', fieldnames=names)
        write.writerow(data)

def main():
    BASE_URL = 'https://www.kivano.kg/mobilnye-telefony'
    html = get_html(BASE_URL)
    soup = get_soup(html)
    get_data(soup)

if __name__ == '__main__':
    main()