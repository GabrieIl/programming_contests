qtd = int(input())
dominos = input()
l = dominos.count('L')
r = dominos.count('R')
ponto = dominos.count('.')

if r==0 and l==0:
    print(ponto)
    
elif r==1 or l==1:
    if r==1:
        print(len(dominos.split('R')[0]))
    else:
        print(len(dominos.split('L')[1]))

else:
    if l < r:
        print(l*2)
    else:
        print(r*2)

