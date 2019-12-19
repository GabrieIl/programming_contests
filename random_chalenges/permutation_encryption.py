input_data=list()
while True:
    secret_key=list(map(int, input().split()))
    if secret_key[0]==0:
        break
    message=list(input())
    input_data.append([secret_key, message])


output_data=list()
for item in input_data:
    key=item[0]
    real_message=item[1]

    while len(real_message)%key[0]!=0:
        real_message.append(' ')

    def slice(real_message, size_cut=key.pop(0)):
        for i in range(0, len(real_message), size_cut):
            yield real_message[i: i+size_cut]

    key_index=[i-1 for i in key]
    encrypt_message=list()
    for part in list(slice(real_message)):
        for i in range(len(part)):
            encrypt_message.append(part[key_index[i]])
    
    print(f"'{''.join(encrypt_message)}'")
    #output_data.append(''.join(encrypt_message))

# Time: +/- 2h
# Reg number: 1822082023
# Problem url: <https://open.kattis.com/problems/permutationencryption>
