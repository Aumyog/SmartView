import csv
import mysql.connector
def view_products(mycursor, order="ASC"):
    if order not in ["ASC", "DESC"]:
        print("Invalid order specified. Defaulting to ASC.")
        order = "ASC"
    
    sql = f"SELECT id, name, price FROM products ORDER BY price {order}"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    
    if len(results) == 0:
        print("No products found.")
        return
    
    print("================================================================================")
    print("| {:<4} | {:<30} | {:<10} |".format("ID", "Product Name", "Price ($)"))
    print("================================================================================")
    
    for row in results:
        id, name, price = row
        print("| {:<4} | {:<30} | {:<10.2f} |".format(id, name, price))
    
    print("================================================================================")
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
            print("========================================================")
            print("Lowest priced item is",i)
            print("========================================================")
def main():
    print("=======================================================================================")
    print('                             Welcome To Smartview                     ') 
    print('1.SIGN IN',end= "     ")
    print('2.CREATE USER ACCOUNT',end="     ")
    print('3.EXIT',end="     ")
    print('4.MYSQL DATABASE DIRECT ACCESS')
    print("=======================================================================================")

    ch1=int(input('ENTER YOUR CHOICE:'))
    if ch1==4:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shalimar11",
            database="project"
        )
        mycursor = mydb.cursor()
        
        while True:
            print("========================================================")
            print("Database Direct Access:")
            print("1. Add Data")
            print("2. Remove Data")
            print("3. View Data")
            print("4. View Data (Highest to Lowest Price)")
            print("5. View Data (Lowest to Highest Price)")
            print("6. Exit")
            
            ch2 = int(input("Enter your choice: "))
            
            if ch2 == 1:
                prod_name = input("Enter product name: ")
                prod_price = float(input("Enter product price: "))
                sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
                val = (prod_name, prod_price)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                
            elif ch2 == 2:
                prod_id = input("Enter product ID to delete: ")
                sql = "DELETE FROM products WHERE id = %s"
                val = (prod_id,)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) deleted.")
                
            elif ch2 == 3:
                 view_products(mycursor)
                    
        
            elif ch2 == 4:
                view_products(mycursor, "DESC")  # View products from highest to lowest price
            
            elif ch2 == 5:
                view_products(mycursor, "ASC")  #
            elif ch2==6:
                main()
            else:
                print("Invalid choice, please try again.")
            
    if ch1==1:
        print("=======================USER LOGIN=======================")#
        u1=input("Enter Username: ")
        p1=input("Enter Password: ")
        mydb=mysql.connector.connect(host="localhost",user="root",password="shalimar11",database="project")
        mycursor=mydb.cursor()
        query="select password from accounts where Username=%s;"
        mycursor.execute(query, (u1,))
        y=mycursor.fetchall()
        for i in y:
            if  p1==i[0]:              
                print()
                print()
                print()
                print("          Login Succesfull!")
                print("          Welcome",u1)
                print("       What would you like to shop today?       ")
                print("Here are the various category's to shop from\n========================================================\n1.)Electronics\n========================================================\n2.)Clothing\n========================================================\n3.)Books\n========================================================\n4.)Log Out\n========================================================\n")
                chh=int(input("Select any one of the following categories"))
                if chh==4:
                    main()
                if chh==1:
                    print("==================Select Subcategory====================\n1.)Smart phones and Speakers\n2.)Gaming Consoles\n3.)Laptops and Television\n4.)Go Back\nLogout")                   
                    chh2=int(input("Enter choice"))
                    opt="y"
                    while opt=="y":
            
                        if chh2==4:
                            from SQLIntegrator import electronic
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
                                fil2=int(input("enter (1-4)"))#
                                if fil2==1:
                                    maxxx("electronic.csv")
                                if fil2==2:
                                    minnn("electronic.csv")
                                if fil2==3:
                                    print("median price is beats")
                                if fil2==4:
                                    from functions import back
                                    back()
                            if fil=="n":
                                from functions import back
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
                                    from functions import back
                                    back()
                               
                            if fil=="n":
                                from functions import back
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
                                    from functions import back
                                    back()
                            if fil=="n":
                                from functions import back
                                
                                back()
                            
                            
                if chh==2:
                    opt="y"
                    while opt=="y":
                        
                        f=open("shirts.txt")#
                                    
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
                               from SQLIntegrator import electronic
                               electronic()
                                
                                
                                
                        if fil=="n":
                            opt="f"
                            from SQLIntegrator import electronic
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
                                f=open("books.csv")#
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
                            from SQLIntegrator import electronic
                            electronic()

            else:
                print("try again")
                main()
                
    elif ch1==2:
        name=input("ENTER YOUR USER NAME:")
        pas=input("ENTER YOUR PASSWORD:")
        mydb=mysql.connector.connect(host="localhost",user="root",password="shalimar11",database="project")
        mycursor=mydb.cursor()
        mycursor.execute("insert into accounts(Username,password) values(%s,%s)",(name,pas))
        mydb.commit();
        print("=========================================")
        print("Adding these details to our MYSQL databse")
        print("=========================================")
        print("Try Log in now")
        print("=========================================")
        u1=input("Enter username")
        query="select password from accounts where Username=%s;"
        mycursor.execute(query, (u1,))
        y=mycursor.fetchall()
        p1=input("Enter password")
        if p1==y[0][0]:
            print("Login Successful")
            from SQLIntegrator import electronic
            electronic()
        else:
            print("try again")
            #from test import entire
            main()
    elif (ch1==3):
        print("bye,see you soon!")

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

def electronic():
    
    print("Here are the various category's to shop from\n1.)Electronics\n2.)Clothing\n3.)Books\n4.)Go back")
    
    
    chh=int(input("select any one of the following categories"))
    if chh==4:
        main()
    if chh==1:
        print("Select Subcategory \n1.)Smart phones and Speakers\n2.)Gaming Consoles\n3.)Laptops and Television\n4.)Go Back")
        chh2=int(input("Enter choice"))
        opt="y"
        while opt=="y":
            if chh2==4:
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
                
                if fil=="n":
                    from functions import back
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
                    from functions import back
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
                    from functions import back
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
                            
                            
                            
                            from SQLIntegrator import electronic
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
                                    from functions import back
                                    back()
                                    
                        
                            
                            if fil=="n":
                                from functions import back
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
                                    from functions import back
                                    back()
                               
                            if fil=="n":
                                from functions import back
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
                                    from functions import back
                                    back()
                            if fil=="n":
                                from functions import back
                                
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
                                from SQLIntegrator import electronic
                                electronic()
                                
                                
                        if fil=="n":
                            opt="f"
                            from SQLIntegrator import electronic
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
                            from SQLIntegrator import electronic
                            electronic()
    else:
        print("try again")
        main()
    
