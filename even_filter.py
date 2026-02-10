result = []

for num in range(21):
    if num % 3 == 0 or num >= 10:
        result.append(num)

print(result)

num = 0
while num < 10:
    if num % 3 == 0:
        print(num)
    num += 1

# 指定した数字以上の偶数を抽出するプログラム

result = []
num = 0

start = int(input("基準の数字を入力してください: "))

# 偶数かつ10以下の数を抽出する
while num <= 30:
    if num % 2 == 0 and num >= start:
        result.append(num)
    num += 1

print(result)

result = []
num = 0
while num <= 50:
    #is_even = num % 2 == 0
    #is_over_10 = num >= 10
    #is_not_multiple_of_4 = num % 4 != 0
    #if is_ever and is_over_10 and is_not_multiple_of_4:
    if num % 2 == 0 and num >= 10 and num % 4 != 0:
        result.append(num)
    num += 1
print(result)