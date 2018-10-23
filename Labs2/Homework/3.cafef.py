from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url ="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

webpage_text = urlopen(url).read().decode("utf-8")

#save html to local file
# f = open("scafef.html","wb")
# f.write(webpage_text)
# f.close

soup = BeautifulSoup(webpage_text,"html.parser")

table = soup.find("table",id = "tableContent")

datas = []

trs = table.find_all("tr")

for tr in trs:
    tds = tr.find_all('td')
    data = {}
       
    if tds != [] and tds[0].string is not None :
        data["title"]=(tds[0].string.strip())
        data["2017"]=(tds[1].string)
        data["2016"]=(tds[2].string)
        data["2015"]=(tds[3].string)
        data["2014"]=(tds[4].string)
    
    if data:
        datas.append(data)

    print(datas)

pyexcel.save_as(records=datas,dest_file_name="scafef.xlsx")

# print(table.prettify())

