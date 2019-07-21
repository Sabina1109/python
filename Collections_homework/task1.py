# FizzBuzz:
#  При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»,
#  а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5,
#  то программа должна выводить слово «FizzBuzz».
for x in range(1, 100):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)
