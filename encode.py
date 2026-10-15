import random as rnd
from sage.all import *
import base64



#arxeio tou kosta
with open("kostas.bin", "rb") as bits:
    data = bits.read()


codeword2 = ''.join(format(b, '08b') for b i data) #from bytes to bits




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
