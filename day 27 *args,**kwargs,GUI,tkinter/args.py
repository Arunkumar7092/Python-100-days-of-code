def add(*args):
    print(type(args))
    sum = 0
    for each in args:
        sum += each
    return sum

def calculate(*args):
    sum = 0
    for n in range(0,len(args)):
        sum += args[n]
    return sum


print(add(1, 2, 4, 67, 45, 78, 87, 54))
print(calculate(1, 2, 4, 67, 45, 78, 87, 54))