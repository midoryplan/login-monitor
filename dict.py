from datetime import datetime
import hashlib
import socket

def hashing(password):
    hashed_password= hashlib.sha256(password.encode())
    return str(hashed_password.hexdigest())

def to_dict(name,password_hash):
    login_time= datetime.now()
    host_name= str(socket.gethostname())
    ip= str(socket.gethostbyname(host_name))
    return {"username":name,"password hash":password_hash,"login time":login_time,"host name":host_name,"ip":ip}