# #Class 1.4                                          #MASS COMMENT: ctrl + /

# x=int(input("Type a number: "))
# if (x<0):
#     print(-x)
#     print("Negative number detected!")
# elif (x>0):                                      #elif bc we want to account for 0
#     print(x)
#     print("Positive number detected!")           #be sure to indent under conditional
# else:
#     print("Zero detected!")

# x=int(input("Type a number: "))
# if 10/x <0:                                       #if false then stops unless there's else/elif
#     print(x)
# if x!=0 and 10/x <0:
#     print (x)
# if x==0:                                          # == when testing equality
#     print("Zero")



# grade = int(input("Grade: "))
# if grade>=85:
#     print("A")
# elif grade>=70:
#     print("B")
# elif grade>=55:
#     print("C")
# else:
#     print("D")



# x= int(input("X= "))
# while x<10:                                 #use while when vague number of iterations
#     print(x)
#     x+=1
# # for i in range(10):                        #use for when more structured
# for i in "cake":
#     print(i)                                #iterates each letter of cake
#
#


# def greeting(name):                         #function (parameter):
#     print("Hello")                          #define function
#     print("Good Morning")
#     print(name)
# greeting("Mariska")                         #uses a function
#
# def echo(message):
#     print(message)
#     print(message)
#     return len(message)
# print(echo("cake"))         #or store in variable and print
#
# def abs(n):
#     if (n<0):
#         return(-n)
#     else:
#         return(n)
#     x= abs(x)
#
#
# def inc():
#     a=a+1                       #scope
# a=5                                  #global
# inc()                                #scope


# def echo(message: str) -> int:            #type hints: msg is a string and going to return int
#     #---if type(message) !=type(""):       #instead...
#     if not isinstance(message,str):
#         print (f"Wrong Type!: {type(message)}")
#         return -1
#     print(message)
#     print(message)
#     return len(message)
#
# a= echo("hi")
# d= echo([1,5,6])        #[list]
# print(d)
# print(type(d))

#___TASK___
# Create a function that generates a UT EID (returned as a string) from initials
# (should be type hints) and a given number.
# Refer to Python doc. to see how to concatenate strings

# def create_uteid (initials: str, num: int) -> str:
#     return initials + str(num)
#
# print (create_uteid("ML", 345))
#
# assert create_uteid("ML",345) == "ML345", "ERROR!"

# def foo(a,b):
#     return a+b, a-b
# foo(3,4)                                #tuples
# sum,diff= foo(3,4)
# print(sum,diff)
#
# range (10)
# print(list(range(10)))                      #range
# for i in range (10):
#     print(i)

# def value_counts(nums):
#     counts={}
#     if nums is not None:
#         for num in nums:
#             #Ternary Equivalent: counts[num]=1 if num not in counts else counts[num] + 1
#             if num not in counts:             #checks if num is already a key (already in list)
#                 counts[num]=1
#             else:
#                 counts[num] += 1
#     return counts

# # define a class
# class Dog:
#     sound = "bark"  # class attribute
#
# # Create an object from the class
# dog1 = Dog()
#
# # Access the class attribute
# print(dog1.sound)
#
# #class
# def Vampire (Monster):                  #class:vampire
#     age= 10                             #inherit from Monster class (has access, reuse code)
#     def get_age(x):
#
# def TeenVampire(Vampire):
#     def smile():

class Monster:
    def __init__(
            self,name, given_age
    ):                                  #Constructor gets called when we "instantiate" an object
        self.name= name
        self.age= given_age
    def speak(self):
        return "Generic Monster Voice"
    def __str__(self):                       #to_string
        return f"{self.name}, {self.age}"

class Vampire(Monster):                          #Inheritance
    def __init__(self, name, age, amt_blood):
        super().__init__(name,age)              #calls superconstructor
        self.amt_blood= amt_blood
    def speak(self):                               #Method overriding - will look for function definition in child
        return "I drink blood."

x= Monster("b", 10)             #parameters of the constructor
y= Monster("a", 15)

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

#Partition (split step):
def partition(arr, low, high):
    pivot = arr[high]            # Pick last element as pivot
    i = low - 1                  # Index for elements < pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]         # Swap
    arr[i+1], arr[high] = arr[high], arr[i+1]        # Place pivot in middle
    return i + 1                 # Return pivot's final position

#Quick Sort (uses partition):
def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)  # Partition step
        quick_sort(arr, low, pivot_idx-1)      # Sort left
        quick_sort(arr, pivot_idx+1, high)     # Sort right






