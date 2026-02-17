text = "banana"

result = ""

for ch in text:
    if ch not in "aeiou":
        result += ch

final = result + result[::-1]

print(final)

text = "programming"

result = ""

for ch in text:
    if ch not in "aeiou":
        result += ch

reversed_text = result[::-1]#gnmmrgrp

fainal = reversed_text[1:-1]#nmmrgr

print(final)