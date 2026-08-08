import json 
import os 

def ij(name):
    if not os.path.exists(name):
        with open(name,"w") as file:
            json.dump([],file)