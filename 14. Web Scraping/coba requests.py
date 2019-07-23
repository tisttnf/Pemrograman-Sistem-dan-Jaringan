import requests
from bs4 import BeautifulSoup
#web crawling process
url = "https://www.detik.com"
con = requests.get(url)
html = con.text

# Extract & transformation process
bs = BeautifulSoup(html, 'html.parser')
titel = bs.title
titel_message = titel.text

# Display mengambil data
print(titel)
print(titel_message)