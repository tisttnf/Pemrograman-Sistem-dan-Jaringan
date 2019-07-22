import requests
from bs4 import BeautifulSoup

# Buat object Session HTTP
s = requests.Session()

# Tentukan URL Login
url = "https://elen.nurulfikri.ac.id/login/index.php"

# Tentukan payload (data) untuk login
data_ = {
    'username' : 'muha033ti',
    'password' : '0110217029',
    'submit' : 'Log in'
    }

# Lakukan post / login
resp = s.post(url, data = data_)

# Proses / supply page kedalam beautifulsoup untuk scraping
bs = BeautifulSoup(resp.text, 'html.parser')

loginAs = bs.find('span', {'class' : 'usertext'})
print(f'Anda login sbg : {loginAs.text}')
print('-----------------------------------')

print("Online User in Elen NF")
print("----------------------")
no = 1
for line in bs.find_all("div", {"class" : "user"}) :
    for user in line.find_all('a') :
        print(f"{no}, {user.text}")
        no = no + 1
