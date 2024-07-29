import requests
from bs4 import BeautifulSoup

full_name = input("Enter full name(ex. John Doe)")

r=requests.get(full_name)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())