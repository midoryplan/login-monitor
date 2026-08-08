# Login Monitor

import json
import i_json 
import dict 
from datetime import datetime

i_json.ij("logs.json")

def to_string(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")

menu= """
1-Login 
2-Show Logs 
3-Search User 
4-Delete Log 
5-Exit 
"""

while True:
    user_input= input(menu)
    found= False
    number= 3
    f= False
    #Login 
    if user_input=="1":
        username= input("username:")
        with open("logs.json","r") as file:
            passwords= json.load(file)
            for n in passwords:
                if username== n["username"]:
                    f= True
                    while number> 0:
                        password= input("password:")
                        p=dict.hashing(password)
                        if p==n["password hash"]:
                            found= True
                            print("welcome !")
                            break
                        else:
                            print("password is wrong!")
                            number-= 1
                    if not found:
                        print("you have to stop for 30 seconds!")
            if not f:
                password= input("password:")
                p=dict.hashing(password)
                login= dict.to_dict(username,p)
                passwords.append(login)
                with open("logs.json","w") as file:
                    json.dump(passwords,file,indent=4,default=to_string)
                    print("you loged in!")

    #Show Logs
    elif user_input=="2":
        with open("logs.json","r") as file:
            passwords_list= json.load(file)
            for p in passwords_list:
                print(f"username:{p["username"]}")
                print(f"password hash:{p["password hash"]}")
                print(f"login time:{p["login time"]}")
                print(f"host name:{p["host name"]}")
                print(f"ip:{p["ip"]}")
                print("----")

    #Search User
    elif user_input=="3":
        name= input("your name:")
        with open("logs.json","r") as file:
            logs=json.load(file)
            print(f"username:{name}")
            for l in logs:
                if name==l["username"]:
                    found= True
                    print(f"password hash:{p["password hash"]}")
                    print(f"login time:{p["login time"]}")
                    print(f"host name:{p["host name"]}")
                    print(f"ip:{p["ip"]}")
                    print("----")
            if not found:
                print(f"there is noone with name:{name}")

    #Delete Log 
    elif user_input=="4":
        delete_name= input("name:")
        with open("logs.json","r") as file:
            deletes= json.load(file)
            for d in deletes:
                if delete_name==d["username"]:
                    found= True
                    deletes.remove(d)
                    with open("logs.json","w") as file:
                        json.dump(deletes,file)
            if not found:
                print(f"there is noone with name:{delete_name}")

    #Exit 
    elif user_input=="5":
        print("have a good day!")
        break

    else:
        print("only between 1 & 5!")

#i_json 
#import json 
#import os 
#def ij(name):
#    if not os.path.exists(name):
#        with open(name,"w") as file:
#            json.dump([],file)

#dict
#from datetime import datetime
#import hashlib
#import socket
#def hashing(password):
#    hashed_password= hashlib.sha256(password.encode())
#    return str(hashed_password.hexdigest())
#def to_dict(name,password_hash):
#    login_time= datetime.now()
#    host_name= str(socket.gethostname())
#    ip= str(socket.gethostbyname(host_name))
#    return {"username":name,"password hash":password_hash,"login time":login_time,"host name":host_name,"ip":ip}

# 98 from 100 ! 