#宣告空串列
#text = input('請輸入一串英文')
text = 'abcabcbb'
repeat = []
not_repeat = []



words = []
for i in range(3):
    for j in range(0,len(text)-i,1):
        endIndex = j + i + 1
        words.append(text[j:endIndex])
print("字串分組")
print(words)


for i in words:
    a = text.count(i,0,len(words))
    if a > 1 and i not in repeat:
        repeat.append(i)
    if a == 1 and i not in not_repeat:
        not_repeat.append(i)
print("重複字串")
print(repeat)
print("不重複字串")
print(not_repeat)


"""
輸入:
abcabcbb

輸出結果:

重複字串
['a', 'b', 'c', 'ab', 'bc', 'abc']
不重複字串
['ca', 'cb', 'bb', 'bca', 'cab', 'bcb', 'cbb']

"""
