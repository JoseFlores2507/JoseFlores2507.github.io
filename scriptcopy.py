from typing import List
from bs4 import BeautifulSoup
import requests


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

url = "https://www.naturalista.mx"


links=[]


for i in range(1,19):#19
    soup = get_soup(f"https://www.naturalista.mx/lists/83947-Flora-del-Valle-de-M-xico-Lista-de-Comprobaci-n?page={i}&q=&rank=leaves&taxonomic_status=all")
    
    
  

    for detail in soup.find_all("div",{"class":"column details"}):
        

        link=detail.find_all("a")[0]["href"]
        links.append(url+link)
        print(url+link)

        
print(len(links))
gallery=[]
gallerytitles=[]
for i in range(len(links)):
    
    print(links[i])
    soup = get_soup(links[i]+"/browse_photos")
    #print(soup)
    splits = str(soup).split('"medium_url":')
    images=[]
    for split in splits:
        images.append(split.split('"',2)[1])

    splits = str(soup).split('"attribution":')
    titles=[]
    for split in splits:
        titles.append(split.split('"',2)[1])

    gallerytitles.append(titles[1:-1])
    gallery.append(images[1:-1])
    #print(len(images[1:-1]))
    #print(str(images[1:-1]))
    #print(len(titles[1:-1]))

print(len(gallery))
print(len(gallerytitles))

with open("gallery.txt", "w", encoding="utf-8") as file: 
    file.write(str(gallery))

with open("gallerytitles.txt", "w",  encoding="utf-8") as file: 
    file.write(str(gallerytitles))






    

