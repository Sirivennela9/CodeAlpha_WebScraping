import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://books.toscrape.com/catalogue/page-1.html"

def scrape_books():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = []
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        rating = book.find('p', class_='star-rating')['class'][1]
        availability = book.find('p', class_='instock availability').text.strip()
        books.append({'Title': title, 'Price': price, 'Rating': rating, 'Availability': availability})
    df = pd.DataFrame(book)
    df.to_csv('books.csv', index=False, encoding='utf-8-sig')
    print(df.head())

scrape_books()
