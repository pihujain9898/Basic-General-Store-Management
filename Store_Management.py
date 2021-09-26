import mysql.connector as msc
import pandas as pd

a2 = input("Enter password of your mysql: ")

def main():
    def one():
        cursor.execute("select * from product")
        product_data = cursor.fetchall()
        product = pd.DataFrame(product_data,columns = ['PID','Item','Quantity','Cost PI'])
        print("Store items and their details :-")
        print(product)
    def two():
        cursor.execute("select * from product")
        product_data = cursor.fetchall()
        product = pd.DataFrame(product_data,columns = ['PID','Item','Quantity','Cost PI'])
        v1 = input("Item name : ")
        v2 = int(input('Quantity of item : '))
        v3 = int(input("Cost of item : "))
        v4 = int(product.iloc[-1:,-4])
        s1 = "insert into product values({},'{}',{},{})".format(v4 +1 ,v1,v2,v3)
        cursor.execute(s1)
        obj.commit()
    def three():
        cursor.execute("select P_ID,Item from product")
        product_data = cursor.fetchall()
        product = pd.DataFrame(product_data,columns = ['P_ID','Product'])
        print('Choose the prodcut with their respective ID Number.')
        print(product)
        v9 = True
        l2= []
        v19 = 0
        while v9:
            v19 = 1 + v19
            v9 = int(input("Choose the prodcut with their respective ID Number. or to exit '0' : "))
            if v9 != 0:
                v11 = int(input("Quantity of product required : "))
                cursor.execute("select quantity,item,Cost_Item from product where P_ID = {}".format(v9))
                v15 = cursor.fetchall()
                v12 = int(v15[0][0])
                v16 = v15[0][1]
                v17 = int(v15[0][2])
                cursor.execute("update product set quantity = {} where P_ID = {}".format(v12-v11,v9))
                obj.commit()
                cursor.execute("insert into bill values({},'{}',{},{},{})".format(v19,v16,v11,v17,v11*v17))
                obj.commit()
                cursor.execute("select * from bill")
                v18 = cursor.fetchall()
                l2.append(v18)
                cursor.execute("truncate table bill")
                obj.commit()
            else:
                v9 = False
                break
        l3 = []      
        for x in range(len(l2)):
            l3.append(l2[x][0])
        d1 = pd.DataFrame(l3,columns = ['SNO','Item','Quantity','Cost PI','Total C'])
        print("Custumer bill :-")
        print(d1)
        print("Grand total :",d1.loc[:,'Total C'].sum())  
    a1 = True
    while a1 == True:
        print("Choose your choice or press 0 to quit the software.")
        print("1. View store items and their details.")
        print("2. Add new item in store.")
        print("3. Costumer transaction.")
        choice = int(input('Enter your choice : '))
        if choice == 1:
            one()
        elif choice == 2:
            two()
        elif choice == 3:
            three()
        elif choice == 0:
            a1 = False
        else:
            print("Your choice is not defined please recheck it.")

try:
    obj = msc.connect(host = "localhost",
                  user = "root",
                  passwd = a2,
                  database = "Store_Management")
    cursor = obj.cursor()
    main()
except:
    obj = msc.connect(host = "localhost",
                      user = "root",
                      passwd = a2,
                      database = "mysql")
    cursor = obj.cursor()
    s1 = "insert into product values(1,'Sugar',20,45),(2,'Floar',80,25),(3,'Rice',20,60),(4,'Meda',20,28),(5,'Suji',20,18);"
    s2 = "insert into product values(6,'Moong Daal',20,55),(7,'Udad Daal',20,60),(8,'Rajma',20,65),(9,'Salt',20,20),(10,'S.Biscuit',40,10);"
    cursor.execute("create database Store_Management;")
    cursor.execute("use Store_Management;")
    cursor.execute("create table product(P_ID int,Item varchar(40),Quantity int,Cost_Item int);")
    cursor.execute("create table bill(Item varchar(40),Quantity int,Cost_PI int,T_Cost int);")
    cursor.execute(s1)
    cursor.execute(s2)
    obj.commit()
    main()


    
