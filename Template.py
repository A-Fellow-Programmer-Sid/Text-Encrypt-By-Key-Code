print("Credit: A-Fellow-Programmer-Sid")
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# Write The Name Of Your Firebase SDK File In Place Of FB-SDK.json
cred = credentials.Certificate("FB-SDK.json")
import random
firebase_admin.initialize_app(cred, {
    # Paste Your Database URL Here
        'databaseURL': ''
    })
flag = input("Read(r), Write(w) Or New-From-Old(a)_ ")
if flag == "w":
    dat = input("Please Enter Your Text To Save In This Server: ")
    Objlist=["a","b","c","d","e","f","g","h","i","j","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Numlist=["1","2","3","4","5","6","7","8","9"]
# Code For Generating ID (Prebuilt For Upto 48 Alphabets And 16 Numbers, Total 64)
    id1 = Objlist[random.randint(0,25)]
    id2= Numlist[random.randint(0,8)]
    id3 = Objlist[random.randint(0,25)]
    id4 = Objlist[random.randint(0,25)]
    id5 = Objlist[random.randint(0,25)]
    id6= Numlist[random.randint(0,8)]
    id7 = Objlist[random.randint(0,25)]
    id8 = Objlist[random.randint(0,25)]
    id9 = Objlist[random.randint(0,25)]
    id10= Numlist[random.randint(0,8)]
    id11 = Objlist[random.randint(0,25)]
    id12 = Objlist[random.randint(0,25)]
    id13 = Objlist[random.randint(0,25)]
    id14= Numlist[random.randint(0,8)]
    id15 = Objlist[random.randint(0,25)]
    id16 = Objlist[random.randint(0,25)]
    id17 = Objlist[random.randint(0,25)]
    id18= Numlist[random.randint(0,8)]
    id19 = Objlist[random.randint(0,25)]
    id20 = Objlist[random.randint(0,25)]
    id21 = Objlist[random.randint(0,25)]
    id22= Numlist[random.randint(0,8)]
    id23 = Objlist[random.randint(0,25)]
    id24 = Objlist[random.randint(0,25)]
    id25 = Objlist[random.randint(0,25)]
    id26= Numlist[random.randint(0,8)]
    id27 = Objlist[random.randint(0,25)]
    id28 = Objlist[random.randint(0,25)]
    id29 = Objlist[random.randint(0,25)]
    id30= Numlist[random.randint(0,8)]
    id31 = Objlist[random.randint(0,25)]
    id32 = Objlist[random.randint(0,25)]
    id33 = Objlist[random.randint(0,25)]
    id34= Numlist[random.randint(0,8)]
    id35 = Objlist[random.randint(0,25)]
    id36 = Objlist[random.randint(0,25)]
    id37= Objlist[random.randint(0,25)]
    id38= Numlist[random.randint(0,8)]
    id39 = Objlist[random.randint(0,25)]
    id40= Objlist[random.randint(0,25)]
    id41= Objlist[random.randint(0,25)]
    id42= Numlist[random.randint(0,8)]
    id43 = Objlist[random.randint(0,25)]
    id44 = Objlist[random.randint(0,25)]
    id45 = Objlist[random.randint(0,25)]
    id46= Numlist[random.randint(0,8)]
    id47 = Objlist[random.randint(0,25)]
    id48 = Objlist[random.randint(0,25)]
    id49 = Objlist[random.randint(0,25)]
    id50= Numlist[random.randint(0,8)]
    id51 = Objlist[random.randint(0,25)]
    id52 = Objlist[random.randint(0,25)]
    id53 = Objlist[random.randint(0,25)]
    id54= Numlist[random.randint(0,8)]
    id55 = Objlist[random.randint(0,25)]
    id56 = Objlist[random.randint(0,25)]
    id57 = Objlist[random.randint(0,25)]
    id58= Numlist[random.randint(0,8)]
    id59 = Objlist[random.randint(0,25)]
    id60 = Objlist[random.randint(0,25)]
    id61 = Objlist[random.randint(0,25)]
    id62= Numlist[random.randint(0,8)]
    id63 = Objlist[random.randint(0,25)]
    id64 = Objlist[random.randint(0,25)]
    fullid = "key" +id1 + id2 + id3 + id4 + id5 + id6 + id7 + id8 + id9 + id10 +id11 + id12 + id13 + id14 + id15 + id16 + id17 + id18 + id19 + id20 + id21 + id22 + id23 + id24 + id25 + id26 + id27 + id28 + id29 + id30 + id31 + id32 + id33 + id34 + id35 + id36 + id37 + id38 + id39 + id40 + id41 + id42 + id43 + id44 + id45 + id46 + id47 + id48 + id49 + id50 + id51 + id52 + id53 + id54 + id55 + id56 + id57 + id58 + id59 + id60 +id61 + id62 + id63 + id64
    TagToSet = fullid
    String = dat
    ref =db.reference(fullid)
    ref.set({
        TagToSet: String
        })
    f = open("privatekey.key", "w")
    key =f.write(fullid)
    print("Private Key Generated")
elif flag == "r":
    f = open("privatekey.key", "r")
    key =f.read()
    print("NOTE: Keep The Program EXE File In The Same Folder As The Private Key File")
    print("The Key Found Is " + key)
    ref = db.reference(key)
    print(ref.get())
elif flag == "a":
    print("Creating New From Old")
    print("NOTE: Keep The Program EXE File In The Same Folder As The Private Key File")
    Objlist=["a","b","c","d","e","f","g","h","i","j","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Numlist=["1","2","3","4","5","6","7","8","9"]
# Code For Generating ID (Prebuilt For Upto 48 Alphabets And 16 Numbers, Total 64)
    id1 = Objlist[random.randint(0,25)]
    id2= Numlist[random.randint(0,8)]
    id3 = Objlist[random.randint(0,25)]
    id4 = Objlist[random.randint(0,25)]
    id5 = Objlist[random.randint(0,25)]
    id6= Numlist[random.randint(0,8)]
    id7 = Objlist[random.randint(0,25)]
    id8 = Objlist[random.randint(0,25)]
    id9 = Objlist[random.randint(0,25)]
    id10= Numlist[random.randint(0,8)]
    id11 = Objlist[random.randint(0,25)]
    id12 = Objlist[random.randint(0,25)]
    id13 = Objlist[random.randint(0,25)]
    id14= Numlist[random.randint(0,8)]
    id15 = Objlist[random.randint(0,25)]
    id16 = Objlist[random.randint(0,25)]
    id17 = Objlist[random.randint(0,25)]
    id18= Numlist[random.randint(0,8)]
    id19 = Objlist[random.randint(0,25)]
    id20 = Objlist[random.randint(0,25)]
    id21 = Objlist[random.randint(0,25)]
    id22= Numlist[random.randint(0,8)]
    id23 = Objlist[random.randint(0,25)]
    id24 = Objlist[random.randint(0,25)]
    id25 = Objlist[random.randint(0,25)]
    id26= Numlist[random.randint(0,8)]
    id27 = Objlist[random.randint(0,25)]
    id28 = Objlist[random.randint(0,25)]
    id29 = Objlist[random.randint(0,25)]
    id30= Numlist[random.randint(0,8)]
    id31 = Objlist[random.randint(0,25)]
    id32 = Objlist[random.randint(0,25)]
    id33 = Objlist[random.randint(0,25)]
    id34= Numlist[random.randint(0,8)]
    id35 = Objlist[random.randint(0,25)]
    id36 = Objlist[random.randint(0,25)]
    id37= Objlist[random.randint(0,25)]
    id38= Numlist[random.randint(0,8)]
    id39 = Objlist[random.randint(0,25)]
    id40= Objlist[random.randint(0,25)]
    id41= Objlist[random.randint(0,25)]
    id42= Numlist[random.randint(0,8)]
    id43 = Objlist[random.randint(0,25)]
    id44 = Objlist[random.randint(0,25)]
    id45 = Objlist[random.randint(0,25)]
    id46= Numlist[random.randint(0,8)]
    id47 = Objlist[random.randint(0,25)]
    id48 = Objlist[random.randint(0,25)]
    id49 = Objlist[random.randint(0,25)]
    id50= Numlist[random.randint(0,8)]
    id51 = Objlist[random.randint(0,25)]
    id52 = Objlist[random.randint(0,25)]
    id53 = Objlist[random.randint(0,25)]
    id54= Numlist[random.randint(0,8)]
    id55 = Objlist[random.randint(0,25)]
    id56 = Objlist[random.randint(0,25)]
    id57 = Objlist[random.randint(0,25)]
    id58= Numlist[random.randint(0,8)]
    id59 = Objlist[random.randint(0,25)]
    id60 = Objlist[random.randint(0,25)]
    id61 = Objlist[random.randint(0,25)]
    id62= Numlist[random.randint(0,8)]
    id63 = Objlist[random.randint(0,25)]
    id64 = Objlist[random.randint(0,25)]
    fullid = "ID" +id1 + id2 + id3 + id4 + id5 + id6 + id7 + id8 + id9 + id10 +id11 + id12 + id13 + id14 + id15 + id16 + id17 + id18 + id19 + id20 + id21 + id22 + id23 + id24 + id25 + id26 + id27 + id28 + id29 + id30 + id31 + id32 + id33 + id34 + id35 + id36 + id37 + id38 + id39 + id40 + id41 + id42 + id43 + id44 + id45 + id46 + id47 + id48 + id49 + id50 + id51 + id52 + id53 + id54 + id55 + id56 + id57 + id58 + id59 + id60 +id61 + id62 + id63 + id64
    TagToSet = fullid
    f = open("privatekey.key", "r")
    key =f.read()
    ref = db.reference(key)
    oldDAT =ref.get()
    print("Old Key: " + key)
    print("New Key: " + TagToSet)
    ref =db.reference(fullid)
    ref.set({
        TagToSet: oldDAT
        })
    f = open("privatekey.key", "w")
    key =f.write(fullid)