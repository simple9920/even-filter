def multiple_of_five():
    result = []
    for num in range(51):
        if num % 5 == 0:
            result.append(num)
    return result

print(multiple_of_five())

#引数
def multiple_of_five(limit):
    result = []
    for num in range(limit + 1):
        if num % 5 == 0:
            result.append(num)
    return result

print(multiple_of_five(50))
print(multiple_of_five(30))
    
#何の倍数
def multiple(limit, base):
    result = []
    for num in range(limit + 1):
        if num % base == 0:
            result.append(num)
    return result
print(multiple(50, 5))
print(multiple(30, 3))

#limit, base , min_value
def multiple(limit, base, min_value):
    result = []
    for num in range(limit + 1):
        if num % base == 0 and num >= min_value:
            result.append(num)
    return result

print(multiple(50, 5, 10))