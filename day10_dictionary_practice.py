#関数
def double_input():
    while True:
        try:
            num = int(input("数字を入力してください；"))
            return num * 2
        except ValueError:
            print("数字以外はダメ！もう一度。")

result = double_input()
print("結果は", result)

#計算専用関数
def multiply(num, base):
    return num * base

#チャレンジ
def double_input():
    #掛け算なのでsafe_multiplyが適切
    while True:
        try:
            num = int(input("数字を入力してください："))
            base = int(input("倍数は？："))
            return num * base
        except ValueError:
            print("数字以外はダメ！もう一度。")

result = double_input()
print("結果は", result)

#単一責任

def get_number():
    while True:
        try:
            num1 = int(input("数字を入力してください：")) #num = int(input("数字を入力してください："))
            num2 = int(input("倍数は？：")) #なし
            return  #return num
        except ValueError:
            print("数字以外はだめ！もう一度。")

def multiply(num1, num2):
    while True: #ここにwhileはいらない　計算のみなのでエラー処理は不要
            return num1 * num2

num1 = get_number()#呼び出し1
num2 = get_number()#呼び出し2

result = multiply(num1, num2)
print("結果は", result)

#完成計

def get_number():
    while True:
        try:
            num = int(input("数字を入力してください："))
            return num
        except ValueError:
            print("数字以外はだめ！もう一度。")

def multiply(num1, num2):
    return num1 * num2

num1 = get_number()
num2 = get_number()

result = multiply(num1, num2)
print("結果は", result)
