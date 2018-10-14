#1. Download web
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel


url = "https://dantri.com.vn"
 
#1.1 Connect to web
conn = urlopen(url)

#1.2 Download raw data
raw_data = conn.read()

#1.3 Decode data
webpage_text = raw_data.decode("utf-8")
# print(len(webpage_text))

# #1.4 Save text file
# f = open("dantri.html","wb")
# f.write(raw_data)
# f.close()

#2. Extract ROI
#2.1 Convert text to soup
soup = BeautifulSoup(webpage_text,"html.parser")
ul = soup.find("ul","ul1 ulnew") #id="ul1 ulnew"

li_list = ul.find_all("li")
news_list = []

for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a["href"]

    # print(title)
    # print(link)
    news = { 
        "Title": title,
        "Link": link,
    }
    news_list.append(news)
    print("*"*10)

print(*news_list,sep="\n * * * * *\n")

# for li in li_list:
#     print(li.prettify())
#     print("* * * * * * * * ")
# print(soup.prettify())

#3. Extract data


#4. Save data
pyexcel.save_as(records=news_list,dest_file_name="dantri.xlsx")

