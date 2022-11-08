#a
import inspect

def multiply_by_two(x):
    return x * 2

def add_numbers(a,b):
    return a + b


def print_arguments(function) :
    return lambda *values : "Arguments are " + str(values) + " and the result is : " + str(function(*values))

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)
print(x)

augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)
print(x)

#b

def multiply_by_three(x ):
    return x * 3

def multiply_output(function) :
    return lambda *args : function(*args) * 2 

augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10) 

print(x)

#c

def add_numbers(a, b):
    return a + b

def augment_function(function,decorators) :
    toDoFunc = function
    for decorator in decorators[1:]:
        aux = toDoFunc
        toDoFunc = lambda *var : decorator(aux(*var)) # it makes sense but doesnt work:(
    toDoFunc = decorators[0](toDoFunc)
    return toDoFunc


decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 
x = decorated_function(3, 4)  
print(x)
