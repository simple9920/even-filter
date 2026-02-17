#文字列xループxカウント

text = "programming"

count = 0

for ch in text:
    if ch == "g":
        count += 1

print(count)

#母音を数える

text = "engineering"

count = 0

for ch in text:
    if ch in "aeiou": #if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        count += 1

print(count)