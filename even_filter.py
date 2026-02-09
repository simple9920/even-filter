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

while num <= 30:
    if num % 2 == 0 and num >= start:
        result.append(num)
    num += 1

print(result)
