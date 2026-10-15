import random as rnd
from sage.all import *
import base64



#arxeio tou kosta
with open("kostas.bin", "rb") as bits:
    data = bits.read()


codeword2 = ''.join(format(b, '08b') for b in data) #from bytes to bits




#13811
#21000
#codeword = ("0011")
#codeword2 = ("0101010011011011")*5 #τιμη για δοκιμες


original_length = len(codeword2)
codeword = codeword2




while len(codeword) % 4 != 0:     # padding
          codeword += "0"

chunks = [codeword[i:i+4] for i in range(0, len(codeword), 4)]   # split into chunks of 4
          
M = GF(2)


G = matrix(M, [                # generator matrix
          [1,0,0,0,1,1,0,1],
          [0,1,0,0,1,0,1,1],
          [0,0,1,0,0,1,1,1],
          [0,0,0,1,1,1,1,0]
          ])  


def add_error(codeword, percentage):
    bits_to_flip = int(len(codeword) * percentage / 100)
    positions = rnd.sample(range(len(codeword)), bits_to_flip)
    received = vector(M, codeword)
    for pos in positions:
        received[pos] += 1
    return received



for i, chunk in enumerate(chunks):
    bits = [int(b[0]) for b in chunk]
    #print(f"Before encoding {chunk}")
          
    codeword = encode(bits) #encode with generator matrix
    #print(f"Codeword: {codeword}")
          
    received = add_error(codeword, 20) # add error
    
    received = ''.join(str(int(b)) for b in received)
    encoded = base64.b64encode(received.encode("ascii")

with open("codeword.txt", "w") as c:
    c.write(encoded)
# πρεπει να σταλθει και το original_length 
