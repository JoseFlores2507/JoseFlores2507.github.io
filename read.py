
import pyrebase

config = {
  "apiKey": "AIzaSyC9Xo9zpXopjKxNsYijBWQQrYud5sQMhWw",
  "authDomain": "naturalista-5dd33.firebaseapp.com",
  "databaseURL": "https://naturalista-5dd33-default-rtdb.firebaseio.com/",
  "storageBucket": "naturalista-5dd33.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

string = open("gallery.txt", "r").read()
listcode = "gallery = "+ string
exec(listcode)

print(len(gallery))


string = open("gallerytitles.txt", "r",encoding="utf-8").read()
listcode = "gallerytitles = "+ string
exec(listcode)

print(len(gallerytitles))

for i in range(len(gallery)):
    for j in range(len(gallery[i])):
        json = {
            "image":gallery[i][j],
            "title":gallerytitles[i][j]
            }
        
        results = db.child("gallery").child(i).child(j).set(json)
        print(f"i:{i} j:{j} ")

'''
for j in range(len(gallery[1])):
    json = {
        "image":gallery[1][j],
        "title":gallerytitles[1][j]
        }
        
    results = db.child("gallery").child(1).child(j).set(json)
    print(f"i:{1} j:{j} ")
    '''