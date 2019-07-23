import requests
from bs4 import BeautifulSoup

# Web crawling process
url = "http://www.bmkg.go.id/gempabumi/gempabumi-terkini.bmkg"
con = requests.get(url)
html = con.text

#extract & transformation process
bs = BeautifulSoup(html,'html.parser')
data = bs.find('table')

print(data)
