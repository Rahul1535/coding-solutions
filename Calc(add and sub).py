#python calculator(add and subtract only)
print("choose your option")
print ("add")
print ("sub")
print("quit")
a = input()
if (a == "quit"):
    quit()
elif (a == "add"):
    a= float(input())
    b= float(input())
    c= a+b
    print(c)
elif (a == "sub"):
    a= float(input())
    b= float(input())
    c= a-b
    print(c)
