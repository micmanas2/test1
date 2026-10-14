import random as rnd
from sage.all import *



codeword = "0011"

while len(codeword) % 4 != 0:     # padding
          codeword += "0"

chunks = [codeword[i:i+4] for i in range(0, len(codeword), 4)]   # split into chunks of 4
          
M = GF(2)

# 16 διαφορετικά μηνύματα(2^4)
# 128 διαφορετικοί vectors(2^7)

G = matrix(M, [                # generator matrix
          [1,0,0,0,1,1,0,1],
          [0,1,0,0,1,0,1,1],
          [0,0,1,0,0,1,1,1],
          [0,0,0,1,1,1,1,0]
          ])           

H = matrix(M, [
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

# 128/16 = 8 σύμπλοκα

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
  if all (v == 0 for v in s):          # αν = 000 σημάινει οτι δεν έχει σφάλματα
    print("No errors")
    corrected = r
    print(f"Decoded {corrected}")
    print(f"Original Message: {corrected[:4]}")
  elif s in error_syndrome_table: # δε ξερουμε ποσα errors υπαρχουν. Αφου ειναι τεχνητα errors μπορουμε απλα να υπολογισουμε ποσα ειναι απο την add_error function
    print(r[2])
    print("Error Detected")
    asoi = 0
    for i in range(len(r)):
        if r[0] == 1:
            asoi += 1
        return asoi
    print (asoi)
    corrected = r - error_syndrome_table[s]  # XOR    
    print(f"Corrected {corrected}")
    print(f"Original Message: {corrected[:4]}")
  else:
    print("More than 1 errors. Can't be corrected")
    return None



def add_error(codeword, percentage):
    bits_to_flip = int(len(codeword) * percentage / 100)
    positions = rnd.sample(range(len(codeword)), bits_to_flip)
    received = vector(M, codeword)
    for pos in positions:
        received[pos] += 1
    return received


for i, chunk in enumerate(chunks):
    bits = [int(b[0]) for b in chunk]
    print(f"Before encoding {chunk}")
    codeword = encode(bits)
    print(f"Codeword: {codeword}")
    received = add_error(codeword, 20)
    print(f"Received: {received}")
    decode(received)
    
    
