from datetime import datetime
name=input ("enter your name:")
mobile_no=int(input("enter your mobile number:"))
lists="""
********************

toordal     RS 80/kg
moongdal    RS 60/kg
chanadal    RS 90/kg
brown rice  RS 100/kg
sugar       RS 30/kg
salt        RS 20/kg
oil         RS 250/liter
groundnuts  RS 80/kg

*********************
"""
print("1.enter 1 to see products\n2.to exit\n")
choice=int(input("enter your choice:"))
if choice==1:
    print(lists)
else:
    print("exit") 

price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]      

items={"toordal":80,"moongdal":60,"chanadal":90,"brown rice":100,
       "sugar":30,"salt":20,"oil":250,"groundnuts":80}
for i in range(len(items)):
    print("1.if you want to buy press 1 or 2.to exit ")
    option=int(input("enter option:"))
    if option==1:
        item=input("enter product name:")
        quantity=int(input("enter product quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            print(price)
            pricelist.append((item,quantity,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            GST=(totalprice*5)/100
            finalprice=GST+totalprice
        else:
            print("entered product is not available ")    

    elif option==2:
        print("exit")
        break
    else:
        print("enter valid option")

print("1.to generate bill\n2.to buy again\n")
choice=int(input("enter choice:"))
if choice==1:
    if finalprice!=0:
        print(25*"=","BALAJI SUPERMARKET",25*"=")
        print(25*" ","chennai",25*" ")
        print("Name:",name,30*" ",datetime.now())
        print(75*"-")
        print("sno.",4*" ","items",12*" ","quantity",8*" ","price")
        for i in range(len(pricelist)):
            print(i,8*" ",ilist[i],15*" ",qlist[i],16*" ",plist[i])
        print(75*"-")
        print(50*" ","Total Amount:","Rs",totalprice)
        print(50*" ","GST amount:","Rs",GST)
        print(75*"-")
        print(50*" ","final price:","Rs",finalprice)
        print(75*"-")
        print(10*" ","thank you for purchasing in our supermarket")
        print(75*"-")
           



