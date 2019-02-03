q = int(0)
num = int(0)
n = int(input('Quantity of strings: '))
for num in range(n):
    print('Enter', (num+1),'string:')
    str = input()
    ListOfWords = str.split()
    for i in range(len(ListOfWords)):
        if len(ListOfWords[i]) > q:
            q = len(ListOfWords[i])
            longest = ListOfWords[i]
    print()
print('The longest word is: ' + longest)


















"""
    q = int(0)
    t = str()
    s = []
    n = int(input('Enter a number of length'))
    for i in range(0, n):
        s.append(input())
    t = s.split()
    print()
    for i in range(len(t)):
        if len(t[i]) > q:
            q = len(t[i])
            print(t[i])
"""





"""
    a= open('input.txt','r')
    r = open('output.txt','w')
    t=a.read().split()                  # разбиваем строку на слова
    q=0                                 # число символов (в слове)
    w=0                                 # слово
    for i in range(len(t)):
        if len(t[i])>q:
            q= len(t[i])
            w= t[i]
    print(w, file = r)                   # запись в файл r строки w
    a.close()
    r.close()
"""