"""
Reference: https://www.youtube.com/watch?v=8hWIWyBfdQE&list=PL98qAXLA6afuh50qD2MdAj3ofYjZR_Phn

"""


def display_info(func):
    def inner():
        print("Exercuting:",func.__name__,"function")
        func()
        print("Finished execution")
    return inner

@display_info
def printer():
    print("Hello world")

printer()


def smart_divide(func):
    def inner(a,b):
        print("dividing",a,'by',b)
        if b==0:
            print('cannot divide by 0!')
            return
        else:
            return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b

divide(15,3)
divide(0,1)
divide(1,0)
