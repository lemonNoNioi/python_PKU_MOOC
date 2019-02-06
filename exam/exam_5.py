cipher_text = input()
last = cipher_text[-1]
distance = ord('E') - ord(last)
clear_text = ''

for c in cipher_text:
    ordc = ord(c)+distance
    if ordc > 90:
        ordc -= 26
    elif ordc < 65:
        ordc += 26
    clear_text += chr(ordc)

print(clear_text)
