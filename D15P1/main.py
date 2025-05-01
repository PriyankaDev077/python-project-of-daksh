
try :
    num = int(input("enter your number :"))
    print(num)
except ValueError as ex:
    print("Exception: ",ex)


    print("i am outside the try block")
    