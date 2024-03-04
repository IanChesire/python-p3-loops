def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("Happy New Year!")
happy_new_year()


def square_intergers(numbers):
    interger_list = [nums ** 2 for nums in numbers]
    return interger_list
print(square_intergers([4, 10, 30, 13, 500]))

def fizzbuzz():
    for nums in range(1, 101):
        if(nums % 3 == 0 and nums % 5 == 0 ):
            print("FizzBuzz")
        elif nums % 3 == 0:
            print("Fizz")
        elif nums % 5 == 0:
            print ("Buzz")
        else:
            print (nums)

fizzbuzz()