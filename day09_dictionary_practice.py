#例外処理
try:
    #エラーが起きる可能性がある処理
    num = int(input("数字を入力"))
    print("2倍は", num * 2)
except:
    #エラーが起きた時の処理(なんでも捕まえる)
    print("数字を入力してください")

#レベルアップ版
try:
    num = int(input("数字を入力"))
    print("2倍は", num * 2)
except ValueError:
    #exceptのみだと全部のエラーを捕まえるが、ValueErrorなら数字変換のエラーのみ捕まえる(特定のエラーのみ)
    print("数字以外はダメ！")

#正しく入力されるまで繰り返す
while True:
    try:
        num = int(input("数字を入力してください:"))
        print("2倍は", num * 2)
        break
    except ValueError:
        print("数字以外はダメ！もう一度。")