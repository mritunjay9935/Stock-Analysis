from http import client
from tokenize import group
import pymongo
import pandas as pd
import json
import array as arr

client = pymongo.MongoClient("mongodb://localhost:27017")

# df = pd.read_excel("VARNEW.xlsx")
# data = df.to_dict(orient="records")


db = client["UPORTFOLIO"]
mycollection = db["VARNEW"]

# db.VARNEW.insert_many(data)


a=[]
f=[]
n=int(input("Enter the number of Stocks Item:"))
for i in range(0,n):
   l=(str(input())).upper()
   m=int(input("Required Quantity:")) 
   a.append(l)
   f.append(m)
# print("Stock Name:",a) 

b = []
for i in range(0,n):
    record_one = mycollection.find_one({"Stock Name":a[i]},{"VARL":1,"_id":0})
    b.append(record_one.get("VARL"))
    

c = []
for i in range(0,n):
    record_two = mycollection.find_one({"Stock Name":a[i]},{"VARR":1,"_id":0})
    c.append(record_two.get("VARR"))
   

d = []
for i in range(0,n):
    record_three = mycollection.find_one({"Stock Name":a[i]},{"ELM":1,"_id":0})
    d.append(record_three.get("ELM"))

price = []    
for i in range(0,n):
    price.append(b[i]*c[i]*d[i])
# print("Stock Prices Are:", price)



# print("Quantities:", f)

Total = [] 
for i in range(0,n):
    Total.append(price[i]*f[i])
# print("Total:",Total)

e = []
for i in range(0,n):
    record_four = mycollection.find_one({"Stock Name":a[i]},{"Total VAR":1,"_id":0})
    e.append(record_four.get("Total VAR")) 
# print("Total Var Values in %: ", e)


Varvalue = []
for  i in range(0,n):
    Varvalue.append(e[i]*Total[i])
# print("Var Values:",Varvalue)


# print("SName   Price   Qunty    Total   Var(%)   VarValue")   
for i in range(0,n):
    print(a[i],"(SN)","   ",int(price[i]),"(P)","   ",f[i],"(Q)","   ",int(Total[i]),"(T)","   ",e[i],"(V%)","   ",int(Varvalue[i]),"(Vvalue)")

    





    
    
