width, partitions = map(int, input().split())
div = list(map(int, input().split()))

width = [i+1 for i in range(width)]
div_rooms = list()
for i in range(len(div)):
    if i == 0:
        div_rooms.append(width[:width[div[i]-1]])
        if i+1 == len(div):
            div_rooms.append(width[div[i]:])

    else:
        div_rooms.append(width[width[div[i-1]-1]:width[div[i]-1]])
        if i+1 == len(div):
            div_rooms.append(width[div[i]:])

size_rooms = [len(i) for i in div_rooms]
spaces = set()

for i in range(len(size_rooms)):
    if size_rooms[i] != 0:
        spaces.add(size_rooms[i])
    
    for k in range(len(size_rooms)):
        if sum(size_rooms[i:k+1]) != 0:
            spaces.add(sum(size_rooms[i:k+1]))

print(' '.join(map(str, sorted(spaces))))

# Time: 20 min (fisrt time) + 10 min (fix issues)
# Reg number: 1822082023
# Problem url: <https://open.kattis.com/problems/flexible>


