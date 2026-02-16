#for文、リスト応用ループ   ⓵ 偶数のみ合計を出力

numbers = [1, 2, 3, 4, 5, 6] 
total = 0

for num in numbers:
    if num % 2 == 0:
        total += num
print(total)

#⓶ 最大値を求めよ

numbers = [8, 3, 15, 1, 9]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
       
print(max_num)

#⓷　奇数だけ表示

numbers = [1, 2, 3, 4, 5, 6, 7]

for num in numbers:
    if num % 2 != 0:
        print(num)

#range()とインデックス操作 ⓵

numbers = [5, 10, 15, 20]

for i in range(len(numbers)):
    print(numbers[i])

#⓶インデックスも表示

numbers = [5, 10, 15, 20]

for i in range(len(numbers)):
    print(i, numbers[i])

#⓷リストを書き換える

numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    if numbers[i] * 2: #numbers[i] = numbers[i] * 2
        print(numbers[i]) #print(numbers)

#⓷正解
numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)