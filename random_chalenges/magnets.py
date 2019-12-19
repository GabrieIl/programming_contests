amount = int(input())
seq = list()
for i in range(amount):
    seq.append(input())
    
k=0
groups = list(''.join(seq))
for i in range(len(groups)-1):
    if groups[i] == groups[i+1]:
        k+=1
print(k+1)

# Time: +/- 5 min
# Reg number: 1822082023
# Problem url: <http://codeforces.com/contest/344/problem/A>

