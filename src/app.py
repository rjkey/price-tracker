import requests
from bs4 import BeautifulSoup
import re
import sqlite3

conn = sqlite3.connect('database_name.db')

cursor = conn.cursor()

# Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS prices")

# Creating table as per requirement
sql ='''CREATE TABLE prices(
    priceId INTEGER PRIMARY KEY, 
    price FLOAT
)'''
cursor.execute(sql)
print("Table created successfully........")

# Commit your changes in the database
conn.commit()


def do_job(product_id):

    url = f'https://www.komplett.no/product/{product_id}'

    headers = {'User-Agent': 'PostmanRuntime/7.32.2'}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    element = soup.find(class_='product-price-now')

    if element is None:
        return

    result = re.sub('\D', '', element.text)

    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO prices (priceId, price) VALUES (?, ?)", (product_id, float(result)))

    conn.commit()

for num in range(1200000, 1300000):
    do_job(num)

