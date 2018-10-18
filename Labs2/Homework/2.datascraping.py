fromfrom urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url ="https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text,"html.parser")
section = soup.find("section","section chart-grid")
ul_list = section.find_all("ul")
print(ul_list)

song_list = []

for ul in ul_list:
    ah3 = ul.h3.a
    ah4 = ul.h4.a
    title = ah3.string
    artist = ah4.string
    link = url + ah3["href"]
    song = { 
        "Link": link,
        "Title": title,
        'Artist': artist,
    }
    song_list.append(song)

    print("*"*10)

print(*ul_list,sep="\n * * * * *\n")

# pyexcel.save_as(records=song_list,dest_file_name="itune_songs.xlsx")
