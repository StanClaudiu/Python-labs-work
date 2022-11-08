#a
import inspect

def multiply_by_two(x):
    return x * 2

def add_numbers(a,b):
    return a + b


def print_arguments(function) :
    return lambda *values : "Arguments are " + str(values) + " and the result is : " + str(function(values))
    # IDK here how to give them as parameters to the function

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10,20)
print(x)

#b
def multiply_by_three(x):
    return x * 3

def multiply_output(function) :
    return lambda *args : function(args) * 2 # here I still dk



