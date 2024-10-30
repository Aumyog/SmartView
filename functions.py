import csv
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


def back():
    print("Select Subcategory \n1.)Smart phones and Speakers\n2.)Gaming Consoles\n3.)Laptops and Television\n4.)Go Back")
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
                print("4.)exit")
                fil2=int(input("enter (1-4)"))
                if fil2==1:
                    maxxx("electronic.csv")
                           
                if fil2==2:
                    minnn("electronic.csv")
                            
                            
                if fil2==3:
                    print("median price is beats")
                
        else:
                
            opt='f'
                    
                        
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
                print("4.)exit")#
                fil2=int(input("enter (1-4)"))
                if fil2==1:
                    maxxx("gaming.csv")
                        
                        
                if fil2==2:
                    minnn("gaming.csv")
                            
                if fil2==3:
                    print("median price is Xbox-One-s")
            if fil=="n":
                back()
        else:
            opt="f"
                        
                    
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
                print("4.)exit")
                fil2=int(input("enter (1-4)"))
                if fil2==1:
                    maxxx("laptops.csv")
                        
                        
                if fil2==2:
                    minnn("laptops.csv")

                            
                if fil2==3:
                    print("median price is dell")
                if fil2==4:
                    opt="f"
        else:
                
            opt="f"
