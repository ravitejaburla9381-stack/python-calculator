def calculator():
  try:
    x=float(input("enter the first number:"))
    y=float(input("enter the second number"))
    choose=input("choose the operation(+,-,/,*):")
    z=0
    if (choose=="+"):
      
        z=x+y
        print("sum of the numbers is:",z)
     
    elif(choose=="-"):
          
             z=x-y
             print("subtraction of the numbers is:",z)

    elif(choose=="*"):
            
               z=x*y
               print("multiplication of the numbers is:",z)
             
    elif(choose=="/"):
               
               z=x/y
               print("division of the numbers is:",z)
               
    else: 
       print("enter a valid operator")
  except ValueError:
    print("enter a vaild value")
  except ZeroDivisionError:
    print("zero is not divisiable")
while True:                 
  calculator()
   choice=input("do you want to continue? (yes or no):")
    if choice.lower()!="yes" :
        break
              
