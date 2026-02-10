result = []
for num in range(21):
    if not(num % 2 == 0 or num % 3 == 0):
        result.append(num)
print(result)