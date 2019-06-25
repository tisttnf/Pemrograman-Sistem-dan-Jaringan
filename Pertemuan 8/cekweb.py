# sudo apt-get install python-pip
# sudo pip install requests
# python3 -m pip install requests
# python3.7 -m pip install requests

# Menggunakan python interactive

# import request
# dir(requests)
# url = "http://www.kompas.com"
# con = requests.get(url)
# con.status_code
# con.text
# con.headers

import requests

# url = "http://localhost"
# url = "http://www.nurulfikri.ac.id"
# url = "http://www.nurulfikris.ac.id"

fname = "web.txt"
fd = open(fname)

for url in fd.readlines() :
    try :        
        url = url.strip()
        requests.get(url)
        print("web server of %s is Running" %(url))
    except :
        print("web server of %s is Stopped" %(url))