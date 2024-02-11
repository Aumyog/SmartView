import csv
import mysql.connector
def maxxx(n):
    maxx=200
    f=open(n)
    k=csv.reader(f)
    for i in k:
        if int(i[1])>maxx:
            maxx=int(i[1])
    f.seek(0)
    for i in k:
        if int(i[1])==maxx:
            print("Highest priced item is",i)
def minnn(n):
    minn=200
    f=open(n)
    k=csv.reader(f)
    for i in k:
        if int(i[1])<minn:
            minn=int(i[1])
    f.seek(0)
    for i in k:
        if int(i[1])==minn:
            print("Lowest priced item is",i)
def electronic():
    
    print("Here are the various category's to shop from\n1.)Electronics\n2.)Clothing\n3.)Books")
    
    chh=int(input("select any one of the following categories"))
    
    if chh==1:
        print("Select Subcategory \n1.)Smart phones and Speakers\n2.)Gaming Consoles\n3.)Laptops and Television\n4.)Go Back")
        chh2=int(input("Enter choice"))
        opt="y"
        while opt=="y":
            if chh2==4:
                electronic()#
                
            
                
                        
                            
            if chh2==1:
                f=open("Smartphones.txt")
                s=f.read()
                print(s)
                print("Do you want any filters")
                fil=input("enter (y/n)")
                if fil=="y":
                    print("1.)show item of highest price")
                    print("2.)show item of lowest price")
                    print("3.)show item of median price")
                
                    fil2=int(input("enter (1-4)"))
                    if fil2==1:
                        maxxx("electronic.csv")
                            
                            
                            

                           
                    if fil2==2:
                        minnn("electronic.csv")
                            
                            
                    if fil2==3:
                        print("median price is beats")
                
                if fil=="n":
                    from test2 import back
                    back()
                    
                        

                    
                        
            if chh2==2:

                f=open("gaming consoles.txt")
                s2=f.read()#
                print(s2)
                print("Do you want any filters")
                fil=input("enter (y/n)")
                if fil=="y":
                    print("1.)show item of highest price")
                    print("2.)show item of lowest price")
                    print("3.)show item of median price")
               
                    fil2=int(input("enter (1-4)"))
                    if fil2==1:
                        maxxx("gaming.csv")
                        
                        
                    if fil2==2:
                        minnn("gaming.csv")
                            
                    if fil2==3:
                        print("median price is XBOX-ONE-s")
                    if fil2==4:
                        opt="f"
                if fil=="n":
                    from test2 import back
                    back()
                        
                    
            if chh2==3:
                    
                f=open("laptops.txt")
                    
                s3=f.read(f)
                    
                    
                print(s3)
                print("Do you want any filters")
                fil=input("enter (y/n)")
                if fil=="y":
                    print("1.)show item of highest price")
                    print("2.)show item of lowest price")#
                    print("3.)show item of median price")
                    
                    fil2=int(input("enter (1-4)"))
                    if fil2==1:
                        maxxx("laptops.csv")
                        
                        
                    if fil2==2:
                        minnn("laptops.csv")

                            
                    if fil2==3:
                        print("median price is DELL")
                if fil=="n":
                    from test2 import back
    if chh==2:
        opt="y"
        while opt=="y":
            f=open("shirts.txt")
            s4=f.read()
            print(s4)
            print("Do you want any filters")
            fil=input("enter (y/n)")
            if fil=="y":
                print("1.)show item of highest price")
                print("2.)show item of lowest price")
                print("3.)show item of median price")
                print("4.)exit")
                fil2=int(input("enter (1-4)"))
                if fil2==1:
                    f=open("shirts.csv")
                    k=csv.reader(f)
                    maxx=200
                    for i in k:
                        if int(i[1])>maxx:
                            maxx=int(i[1])
                            f.seek(0)
                            for i in k:
                                if int(i[1])==maxx:#
                                    print("item is",i)
                if fil2==2:
                    minn=200
                    f=open("shirts.csv")
                    k=csv.reader(f)
                    for i in k:
                        if int(i[1])<minn:
                            minn=int(i[1])
                            f.seek(0)
                            for i in k:
                                if int(i[1])==minn:
                                    print("item is",i)
                if fil2==3:
                    print("median price is armani")
                if fil2==4:
                    electronic()
                    
            if fil=="n":
                opt="f"
                electronic()
                 
                
    if chh==3:
        
        opt="y"
        while opt=="y":
            f=open("books.txt")
            s4=f.read()
            print(s4)
            print("Do you want any filters")
            fil=input("enter (y/n)")
            if fil=="y":
                print("1.)show item of highest price")
                print("2.)show item of lowest price")
                print("3.)show item of median price")
                fil2=int(input("enter (1-4)"))
                if fil2==1:
                    f=open("books.csv")
                    k=csv.reader(f)#
                    maxx=200
                    for i in k:
                        if int(i[1])>maxx:
                            maxx=int(i[1])
                            f.seek(0)
                            for i in k:
                                if int(i[1])==maxx:
                                    print("item is",i)
                if fil2==2:
                    minn=200
                    f=open("books.csv")
                    k=csv.reader(f)
                    for i in k:
                        if int(i[1])<minn:
                            minn=int(i[1])
                            f.seek(0)
                            for i in k:
                                if int(i[1])==minn:
                                    print("item is",i)
                if fil2==3:
                    print("median price is Harry Potter")
            if fil=="n":
                electronic()
def entire():
    
    print("========================================================")
    print('             WELECOME TO Smartview           ') 
    print('1.SIGN IN',end= "     ")
    print('2.CREATE USER ACCOUNT',end="     ")
    print('3.EXIT')
    print("========================================================")
    ch1=int(input('ENTER YOUR CHOICE:'))

    if ch1==1:
        
        print("=======================USER LOGIN=======================")
        u1=input("Enter Username: ")
        p1=input("Enter Password: ")
        mydb=mysql.connector.connect(host="localhost",user="root",password="shalimar11",database="project")
        mycursor=mydb.cursor()
        mycursor.execute("select Username,password from accounts;")
        y=mycursor.fetchall()
        for i in y:
            if u1==i[0] and p1==i[1]:
                
                
                
                print()
                print()
                print()
                print("          Login Succesfull!")
                print("          Welcome",u1)
                print("       What would you like to shop today?       ")

            
                print("Here are the various category's to shop from\n========================================================\n1.)Electronics\n========================================================\n2.)Clothing\n========================================================\n3.)Books\n========================================================")
                chh=int(input("Select any one of the following categories"))
                if chh==1:
                    print("=======a==========Select Subcategory====================\n1.)Smart phones and Speakers\n2.)Gaming Consoles\n3.)Laptops and Television\n4.)Go Back")
                    chh2=int(input("Enter choice"))
                    opt="y"
                    while opt=="y":
                        if chh2==4:
                            
                            
                            
                            from test import electronic
                            electronic()
                        
                                
                                    
                        if chh2==1:
                            f=open("Smartphones.txt")
                            s=f.read()
                            print(s)
                            print("Do you want any filters")
                            fil=input("enter (y/n)")
                            if fil=="y":
                                print("1.)show item of highest price")
                                print("2.)show item of lowest price")
                                print("3.)show item of median price")
                                fil2=int(input("enter (1-4)"))
                                if fil2==1:
                                    maxxx("electronic.csv")
                                    
                                    
                                    

                                   
                                if fil2==2:
                                    minnn("electronic.csv")
                                    
                                    
                                if fil2==3:
                                    print("median price is beats")
                                if fil2==4:
                                    from test2 import back
                                    back()
                                    
                        
                            
                            if fil=="n":
                                from test2 import back
                                back()
                            
                            
                                
                        if chh2==2:
                            f=open("gaming consoles.txt")
                            s2=f.read()
                            print(s2)
                            print("Do you want any filters")
                            fil=input("enter (y/n)")
                            if fil=="y":
                                print("1.)show item of highest price")
                                print("2.)show item of lowest price")
                                print("3.)show item of median price")
                                
                                fil2=int(input("enter (1-4)"))
                                if fil2==1:
                                    maxxx("gaming.csv")
                                   
                                if fil2==2:
                                    minnn("gaming.csv")
                                   
                                if fil2==3:
                                    print("median price is XBOX-One-S")
                                if fil2==4:
                                    from test2 import back
                                    back()
                               
                            if fil=="n":
                                from test2 import back
                                back()
                                
                            
                        if chh2==3:
                            
                            f=open("laptops.txt")
                            
                            s3=f.read()
                            
                            
                            print(s3)
                            print("Do you want any filters")
                            fil=input("enter (y/n)")
                            if fil=="y":
                                print("1.)show item of highest price")
                                print("2.)show item of lowest price")
                                print("3.)show item of median price")
                                
                                fil2=int(input("enter (1-4)"))
                                if fil2==1:
                                    maxxx("laptops.csv")
                                    
                                if fil2==2:
                                   minnn("laptops.csv")
                                if fil2==3:
                                    print("median price is dell")
                                if fil2==4:
                                    from test2 import back
                                    back()
                            if fil=="n":
                                from test2 import back
                                
                                back()
                            
                            
                if chh==2:
                    opt="y"
                    while opt=="y":
                        
                        f=open("shirts.txt")
                                    
                        s4=f.read()
                        print(s4)
                        print("Do you want any filters")
                        fil=input("enter (y/n)")
                        if fil=="y":
                            print("1.)show item of highest price")
                            print("2.)show item of lowest price")
                            print("3.)show item of median price")
                           
                            fil2=int(input("enter (1-4)"))
                            if fil2==1:
                                f=open("shirts.csv")
                                k=csv.reader(f)
                                maxx=200
                                            
                                for i in k:
                                    if int(i[1])>maxx:
                                            maxx=int(i[1])
                                f.seek(0)
                                for i in k:
                                    if int(i[1])==maxx:
                                        print("item is",i)
                            if fil2==2:
                                minn=200
                                f=open("shirts.csv")
                                k=csv.reader(f)
                                for i in k:
                                    if int(i[1])<minn:
                                        minn=int(i[1])
                                f.seek(0)
                                for i in k:
                                    if int(i[1])==minn:
                                        print("item is",i)
                            if fil2==3:
                                print("median price is armani")
                            if fil2==4:
                                from test import electronic
                                electronic()
                                
                                
                        if fil=="n":
                            opt="f"
                            from test import electronic
                            electronic()
            

                if chh==3:
                    
                    
                    opt="y"
                    while opt=="y":
                        f=open("books.txt")
                        s4=f.read()
                        print(s4)
                        print("Do you want any filters")
                        fil=input("enter (y/n)")
                        if fil=="y":
                            print("1.)show item of highest price")
                            print("2.)show item of lowest price")
                            print("3.)show item of median price")
                            fil2=int(input("enter (1-4)"))
                            if fil2==1:
                                f=open("books.csv")
                                k=csv.reader(f)
                                maxx=100
                                for i in k:
                                    if int(i[1])>maxx:
                                        maxx=int(i[1])
                                        f.seek(0)
                                        for i in k:
                                            if int(i[1])==maxx:
                                                print("item is",i)
                            if fil2==2:
                                minn=70
                                f=open("books.csv")
                                k=csv.reader(f)
                                for i in k:
                                    if int(i[1])<minn:
                                        minn=int(i[1])
                                        f.seek(0)
                                        for i in k:
                                            if int(i[1])==minn:
                                                print("item is",i)
                            if fil2==3:
                                print("median price is Harry potter")
                        if fil=="n":
                            from test import electronic
                            electronic()
    else:
        print("try again")
        entire()
    
