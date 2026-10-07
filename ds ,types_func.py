def even_finder(n):
  if n%2 == 0:
      print('even number')
  else:
      print('odd number')

even_finder(10)

even_finder(3)

def largest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print(largest_number(a, b, c), "is the largest")

#largest of 3

def number_finder(n):
  if n <=0:
    print('zero')
  elif n >0:
    print('greater than zero')
  else:
   print('leass than zero') # less than zero or + or -

  number_finder(34)

def sum_finder(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_finder(5))
  # sum finder for 3 numbers


def square(number):
  print('print before')
  if number% 2 == 0:
    return number * number
  print('after return')
  """ bascially to prove that after return function is used
  we either need to write another code or new condition otherwise it will break the code """

square(20)

square(17)

def calculate(a,b):
  return a+b ,a-b, a*b


totat ,differnce ,product = calculate(10,4)
print(totat ,differnce ,product)
#this is prove that the values can be stored in 3 varinets
 # like above  with different operations

def total(*args):
    return sum(args)

print(total(10,20))

print(total(10,20,30,40)) # basically the function of "(*args)" is total up in tuple list format

def show_student(**kwargs):
  for key, value in kwargs.items():
    print(key , ":", value)
# basically k=(**kwars is used to add into dictonary)

show_student(name ='anu',age =20 , mark=22)

def demo(*args, **kwargs):
  print(args)
  print(kwargs)

demo(10,20 , name= 'anu', age =22) # we can also add up args and kwargs togather to add and make it into a sum

def greet (name, message= ' HI How are you'):
    print(message , name)

greet("anu")

greet("anu ", "Good mroning")

def countdown(n):
  if n == 0:
    print("Done")
    return

  print(n)
  countdown(n-1)# recurssion function  here we can call the same fucntion inside
  # another fucntion 


countdown(10)

#factorial using 2 fucntions 
def factorial(n):
  if n ==0 or n==1 :
      return 1
  return n* factorial (n-1)



factorial(5)

#lambda function 
# normal sqaure fucntion 
""" normal-
def square(x):
  retyrn x * x
but in lambda we write like"""

sqaure_lambda = lambda x: x*x
print(sqaure_lambda(5))
#

# doubling a digit
double=lambda x: x*2
print(double(5))

# Multiple parameters
add = lambda a, b: a + b
print(add(10, 20))


# No parameters
message = lambda: "Hello"
print(message())

check = lambda x : "even" if x % 2 ==0 else  "odd"
print(check(8))