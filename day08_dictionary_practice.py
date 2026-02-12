#辞書
book = {
    "title" : "python入門",
    "price" : 3000,
    "author" : "Tanaka"
}
book["price"] = 2000

for key in book:
    print(key, book[key])

#条件判定
book = {
    "title" : "python入門",
    "price" : 3000,
    "author" : "Tanaka"
}
book["price"] = 2000

for key in book:
    if book["price"] >= 2500:
        print("高い")
    else:
        print("安い")

#next
books = [
    {"title": "A", "price": 3000},
    {"title": "B", "price": 2000},
    {"title": "C", "price": 4000}
]

for book in books:
    if book["price"] >= 2500:
        print(book["title"], book["price"])

#合計金額
books = [
    {"title": "A", "price": 3000},
    {"title": "B", "price": 2000},
    {"title": "C", "price": 4000}
]
total = 0

for book in books:
    if book["price"] >= 2500:
        total += book["price"]

print(total)

#締め
books = [
    {"title": "A", "price": 3000},
    {"title": "B", "price": 2000},
    {"title": "C", "price": 4000}
]

result = []

for book in books:
    if book["price"] >= 2500:
        result += book["title"]
        #result.append(bookp["title"])
        # #文字なので+=はおかしい     
    
print(result)