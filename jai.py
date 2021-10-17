#Assignment0

#Algorithm for finding x and y
# x=int
# y=int
# 10,1,8,3,6,5,4,7,x,y
# Here, 
# nos(10,8,6,4,x) are at odd places 
# here m1=10,m2=8,m3=6,m4=4,m5=x,......,m=(m-1) - 2 #sequence is followed of subtracting 2 from previous no
# since m4=4,m5=(m4 - 2) =(4-2)=2
# Also,
# nos(1,3,5,7,y) are at even places
# here n1=1,n2=3,n3=5,n4=7,n5=y,.....,n=(n-1) + 2 #sequence is being followed of adding 2 with previous no
# since n4=7,n5=(n4 + 2) =(7+2)=9

# x=2,y=9


# "END" IN PRINT FUNCTION
 
 #end the output with @
# print("python", end=' @ ')
# print("MyCaptain") 


#Assignment1.1

    #USE OF OPERATORS- < , <= , > , >= , or , not

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))

# if(a<b):
#     print("b is greater than a")
# else:
#     print("null")

# if(a<=b):
#     print("b is greater or equal to:")
# else:
#     print("zero")

# if(a>b):
#     print("a is greater than b")
# else:
#     print("not given")

# if(a>=b):
#     print("a is greater or equal to b")
# else:
#     print("nil")

# if(a>b or a==b):
#     print("a is either greater or equal to b")
# else:
#     print("b is greater than a")

# if(not a==b):
#     print("a is not equal to b")
# else:
#     print("equal")    

     #SIMPLE CALCULATOR

# menus
# print("Calculator")
# print("1.Add")
# print("2.Substract")
# print("3.Multiply")
# print("4.Divide")

#  input choice
# ch=int(input("Enter Choice(1-4): "))

# if ch==1:
#     a=int(input("Enter A:"))
#     b=int(input("Enter B:"))
#     c=a+b
#     print("Sum= ",c)
# elif ch==2:
#     a=int(input("Enter A:"))
#     b=int(input("Enter B:"))
#     c=a-b
#     print("Difference = ",c)
# elif  ch==3:
#     a=int(input("Enter A:"))
#     b=int(input("Enter B:"))
#     c=a*b
#     print("Product = ",c)
# elif ch==4:
#     a=int(input("Enter A:"))
#     b=int(input("Enter B:"))
#     c=a/b
#     print("Quotient = ",c)
# else:
#     print("Invalid Choice")


#Assignment1.2

    #LISTS METHODS

  #Print list
# list=["A","B","C","D"]
# print(list)
 
  #list[1](INSERT)
# list=["A","B","C","D"]
# print(list[1]) #list can print a particular element with help of index no

  #list (length)
# list=["A","B","C","D"]
# print(len(list)) #length of elements inside list

  #list allows duplicate values
# list=["A","B","C","D"]
# list.append("A")
# print(list)  
 
  #new item can be added in list
# list=["A","B","C","D"]
# list.append("E")
# print(list)

  #list can show changebility
# list=["A","B","C","D"]
# list[1]="J"
# print(list)  

  #copy of list
# list=["A","B","C","D"]
# newlist=list.copy()
# print(newlist)  

  #removing items from list
# list=["A","B","C","D"]
# list.remove("B") 
# print(list) 

  # clearing the list
# list=["A","B","C","D"]
# list.clear() #clearing the list
# print(list)

  #count 
# list=["A","B","C","D","A","A"]
# b=list.count("A")
# print(b)

  #extend
# list=["A","B","C","D"]
# list1=["E","F","G","H"]
# list.extend(list1)
# print(list)
  
  #index
# list=["A","B","C","D"]
# a=list.index("B")
# print(a)  

  #reverse
# list=["A","B","C","D"]
# list.reverse()
# print(list)  

  #sort
# list=[1,7,9,5,4,6]
# list.sort()
# print(list)  

   #STRINGS METHODS

  #capitalize
# string=("hello")
# a=string.capitalize()
# print(a)

  #casefold
# string=("HELLO everyone")
# a=string.casefold()
# print(a)  

  #center
# str=("pleothra")
# a=str.center(85)
# print(a)  
   
  #count
# str=("how are you doing")
# a=str.count("o")
# print(a)  

  #encode
# str=("however")
# a=str.encode()
# print(a)

  #endswith
# str=("hello")
# a=str.endswith("o")
# print(a)  

  #expandtabs
# str=("h\te\tl\tl\to")
# a=str.expandtabs(2)
# print(a)  

  #find
# str=("hello")
# a=str.find("o")
# print(a)  

  #format
# str=("hello {size:.0f} shoes")
# a=str.format(size=7)
# print(a)

  #index
# str=("hello")
# a=str.index("l")
# print(a)
 
  #isalnum
# str=("helo235o")
# a=str.isalnum()
# print(a)  

  #isalpa
# str=("helloA")
# a= str.isalpha()
# print(a) 

  #isdecimal
# str=("uee32")
# a=str.isdecimal()
# print(a)  

  #isdigit
# str=("12345")
# a=str.isdigit()
# print(a)  

  #isidentifier
# str=("abcde")
# a=str.isidentifier()
# print(a)  

  #islower
# str=("hello")
# a=str.islower()
# print(a)  

  #isnumeric
# str=("1234566")
# a=str.isnumeric()
# print(a) 

  #isprintable
# str=("hihello0,.;kjajh")
# a=str.isprintable()
# print(a)  

  #isspace
# str=(" ")
# a=str.isspace()
# print(a)  

  #istitle
# str=("Hello")
# a=str.istitle()
# print(a)  

  #isupper
# str=("HELLO")
# a=str.isupper()
# print(a)  

  #join
# str=("hello","hi","why")
# a=",".join(str)
# print(a)  

  #ljust
# str="apple"
# a=str.ljust(20)
# print(a,"is my fav fruit")  

  #lower
# str=("HELLO")
# a=str.lower()
# print(a)  

  #lstrip
# str="hello"
# a=str.lstrip()
# print(a,"everyone")  

  #maketrans
# str=("hello Joy!")
# a=str.maketrans("J", "R")
# print(str.translate(a))  

  #partition
# str=("hello boys")
# a=str.partition("boys")
# print(a)  

  #replace
# str=("hello")
# a=str.replace("h","j")
# print(a)  

  #rfind
# str=("hello")
# a=str.rfind("l")
# print(a)  

  #rindex
# str=("hello")
# a=str.rindex("e")
# print(a)  

  #rjust
# str=("hello")
# a=str.rjust(20)
# print(a,"everyone")  

  #rpartition
# str=("hello how you")
# a=str.rpartition("how")
# print(a)  

  #rsplit
# str=("hello")
# a=str.rsplit()
# print("evrybody", a ,"how are you")  

  #rstrip
# str=("hello")
# a=str.rstrip()
# print("every",a,"has a meaning")  

  #split
# str=("hello everybody")
# a=str.split()
# print(a)  

  #splitlines
# str=("hello everybody\nThis is python class")
# a=str.splitlines()
# print(a)  

  #startswith
# str=("hello")
# a=str.startswith("h")
# print(a)  

  #strip
# str=("hello how are you")
# a=str.strip()
# print(a,"i am fine")  

  #swapcases
# str=("hellO")
# a=str.swapcase()
# print(a)  

  #title
# str=("hello")
# a=str.title()
# print(a)  

 #upper
# str=("hello")
# a=str.upper()
# print(a) 

  #CALCULATOR USING FUNCTIONS

# def multiplication(num1, num2):
#     return num1 * num2
# def addition(num1, num2):
#     return num1 + num2
# def subtraction(num1, num2):
#     return num1 - num2
# def divide(num1, num2):
#     return num1 / num2
# value1 = int(input("Enter 1st number: "))
# value2 = int(input("Enter 2nd number: "))
# print("Select operation 1-Division, 2-Multiplication, 3-Addition, 4-Subtraction")
# operation = int(input("Choose operation 1/2/3/4: "))
# if operation == 1:
#     print(value1, "/", value2, "=", divide(value1, value2))
# elif operation == 2:
#    print(value1, "*", value2, "=", multiplication(value1, value2))
# elif operation == 3:
#    print(value1, "+", value2, "=", addition(value1, value2))
# elif operation == 4:
#    print(value1, "-", value2, "=", subtraction(value1, value2))
# else:
#    print("Enter correct operation")

              
              


