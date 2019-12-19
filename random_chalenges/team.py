amount = int(input())
ans=0
for i in range(amount): 
    ans+=1 if list(map(int, input().split())).count(1)>=2
print(ans)

# Time: +/- 4 min
# Reg number: 1822082023
# Problem url: <http://codeforces.com/contest/231/problem/A>

