import requests
from bs4 import BeautifulSoup

username = "engineerapex"
URL = "https://www.instagram.com/engineerapex/"

r = requests.get(URL.format(username))
s = BeautifulSoup(r.text,"html.parser")
u = s.find("meta",property = "og:image")
url = u.attrs['content']

with open(username+ '.jpg',"wb") as pic:
    binary = requests.get("https://www.instagram.com/engineerapex/").content
    pic.write(binary)