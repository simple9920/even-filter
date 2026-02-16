#問題1 偶数だけ3倍

numbers = [3, 7, 2, 9, 4]

for i in range(len(numbers)):
    if numbers[i] % 2 ==0:
        numbers[i] = numbers[i] * 3

print(numbers)

