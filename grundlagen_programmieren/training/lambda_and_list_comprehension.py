import random
import string
import time

class Clock():
    def __init__(self):
        self.start_time = None 

    def tic(self):
        self.start_time = time.time()

    def toc(self):
        if self.start_time != None:
            print(f"{time.time() - self.start_time} seconds")
        self.start_time = None

c = Clock()

c.tic()

print("Task 1")
l1 = [x for x in range(0,100)]
print([x for x in l1 if x % 2 == 0] + [x for x in l1 if x % 2 != 0])

print("Task 2")
print([i for i in range(5,100,10)])

print("Task 3")
print([random.randint(0,1000) for _ in range(1000)])

print("Task 4")
print({letter:ord(letter) for letter in string.ascii_lowercase})

print("Task 5")
class Person():
    pass

print([Person() for _ in range(100)])

c.toc()
print("--------------------------------------------------")

print("Task: remove all odd numbers")
print([x for x in range(100) if x%2==0])

print("Task: Find all numbers from 1-1000 that are divisible by 7")
print([x for x in range(1, 1000) if x%7==0])

print("Task: Find all numbers from 1-1000 that contain a 3")
print([x for x in range(1, 1000) if str(x).find("3") >= 0])

print("Task: Count the numbers of spaces in a string")
sample = "   test   test " 
print(len([x for x in sample if x == " "]))

print("Task: Create a list of all the consonants in the string '")
sample = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
consonants = ["a", "e", "u", "o", "i"]
print([x for x in sample if x in consonants])

print("Task: Get the index and the value as a tuple for items in the list . Result would look like (index, value), (index, value)")
sample = ["hi", 4, 8.99, 'apple', ('t,b','n')]
print([(x,y) for x,y in enumerate(sample)])

print("Task: Find the common numbers in two lists (without using a tuple or set)")
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
print([x for x in list_a if x in list_b])

print("Task: Get only the numbers in a sentence like")
sample = "In 1984 there were 13 instances of a protest with over 1000 people attending"
print([x for x in sample.split(" ") if x.isnumeric()])

print("Task: Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’")
print(["even" if x%2==0 else "odd" for x in range(20)])

print("Task: Produce a list of tuples consisting of only the matching numbers in these lists Result would look like (4,4), (12,12)")
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
list_b = [2, 7, 1, 12] 
print([(x,x) for x in list_a if x in list_b])

print("Task: Find all of the words in a string that are less than 4 letters")
sample = "Find all of the words in a string that are less than 4 letters"
print([x for x in sample.split(" ") if len(x) < 4])

print("Task: Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)")
print([x for x in range(1, 100) if not any([x%y == 0 for y in range(2,10)])])
