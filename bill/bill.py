import sys
import os
import datetime

def bilcal():
    filename="price.txt"
    accessmode="a"
    file=open(filename,accessmode)
    #qty=0
    itm=0
    tot=0
    currentDate=datetime.date.today()
    print(currentDate.strftime("%d %B %Y" ))
    while True:
        try:
            price=input("\nEnter Item Price:Rs ")
            if not price:
                if not tot:
                    print("Invalid")
                    quit()
                break
            #qty=float(input("Enter Quntity: "))
            #if not qty:
                #if not price:
                    #print("Invalid")
                    #quit()
                #break
            itm=price
            tot+=float(itm)
   
        except ValueError as e:
           print(e)
           #break
        
    if tot>=10000:
        y=tot*0.4
        subtot=tot-y
        dis="40%"       
        
    elif tot>= 5000:
        y=tot*0.1
        subtot=tot-y
        dis="10%"
        
    elif tot>= 1000:
        y=tot*0.05
        subtot=tot-y
        dis="5%"
        
    else:
        y=0
        subtot=tot
        dis="0%"
        
        
    print("\n\tYou Get "+ dis +" Discount")    
    print("\tYour Price Is :Rs %.2f" % tot)
    print("\tDiscount Value is :Rs %.2f" % y)
    print("\n\tDiscount Price is :Rs %.2f" % subtot)
   # print("\n Your bill has Printed !!!!")
    file.write("\n.........................................\n")
    file.write(currentDate.strftime("%d %B %Y "))
    file.write("\n.........................................")
    file.write("\n\tYou Get "+ dis +" Discount \n")
    file.write("\tYour Price Is :Rs %.2f" % tot)
    file.write("\n\tDiscount Value is :Rs %.2f" % y)
    file.write("\n\tDiscount Pice is :Rs %.2f" % subtot)
    file.close()
bilcal()
