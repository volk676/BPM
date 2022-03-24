from bs4 import BeautifulSoup
import urllib.request

artist = "Nine Inch Nails"
song = "Closer"

split_artist = artist.split()
split_song = song.split()

artist = ""
song = ""

for a in split_artist:
    artist += a + "+"
    
for s in split_song:
    song = s + "+"

artist = artist[0:len(artist) - 1]
song = song[0:len(song) - 1]

req = urllib.request.Request("https://www.bpmdatabase.com/music/search/?artist=" + artist + "&title=" + song + "&bpm=&genre=", headers={"User-Agent" : "Mozilla/5.0"})
response = urllib.request.urlopen(req)
html = response.read()

soup = BeautifulSoup(html, "html.parser")
tr_find = soup.find_all("tr")

for tr in tr_find:
    for td in tr.find_all("td"):
        if td.has_attr("class"):
            if td["class"][0] == "artist":
                print("Artist: " + td.string)
            if td["class"][0] == "title":
                print("Title: " + td.string)
            if td["class"][0] == "bpm":
                print("BPM: " + td.string)
    print() 