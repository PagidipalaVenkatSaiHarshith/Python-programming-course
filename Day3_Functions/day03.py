# -*- coding: utf-8 -*-
"""Day03.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1erxUBjX4ywftj_A5jcwegNxT9iRcaC7y
"""

def function_name():
    # Do something here

# create function to hello world
def hello_world():
  print("hello")
  print("class")

hello_world()

def repitative_task():
  pass
  #steps which are recurring

repitative_task()

#addition of two numbers
#passing the parameters to a function
def addition(a,b):
  print(a+b)

addition(2,5)

def greet(name):
    print("Hello, " + name + "!")

greet("Suresh")

#addition of numbers
def addi(a,b):
  return a+b

c=addi(2,5)

print(c)

def addi(a=0,b=0):
  return a+b

addi()

list_numbers = [1,2,3,4,5,6,7]

def addition_list(l):#l is a list of number
  s = 1
  for i in l:
    print("i is ",i)
    print("old s is ",s)
    s = s*i
    print("new s is ",s)
  print("total is ",s)

addition_list(list_numbers)

"""
1st time the of s is 0 and i is 1, the new s value is 0+1=1
2nd time the value of s is 1 and i is 2, the new s value is 1+2=3

def greet(name):
    print("Hello, " + name + "!")

greet("Madhavi")

def add_numbers(num1, num2):
    return num1 + num2


result = add_numbers(7, 8)
print(result)

#Write a function that takes three numbers and returns the largest one.
def largest(num1,num2,num3):
  if num1>num2:# comparing num1 and num2 and find bigger one of those both
    if num1>num3:# comparing the bigger one with num3
      return num1
    else:
      return num3
  else:
    if num2>num3:
      return num2
    else:
      return num3

bignum = largest(3,2,5)

print(bignum)