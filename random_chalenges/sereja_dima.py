num = int(input())
cards = list(map(int, input().split()))
sereja, dima = 0, 0
 
while len(cards)>0:
    if cards[len(cards)-1]>cards[0]:
        sereja+=cards.pop()
        
        if len(cards)>0 and cards[len(cards)-1]>cards[0]:
            dima+=cards.pop()
        elif len(cards)>0:
            dima+=cards.pop(0)

    else:
        sereja+=cards.pop(0)
    
        if len(cards)>0 and cards[len(cards)-1]>cards[0]:
            dima+=cards.pop()
        elif len(cards)>0:
            dima+=cards.pop(0)

print(sereja, dima)

# Time: 25 min
# Reg number: 1822082023
# Problem url: <http://codeforces.com/contest/381/problem/A>

