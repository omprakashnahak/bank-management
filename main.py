#bank account
#deposite money
#withdraw money
#details
#update details
#delete account



import json
import random
import string
from pathlib import Path




class Bank:
    database='data.json'
    data=[]
    try:
        if Path(database).exists:
            with open(database)as fs:
                data =json.loads(fs.read())
        else:
            print("no such file exists")
        
    except Exception as err:
       print(f"an exception occoured as {err}")

    @classmethod
    def __update(cls):
        with open (Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accontgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*,k=1")
        id= alpha+ num+ spchar 
        random.shuffle(id)
        return"".join(id)




    
    def Createaccount(self):
        info={
            "name": input("tell ur name:- "),
            "age": input("tell ur age:- "),
            "email": input("tell ur email:- "),
            "pin": int(input("tell ur pin:- ")),
            "accountNo": Bank.__accontgenerate(),
            "balance": 0
        }
        if int(info["age"]) < 18 or len(str(info['pin']))!=4:
            print("sorry you cant create your account")
        else:
            print("account has been created succesfully")
            for i in info:
                print(f"{i}:{info[i]}")
            print("please note ur account number")    
            Bank.data.append(info)
            Bank.__update()
    def depositmoney(self):
        accnumber=input("plz tell ur account number :-")
        pin=int(input("plz tell ur pin number"))


        userdata=[i for i in Bank.data if i ['accountNo']==accnumber and i['pin']==pin]
        if userdata== False:
            print("sorry no data found")
        else:
            amount=int(input("how much you want to deposite"))
            if amount>10000 or amount<0:
                print("sorry the amount is too much you can deposite below 10000 and above 0")

            else:
                print(userdata)
                
                userdata[0]['balance']+=amount
                Bank.__update()
                print("amount deposited successsfully")


    def withdrawmoney(self):
        accnumber=input("plz tell ur account number :-")
        pin=int(input("plz tell ur pin number"))

        userdata=[i for i in Bank.data if i ['accountNo']==accnumber and i['pin']==pin]
        
        if userdata==False:
            print("Sorry no data found")
        else:
            amount = int(input("How much you want to withdraw: "))
            print(userdata)
            if userdata[0]['balance']<amount:
                print("Sorry you don't have that much money")
            else:
                userdata[0]['balance']-=amount
                Bank.__update()
                print("Amount withdrawn successfully")
       
    def showdetails(self):
        accnumber=input("plz tell ur account number :-")
        pin=int(input("plz tell ur pin number"))
        userdata=[i for i in Bank.data if i ['accountNo']==accnumber and i['pin']==pin]
        print("your information are:-")
        for i in userdata[0]:
            print(f"{i}: {userdata[0][i]}")

    def updatedetails(self):
        accnumber=input("plz tell ur account number :-")
        pin=int(input("plz tell ur pin number"))
        userdata=[i for i in Bank.data if i ['accountNo']==accnumber and i['pin']==pin]

        if userdata==False:
            print("no such user found")

        else:
            print("you cant change ur age ,account number and balance")
            print("fill the details for the changes or leave it empty if")
            newdata= {
                "name":input("please tell ur new name or press enter : "),
                "email":input("please tell ur new email or press enter to skip : "),
                "pin":input("tell ur new pin or press enter to skip: ")
                    }
            if newdata["name"]=="":
                newdata["name"]=userdata[0]['name']    
            if newdata["email"]=="":
                newdata["email"]=userdata[0]['email']     
            if newdata["pin"]=="":
                newdata["pin"]=userdata[0]['pin']

             

user = Bank()
print("press 1 for creating an account")
print("press 2 for depositing money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check=int (input("tell your response:- "))


if check==1:
    user.Createaccount()

if check==2:
    user.depositmoney()

if check==3:
    user.withdrawmoney()

if check==4:
    user.showdetails()

if check==5:
    user.updatedetails()






















