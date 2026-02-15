#判定と計算をわけれるか

def get_number():
    while True:
        try:
            num = int(input("数字を入力してください："))
            return num
        except ValueError:
            print("数字以外を入力しないでください：")

def is_pass(num):
    return num > 9

num = get_number()

if is_pass(num):
    print("合格")
else:
    print("不合格")



