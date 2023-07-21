def inner_func(a, b):
    def outer_func(a,b):
        addition = a + b
        return addition
    addition = outer_func(a, b)
    return addition + 5
add = inner_func(10,20)
print(add)