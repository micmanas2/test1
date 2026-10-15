from sage.all import *
import base64 

with open("encoded.txt", "r") as c:
  encoded = c.read()

decoded = base64.b64decode(encoded).decode("ascii")

chunks = [decoded[i:i+8] for i in range(0, len(decoded), 8)] 

M = GF(2)


H = matrix(M, [                # parity check matrix
          [1,1,0,1,1,0,0,0],
          [1,0,1,1,0,1,0,0],
          [0,1,1,1,0,0,1,0],
          [1,1,1,0,0,0,0,1]
          ])


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




reconstructed = ""
for i, chunk in enumerate(chunks):
    bits = [int(b[0]) for b in chunk]         
    decoded = base64.b64decode(encoded).decode("ascii") 
    og = decode(decoded)
    og = ''.join(str(int(bit)) for bit in og)
    reconstructed += og
     

final = reconstructed[:original_length]
print("Final Result")
print(final == codeword2)



to_bytes = bytes(int(final[i:i+8],  2) for i in range(0, len(final), 8))

with open("kostas2", "wb") as bits:
    bits.write(to_bytes)
