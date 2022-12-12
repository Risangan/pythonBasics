def sayhi(name, age):
    print("Hello " + name + ", you are " + str(age))


def cube(num1):
    return num1 * num1 * num1


def check_is_male(is_male, is_tall):
    if is_male and is_tall:
        print("You are a tall male")
    elif is_male and not is_tall:
        print("You are a short male")
    elif not is_male and is_tall:
        print("You are not a male but you are tall")
    else:
        print("You are not a male and not tall")


def maxNum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num2
    else:
        return num3


userName = input("What is your name? ")
sayhi(userName, 20)
sayhi("no name", "35")
print(cube(2))
is_male_val = True
is_tall_val = True
check_is_male(is_male_val, is_tall_val)
check_is_male(False, True)
print(maxNum(1, 2, 3))
