import random
nom = random.randint(-1000, 1000)
val = float(input(f"{nom} / "))
try: 
    print(f"{nom} / {val} = {nom/val}")
except ZeroDivisionError:
    print("you are trying to divide by zero")
except ValueError:
    print("you are trying to divide by a string")
print("done")
