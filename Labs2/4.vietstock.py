from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://finance.vietstock.vn/VNM/tai-chinh.htm"

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text,"htm.parser")
ul = soup.find("ul","BR_modTable")
print(ul)


