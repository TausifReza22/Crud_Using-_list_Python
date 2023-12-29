list=[]
while True:
    print("1.Create\n2.Read\n3.Update\n4.Delete\n5.Exit")
    choice=int(input("Enter the choice:>"))
    if choice==1:
        n=input("enter the name   :--")
        print(n)
        while True:
            mobileno=input("Enter the Mobile No.")
            if len(mobileno)==10:
                print(mobileno,("\n your mobile no. is valid "))
                break
            else:
                print(mobileno,"\nnot valid")
        while True:        
            gmail = input("Enter the Gmail: ")
            
            if ".com" in gmail and "gmail" in gmail and "@" in gmail:
                print(gmail)
                break
            else:
                print("Invalid Gmail. Please enter a valid Gmail address.")
        while True:
                password=input("Enter the Password:>")
                if len(password)==8:
                        if (
                            any(char.isupper() for char in password)
                            and any(char.islower() for char in password)
                            and any(char.isdigit() for char in password)
                            and any(char in "~!@#$%^&*_" for char in password)
                        ):
                            print("your password is corect")
                        

                            break 
                        else:
                            print("Incorrect:-")
                else:
                    print("wrong password")
        list.append(n)
        list.append(mobileno)
        list.append(gmail)
        list.append(password)
        print("your data is created successfully:-")
    
    elif choice==2:
        n=input("enter the name:-")
        if n in list:
            password1=input("Enter the password:>>>")
            if list[3]==password1:
                print("this was your first data",list)
                # print("your data is")
                # print(n)
                # print(mobileno)
                # print(gmail)
                # print(password)
            else:
                print("incorrect password:-")
        else:
            print("user id not found:-")
            
    elif choice==3:
        newname=input("enter the name:>")
        if list[0]==newname:
            print("1.n\n2.mobileno\n3.gmail\n4.password")
            choice=int(input("Enter the choice:>>>"))
            if choice==1:
                upn=input("Enter the update name:>")
                list[0]=upn
                print(list)
            elif choice==2:
                upn=int(input("Enter the update mobile no:>>"))
                list[1]=upn
                print(list)
            elif choice==3:
                upn=input("Enter the update gmail:>>")
                list[2]=upn
                print(list)
            elif choice==4:
                upn=input("Enter the update password:>>")
                list[3]=upn
                print(list)
        else:
            print("please enter your correct name")
    elif choice==4:
        newname=input("Enter the name to Delete:>>>")
        if list[0]==newname:
            print("What you want to Delete\n1.n\n2.mobileno\n3.gmail\n4.password")
            chose=int(input("enter the choie >>>>>"))
            if chose==1:
                list.remove(list[0])
                
                print([list])
            elif chose==2:
                list.remove(list[1])
                i=1
                v=[]
                list.insert(i,v)
                print([list])
            elif chose==3:
                list.remove(list[2])
                j=2
                k=[]
                list.insert(j,k)
                print([list])
            elif chose==4:
                
                list.remove(list[3])
                l=3
                m=[]
                list.insert(l,m)
                print([list])
    elif choice==5:
        print("Thank You")
    else:
        print("Choice is wrong please choice right option")
        
        
