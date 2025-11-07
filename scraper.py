import requests
from bs4 import BeautifulSoup
import csv

website = "https://books.toscrape.com/catalogue/page-{}.html"
books = []

for page in range(1, 51):
    print(f"Scraping page {page}...")
    url = website.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        books.append([title, price])

with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Price'])
    writer.writerows(books)

print(f"Scraping completed.")
