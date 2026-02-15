#復元テスト

def get_number():
    while True:
        try:
            num = int(input("数字を入力してください："))
            return num
        except ValueError:
            print("数字以外を入力しないでください。")
    
def judge_number(num):
    return num % 2 == 0


num = get_number()


if judge_number(num):
    print("正の数です")
else:
    print("負の数です")

#正解

def get_number():
    while True:
        try:
            num = int(input("数字を入力してください："))
            return num
        except ValueError:
            print("数字以外を入力しないでください。")
    
def judge_number(num):
    if num > 0:
        return "正の数です"
    elif num == 0:
        return "ゼロです"
    else:
        return "負の数です"

num = get_number()
print(judge_number(num))
