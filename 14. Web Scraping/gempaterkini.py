import requests
from bs4 import BeautifulSoup

fileout = "gempa-terkini2.csv"
delimiter = ";"

#web crawling process
url = "http://www.bmkg.go.id/gempabumi/gempabumi-terkini.bmkg"
con = requests.get(url)
html = con.text

#extract & transformation process
bs = BeautifulSoup(html,'html.parser')
data = bs.find('table')

fp = open(fileout,"w")
row_header = data.find('tr')
strdata = ""
i = 0
for th in row_header.find_all('th'):
	if i != 0:	
		strdata = strdata + delimiter + th.text
	else:
		strdata = strdata + th.text
	i = i + 1

fp.write(strdata + "\n")

for rec in data.find_all('tr'):
	i = 0
	strdata = ""
	for td in rec.find_all('td'):
		if i != 0:	
			strdata = strdata + delimiter + td.text
		else:
			strdata = strdata + td.text
		i = i + 1
	fp.write(strdata + "\n")

fp.close()







