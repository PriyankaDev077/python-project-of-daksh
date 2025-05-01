def employee(name):
    print(name)

def salary(exp):
    if exp>=5:
        return 3000000
    elif exp>=3:
        return 1000000
    else:
        return 5000000
employee("Ram")
a = salary(15)
print("the salary of the employee is",a)

                