
'''
while True:
    a=int(input())
    if a==0:
        break
    print(chr(a))
'''
'''

a=input()
if len(a)>10:
    print('строка длиннее десяти символов')
for i in range(len(a),10):
    a+='*'
    print(a)
'''
C_words=[]
with open('zen.txt','r') as f:
    word=f.read().split()
    print(word)
    for i in word:
        print(i)
        if 'c' in i or 'C' in i:
            C_words.append(i)
print(C_words)
