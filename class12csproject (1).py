import mysql.connector
import datetime
from tabulate import tabulate
db=input("enter the name of the database to be created or used:")
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Vyusti@123")
mycursor=mydb.cursor()
sql="create database if not exists %s"%(db,)
mycursor.execute(sql)
print("database successfully created")
query="use %s"%(db,)
mycursor.execute(query)
table=input("enter the name of the table to be created or used:")
query="create table if not exists '{}'(item_no int,item_name varchar(50),price float,qty int)".format(table,)
print("table created successfully")
print('*'*150)
print("\t\t\t\tmain menu")
print('*'*160)
while True:
    print("press 1 to insert new item")
    print("press 2 to display all the items")
    print("press 3 to display particular item")
    print("press 4 to update the table")
    print("press 5 for billing")
    print("press 6 to delete all the items")
    print("press 7 to delete a particular item")
    print("press 8 to know the items to be resupplied")
    print("press 9 to exit")
    c=int(input("enter your choice"))
    #inserting records
    if c==1:
        item_no=int(input("enter the item_no."))
        item_name=input("enter the item_name")
        price=float(input("enter the price"))
        qty=int(input("enter the quantity"))
        query="insert into products values({},'{}',{},{})".format(item_no,item_name,price,qty)
        mycursor.execute(query)
        mydb.commit()
        print("record inserted successfully")
    #to display all records
    elif c==2:
        query="select * from %s"%(table,)
        mycursor.execute(query)
        data=mycursor.fetchall()
        print(tabulate(data,headers=['item_no','item_name','price','quantity'],tablefmt="fancy_grid"))
    #to diplay particular record
    elif c==3:
        try:
            item_no=int(input("enter the item_no"))
            query="select * from %s where item_no=%s"%(table,item_no)
            mycursor.execute(query)
            data=mycursor.fetchone()
            a=mycursor.rowcount
            if a==-1:
                print("itemno doesnt exist")
            else:
                print(data)
        except:
            print("something went wrong")
    # to update the table
    elif c==4:
        try:
            item_no=int(input("enter the item_no"))
            query="select * from %s where item_no=%s"%(table,item_no)
            mycursor.execute(query)
            data=mycursor.fetchone()
            a=mycursor.rowcount
            if a==-1:
                print("itemno doesnt exist")
            else:
                item_no=data[0]
                item_name=data[1]
                price=data[2]
                quantity=data[3]
                print("item_no:",data[0])
                print("item_name:",data[1])
                print("price:",data[2])
                print("quantity:",data[3])
                print('-'*50)
                print("type value to modify or just press enter for no change")
                x=input("enter name")
                if len(x)>0:
                    item_name=x
                y=input("enter the price")
                if len(y)>0:
                    price=float(y)
                z=input("enter the quantity")
                if len(z)>0:
                    quantity=int(z)
                query="update {} set item_name='{}',price={},qty={} where item_no={}".format(table,item_name,price,quantity,item_no)
                mycursor.execute(query)
                mydb.commit()
                print("modification done successfully")
        except:
            print("something went wrong")
    # for billing
    elif c==5:
        bill=0
        l=[]
        while True:
            item=input("enter the name of item")
            query="select * from {} where item_name='{}'".format(table,item)
            mycursor.execute(query)
            data=mycursor.fetchone()
            item_no=data[0]
            item_name=data[1]
            price=data[2]
            quantity=data[3]
            print("item_no:",data[0])
            print("item_name:",data[1])
            print("price:",data[2])
            print("quantity:",data[3])
            qt=int(input("enter the quantity required"))
            if data[3]>=qt:
                quantity=data[3]-qt
                query="update {} set qty={} where item_name='{}'".format(table,quantity,item)
                print(query)
                mycursor.execute(query)
                price_each=data[2]*qt
                bill=bill+price_each
                r=(data[1],data[2],qt,price_each)
                l.append(r)
                mydb.commit()
            else:
                print("item unavailable at present")
            b=input("more item to be purchased? (y/n)")
            if b=='n':
                break
        print("\n\n\n")
        print(160*'*')
        print("BILL".center(90))
        now=datetime.datetime.now()
        print("current date and time:")
        print(now.strftime("%Y-%n-%d %H:%M:%S"))
        print(tabulate(l,headers=['item_no','item_name','qty','totalprice'],tablefmt="fancy_grid"))
        print("TOTAL COST",bill)
    # to delete all records
    elif c==6:
        try:
            ch=input("do you want to delete all the records (y/n)")
            if ch.lower()=='y':
                mycursor.execute('delete from'+table)
                mydb.commit()
                print("all records are deleted")
        except:
            print("something went wrong")
    # to delete a particular record
    elif c==7:
        try:
            inn=int(input("enter the item no to be deleted"))
            query="delete from {} where item_no={}".format(table,inn)
            mycursor.execute(query)
            mydb.commit()
            a=mycursor.rowcount
            if a>0:
                print("deletion done")
            else:
                print("item no",inn,"not found")
        except:
            print("something went wrong")
    # to know the items which are to be ordered
    elif c==8:
        try:
            query="select item_no,item_name from {} where qty<10".format(table,)
            mycursor.execute(query)
            data=mycursor.fetchall()
            print("ALERT!!!,items whose quantity is less than 5")
            print(tabulate(data,headers=['item_no','item'],tablefmt='psql'))
        except:
            print("something went wrong")
    # to exit
    elif c==9:
        print("THANK YOU!!!")
        break
    else:
        print("invalid entry")
        
                
                
            
            

            
            

   
        
        
        






