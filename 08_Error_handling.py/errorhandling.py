#error handling or exception handling
#control over the error in programs

#error in program

#solution
try:
    print(x)
except NameError:
    print("x is not defined") 
#Error 5
amount = 500 
email = "p@mail.com"
#total = amount+email
try:
    total = amount +email
except TypeError:
    print("this error is data type error")
       