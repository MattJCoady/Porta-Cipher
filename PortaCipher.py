table =[['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'],
['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'n', 'm', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'],
['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'l', 'm', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'],
['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'k', 'l', 'm', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'j', 'k', 'l', 'm', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
['s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 'i', 'j', 'k', 'l', 'm', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
['t', 'u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 'h', 'i', 'j', 'k', 'l', 'm', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],
['u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a', 'b', 'c', 'd', 'e', 'f'],
['v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a', 'b', 'c', 'd', 'e'],
['w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a', 'b', 'c', 'd'],
['x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a', 'b', 'c'],
['y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a', 'b'],
['z', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a']]


#Get the message

message = input('Enter the message')

message = message.lower()

messL = []

encrypted_message = []

for i in message:
    
    if i.isalpha() or i.isspace():
        
        messL.append(i)
        
 #Get a valid key

while True:
    
    key = input('Enter the key')

    key = key.lower()

    keyL = []
    
    valid_key = True

    for i in key:
        
        if i.isalpha():
            
            keyL.append(i)
        
        else:
            
            print('Please enter a valid key')
            
            valid_key = False
            
            break

    if valid_key == True:
        
        break
    
#Repeat the key over the length of messL

keyL2 = []

for i in range(len(messL)):
    
    keyL2.append(keyL[i % len(keyL)])


#Convert values in lists into unicode

for char in range(len(messL)):
        
    uni = ord(messL[char])
        
    messL[char] = uni
    
for char in range(len(keyL2)):
        
    uni2 = ord(keyL2[char])
        
    keyL2[char] = uni2
        
# Convert to the encrypted message

keyL2_index = 0

for char in messL:
    
    if char == 32:
        
        encrypted_message.append(' ')
    
    else:
        
        col_index = (keyL2[keyL2_index] - ord('a')) //2
            
        row_index = char - ord('a')
            
        encrypted_char = table[col_index][row_index]
            
        encrypted_message.append(encrypted_char)

        keyL2_index += 1
    
    if keyL2_index == len(keyL2):
        
        break

# Convert the list of encrypted characters back to a string

encrypted_message = ''.join(encrypted_message)

print("Encrypted Message is", encrypted_message)
