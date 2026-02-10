result = []
for num in range(31):
    if (num % 5 == 0 or num % 2 == 0) and num < 15:
        result.append(num)
print(result)