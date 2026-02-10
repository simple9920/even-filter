result = []
for num in range(31):
    if num % 4 == 0 and num >= 10:
        result.append(num)
print(result)