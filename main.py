import requests
from bs4 import BeautifulSoup

def get_stock_name():
    stock_name = input("Enter Stock to find : ")
    return stock_name

def search_stock():
    base_url = "https://www.google.com/search?safe=strict&q=bank+of+india+stock&oq=bank+of+india+stock&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEYQ-https://www.google.com/search?safe=strict&q=bank+of+india+stock"
    stock_name = get_stock_name()
    stock_url = base_url + stock_name
    res = requests.get(stock_url)
    return res

page = search_stock()
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title
page_title = soup.title.text

status = page.status_code

print(page_title)
print(status)