def add(x, y):
    return "Your answer is " + str(x + y)

def subtract(x, y):
    return "Your answer is " + str(x - y)

def multiply(x, y):
    return "Your answer is " + str(x * y)

def divide(x, y):
    if x == 0 or y == 0:
        diff = "Invalid"
    else:
        diff = x / y
    return "Your answer is " + str(diff)

def add_unbreakable():
    flage = 0
    while flage == 0:
        add_num1 = input("Enter first number for addition>> ")
        add_num2 = input("Enter second number for addition>> ")
        if add_num1.isnumeric() and add_num2.isnumeric():
            print(add(int(add_num1), int(add_num2)))
            flage = 1
        else:
            print("PLEASE ENTER A NUMBER!!")

def sub_unbreakable():
    flage = 0
    while flage == 0:
        sub_num1 = input("Enter first number for subtraction>> ")
        sub_num2 = input("Enter second number for subtraction>> ")
        if sub_num1.isnumeric() and sub_num2.isnumeric():
            print(subtract(int(sub_num1), int(sub_num2)))
            flage = 1
        else:
            print("PLEASE ENTER A NUMBER!!") 

def multi_unbreakable():
    flage = 0
    while flage == 0:
        multi_num1 = input("Enter first number for multiplication>> ")
        multi_num2 = input("Enter second number for multiplication>> ")
        if multi_num1.isnumeric() and multi_num2.isnumeric():
            print(subtract(int(multi_num1), int(multi_num2)))
            flage = 1
        else:
            print("PLEASE ENTER A NUMBER!!") 

def div_unbreakable():
    flage = 0
    while flage == 0:
        div_num1 = input("Enter first number for division>> ")
        div_num2 = input("Enter second number for division>> ")
        if div_num1.isnumeric() and div_num2.isnumeric():
            print(divide(int(div_num1), int(div_num2)))
            flage = 1
        else:
            print("PLEASE ENTER A NUMBER!!") 

if __name__ == '__main__':
    add_unbreakable()
    sub_unbreakable()
    multi_unbreakable()
    div_unbreakable()
    