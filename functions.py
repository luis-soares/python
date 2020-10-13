import random
import sys


num = 0

def test1():
    global num
    num += 1
    

def print_test1():
    print ('only to test functions and global vars')
    print ('this function was exec', num)


def hello(name):
    print('Hello', end=' ') #only test function end from print
    print (name)

hello('Luis')
hello('Fla')
test1()
print_test1()
test1()
print_test1()
test1()
print_test1()
test1()
print_test1()

sys.exit()

print ('test')