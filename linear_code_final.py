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

H = matrix(M, [                # parity check matrix
          [1,1,0,1,1,0,0,0],
          [1,0,1,1,0,1,0,0],
          [0,1,1,1,0,0,1,0],
          [1,1,1,0,0,0,0,1]
          ])

# Κάθε vector() ή tuple() αλλάζει τον τύπο τις μεταβλητής όπως χρειάζεται για να μπορέσουν να γίνουν οι πράξεις

def encode(c):                # πολλαπλασιαζμός μηνύματος(c) με generator matrix
  return vector(M, c) * G

def error_syndrome(r):        # πολλαπλασιαμός με πίνακα ελέγχου. r = c + e(error)
   return H * vector(M, r)


def build_error_syndrome_table():
  table = {}
  zero = vector(M, [0,0,0,0,0,0,0,0])
  table[tuple(error_syndrome(zero))] = zero # no error
  for i in range(8):
    e = [0,0,0,0,0,0,0,0]
    e[i] =  1
    e = vector(M, e)
    table[tuple(error_syndrome(e))] = e
  return table    

error_syndrome_table = build_error_syndrome_table()


def decode(r):
    r = vector(M, r)
    s = tuple(error_syndrome(r))
    if s not in error_syndrome_table: 
        print("More than 1 errors. Can't be corrected")
        return None
    e = error_syndrome_table[s]
    corrected = r - e
    
    if all (v == 0 for v in s):          # αν = 000 σημάινει οτι δεν έχει σφάλματα
        print("No errors")
        print(f"Decoded {corrected}")
        print(f"Original Message: {corrected[:4]}") 
    elif s in error_syndrome_table:
        print("Error Detected")    
       # print(f"Corrected {corrected}")
      #  print(f"Original Message: {corrected[:4]}")
    return corrected[:4]




def add_error(codeword, percentage):
    bits_to_flip = int(len(codeword) * percentage / 100)
    positions = rnd.sample(range(len(codeword)), bits_to_flip)
    received = vector(M, codeword)
    for pos in positions:
        received[pos] += 1
    return received
    
# αυτο απλα κανει τους υπολογιζμους για να δω οτι δουλευει ο κωδικας.
# θα γινουν αλλιως οι υπολοιησεις στο κανονικη εργασια
###
reconstructed = ""
for i, chunk in enumerate(chunks):
    bits = [int(b[0]) for b in chunk]
    #print(f"Before encoding {chunk}")
          
    codeword = encode(bits) #encode with generator matrix
    #print(f"Codeword: {codeword}")
          
    received = add_error(codeword, 20) # add error
    
    received = ''.join(str(int(b)) for b in received)
    encoded = base64.b64encode(received.encode("ascii")) #encode with base64
    #print (f"Encoded with base64 {encoded}")
    
   ### λγκ τα παραπανω θα μπουν στη μερια του αποστολεα               
   ### και τα παρακατω στη μερια του παραληπτη. δν ειμαι και σιγουρος ομως :)
         
    decoded = base64.b64decode(encoded).decode("ascii") #decode with base64
    #print(f"Decoded with base64 {decoded}")
          
          
    #print(f"Received: {decoded}") #decode with parity check matrix
    og = decode(decoded)
    og = ''.join(str(int(bit)) for bit in og)
    #print(og == chunk)
    reconstructed += og
     
print("Final Result")
final = reconstructed[:original_length]
print(final == codeword2)



to_bytes = bytes(int(final[i:i+8],  2) for i in range(0, len(final), 8))

with open("kostas2", "wb") as bits:
    bits.write(to_bytes)

    
    

    
    
    
