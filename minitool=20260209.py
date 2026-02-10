result = []
num = 0

while num < 30:
    if num % 2 == 0 and num > 10:
        result.append(num)
    num += 1

print(result)