from xmlrpc.client import DateTime
from oma_moodul2 import *
import pickle
import os


ikood=""
ikoodid=[]
arvud=[]
adminpass = 8585

storage_filename1 = "ikoodid"
if not os.path.exists(storage_filename1): 
    with open(storage_filename1, "wb") as f: 
        pickle.dump(ikoodid, f)
else: 
    with open(storage_filename1, "rb") as f:
        ikoodid = pickle.load(f)

storage_filename2 = "arvud"
if not os.path.exists(storage_filename2): 
    with open(storage_filename2, "wb") as f: 
        pickle.dump(arvud, f)
else: 
    with open(storage_filename2, "rb") as f:
        arvud = pickle.load(f)

while True:
    try:
        choice=int(input("1 - vaata arvud \n2 - vaata ikoodid \n3 - isikukood \n4 - sorteeri arvud \n5 - sorteeri ikoodid \n6 - admin panel\n7 - stop programmi\n"))
        if choice == 1:
            print(arvud)
        elif choice == 2:
            print(ikoodid)
        elif choice == 3:
            ikood=input("Sisesta isikukood: ")
            if pikkus(ikood)==False:
                print("Liiga pikk või lühike isikukood")
                arvud.append(ikood)
            else:
                s = esimine (ikood)
                if s=="viga":
                    print("Esimene täht ei ole õige")
                    arvud.append(ikood)
                else:
                    if sunnipaev(ikood)=="viga":
                        print("2-7 tähed on valesti sisestatud")
                        arvud.append(ikood)
                    else:
                        lause(ikood)
                        print(kontrollnr(ikood))
                        ikoodid.append(ikood)
        elif choice == 4:
            arvud = arvud_sorted(arvud)
            print(arvud)
        elif choice == 5:
            ikoodid = naised_mehed(ikoodid)
            print(ikoodid)
        elif choice == 6:
            anspass = int(input("Enter password:"))
            if anspass == adminpass:
                while True:
                    adminchoice = int(input("Menu:\n1 - delete ikood from arvud\n2 - delete ikood from ikoodid\n3 - vaata arvud ja ikoodid\n4 - exit from admin menu\n"))
                    if adminchoice == 1:
                        print(arvud)
                        removechoice = input("Enter ikood to remove:")
                        arvud.remove(removechoice)
                    elif adminchoice == 2:
                        print(ikoodid)
                        removechoice = input("Enter ikood to remove:")
                        ikoodid.remove(removechoice)
                    elif adminchoice == 3:
                        print(ikoodid)
                        print(arvud)
                    elif adminchoice == 4:
                        break
                    else:
                        print("Vale number")
                        ValueError
        elif choice == 7:
            print("Head aega!")
            break
    except ValueError:
        print("Vali õige vastu")

with open(storage_filename1, "wb") as f:
                pickle.dump(ikoodid, f)
with open(storage_filename2, "wb") as f:
                pickle.dump(arvud, f)


