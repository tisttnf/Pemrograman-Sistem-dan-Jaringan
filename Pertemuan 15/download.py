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

# Url PSJ
url = "https://elen.nurulfikri.ac.id/course/view.php?id=728"
psj = s.get(url)
bs = BeautifulSoup(psj.text, 'html.parser')

for activity in bs.find_all('div', {'class':'activityinstance'}):
    # URL File PDF
    a = activity.find('a')
    # Nama File
    n = activity.find('span',{'class':'instancename'})

    # pola tipe PDF File
    img = activity.find('img')
    imgurl = img.get('src')
    if imgurl.find('pdf') > -1:
        fname =  n.text.replace(" ","_")
        fname =  fname.replace("/","_")
        f = fname + ".pdf"
        # Mulai Download file 
        getpdf = s.get(a.get('href'))
        # Simpan File ke lokal disk
        fd = open(f,'wb')
        fd.write(getpdf.content)