# print("hello")
# name = input("Enter your name  ")
# print(f"Hello {name}")

#conditions
# n = int(input("Number: "))
# if n > 0:
#     print("n is positive")
# elif n < 0:
#     print("n is negative")
# else:
#     print("n is zero")


#sequences
# name = "Mohamed"
# print(name[0])
# print(name[0:3])

# names = ["mohamed","Ali","hassan"]
# print(names[1])
# coordinate = (10.0,30.0)

# list - Sequence of mutable values
# tuple - sequence of unmutable values
# set - collection of unique values
# dict - collection of key-value pairs

#lists
# names = ["mohamed","Ali","hassan"]
# print(names)
# print(names[2])

# names.append("Faarah")
# names.sort()
# print(names)


#sets
# s = set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(5)
# print(s)
# s.remove(2)
# print(s)

# print(f"the set has {len(s)} elements")



#loops
# for i in [1,2,3,4,5,6]:
#     print(i)

# name = "Mohamed"
# for charator in name:
#     print(charator)



#dectionary

# housee = {"mohamed": "105", "Hassan":"120" }
# print(housee["mohamed"])

#functions 
# def square(x):
   
#     return  x*x


# for i in range(10):
#     print(f"the  of {i} is {square(i)}")

#classes
# class point():
#     def __init__(self,input1,input2):
#         self.x = input1
#         self.y = input2

# p = point(3,2)
# print(p.x)
# print(p.y)

# class flight():
#     def __init__(self,capacity) :
#         self.capacity = capacity
#         self.passengers = []
#     def add_passengers(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True
#     def open_seats(self):
#         return self.capacity - len(self.passengers)
        
# flight = flight(3)
# people = ["Ali","hassan","Abdi","mohamed"]
# for person in people:
#     success =  flight.add_passengers(person)
#     if success:
#         print(f"Added {person} to flight successfuly.")
#     else:
#         print(f"No available seats for {person}")



#decorators
# def announce(f):
#     def wrapper():
#         print("about the run function")
#         f()
#         print("Done with the function")
#     return wrapper
# @announce
# def hello():
#     print("hello world")
# hello()


#lambda
# people = [
#     {"a":"c","l":"g"},
#     {"t":"e","b":"s"},
#     {"x":"m","d":"y"}
# ]


# people.sort(key=lambda person : person["a"] )
# print(people)

# #exception
# import sys
# n1 = int(input("num1: "))
# n2 = int(input("num2: "))
# try:
        
#     result = n1/n2
#     print(f"{n1} / {n2} = {result}")
# except ZeroDivisionError:
#     print("Error connot  divide by 0")
    
