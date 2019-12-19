from math import sqrt

amount=int(input())

for c in range(amount):
    message=list(input())
    while int(sqrt(len(message)))**2 != len(message):
        message.append('*')

    size=len(message)
    def matrix(message, size_cut=int(sqrt(size))):
        for i in range(0, size, size_cut):
            yield message[i: i+size_cut]

    reverse_matrix=list(matrix(message))[::-1]
    re_size=len(reverse_matrix)
    for i in range(re_size):
        for j in range(re_size):
            if reverse_matrix[j][i] != '*':
                print(reverse_matrix[j][i], end='')

    print()

# Time: 40 min
# Reg number: 1822082023
# Problem url: <https://open.kattis.com/problems/secretmessage>

