word = input()
word_list = list(map(ord, list(word)))
up, down = 0, 0
for c in word_list:
    if c < 97:
        up+=1
    else:
        down+=1    
print(word.upper()) if up>down else print(word.lower())

# Time: +/- 5 min
# Reg number: 1822082023
# Problem url: <http://codeforces.com/contest/59/problem/A>

