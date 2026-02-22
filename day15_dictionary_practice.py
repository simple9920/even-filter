#文字列・ループ・条件
#1 step1
text = "apple,banana,avocado,grape,apricot"
words = text.split(",")
print(words)
#step2
text = "apple,banana,avocado,grape,apricot"
words = text.split(",")
for word in words:
 print(word)
#step3
text = "apple,banana,avocado,grape,apricot"
words = text.split(",")
word[0]
for word in words:
     if word[0] in "a" :
        words.append(word)
print(word)
#答え
text = "apple,banana,avocado,grape,apricot"
words = text.split(",")
a_words = []
for word in words:
     if word[0] == "a" :
        a_words.append(word)
print(a_words)
#発展1
text = "apple,banana,avocado,grape,apricot"
words = text.split(",")
a_words = []
b_words = []
count = 0
for word in words:
     if word[0] == "a" :
        a_words.append(word)
for b_words in len(a_words):
    if b_words + 0:
        count += 1

print(b_words)