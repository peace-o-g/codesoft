while True:
    #take user choice of number
    a=float(input("\nenter first num: "))
    b=float(input("enter second num: "))

    print("\n1-for addition\n2-for substraction")
    print("3-for multiplication\n4-for division")

  #taking user choice for operation
    choice=input("\nfunction you want to perform: ")
    print("\n")
    if choice=="1":
        print(f'addition= {a+b}')
      
    elif choice=="2":
        print(f"substaraction={a-b}")
       
    elif choice=="3":
        print(f"product={a*b}")    
        
    elif choice=="4":
        print(f"division={a/b}")
        print(f'reminder={a%b}')    
        
    else:
        print("enter correcrt choice!")
        continue

    #for using again    
    print("\nwant to use again?")
    yes_no=str(input("(Y/N)").upper())
    if yes_no!="Y":
        break
   


    
