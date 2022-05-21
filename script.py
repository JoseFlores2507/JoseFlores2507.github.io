from typing import List
from bs4 import BeautifulSoup
import requests


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

url = "https://www.naturalista.mx"

images=[]
titles=[]
names=[]
scinames=[]
links=[]


for i in range(1,19):
    soup = get_soup(f"https://www.naturalista.mx/lists/83947-Flora-del-Valle-de-M-xico-Lista-de-Comprobaci-n?page={i}&q=&rank=leaves&taxonomic_status=all")
    
    for img in soup.find_all("img",{"class": "image"}):
        if "medium" in img["src"]:
            images.append(img["src"])
            titles.append(img["title"])
            #print(img["title"])
            if img["src"]=="https://inaturalist-open-data.s3.amazonaws.com/photos/30820549/medium.jpeg":
                images.append("None")
                titles.append("None")
                #print("None")
       
  

    for detail in soup.find_all("div",{"class":"column details"}):
        sciname=detail.find_all("span",{"class":"sciname"})
        scinames.append(sciname[0].text)

        link=detail.find_all("a")[0]["href"]
        links.append(url+link)
       #print(url+link)

        name=detail.find_all("span",{"class":"comname"})
        if name:
            names.append(name[0].text.strip())
            print(name[0].text.strip())
        else:
            names.append(sciname[0].text)
            print(sciname[0].text)


print(len(images))
print(len(titles))
print(len(names))
print(len(scinames))
print(len(links))


with open("images.txt", "w") as file:
    lines = "\n".join(images)
    file.write(lines)

with open("names.txt", "w") as file:
    lines = "\n".join(names)
    file.write(lines)

with open("scinames.txt", "w") as file:
    lines = "\n".join(scinames)
    file.write(lines)
with open("links.txt", "w") as file:
    lines = "\n".join(links)
    file.write(lines)

with open("titles.txt", "w", encoding="utf-8") as file:
    lines = "\n".join(titles)
    file.write(lines)




#elements = soup.find_all('ul')[5].find_all('li')




    

