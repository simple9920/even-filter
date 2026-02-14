def triple(num):
    return num * 3

print(triple(3))
print(triple(5))

#単一責任 問題1

def get_number():
    while True:
        try:
            price = int(input("価格を入力してください："))
            return price
        except: #ValueError 忘れないように
            print("数字のみ")

def add_tax(price1, price2, tax):# price1 price2ではなくpriceのみ意味が崩れる　taxは税率変わる可能性が有る為、実務的には入れる、今回は抜く def add_tax(price)
    #tax = 0.1
    return price1 + price2 * tax #同じく return price + price * tax

price1 = get_number #同じく　price = get_number
price2 = get_number #必要ない
tax = 0.1 #add_tax元に入れる 計算担当なので入れて問題ない

total = add_tax(price1, price2, tax) #priceのみ
print("税込価格は", total)

#答え

def get_number():
    while True:
        try:
            price = int(input("価格を入力してください："))
            return price
        except ValueError:
            print("数字のみ入力してください")

def add_tax(price):
    tax = 0.1
    return price + price * tax

price = get_number()
total = add_tax(price)

print("税込価格は", total)

#問題2

def get_number():
    while True:
        try:
            num = int(input("数字を入力してください："))
            return num
        except ValueError:
            print("数字のみ入力してください")

def is_even(num):
    return num % 2 == 0

num = get_number()

if is_even(num):
    print("偶数です。")
else:
    print("奇数です。")
