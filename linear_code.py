from sage.all import *

image = ""

while len(image) % 4 != 0:     # padding
          image += "0"

chunks = [image[i:i+4] for i in range(0, len(image), 4)]   # split into chunks of 4
          
M = GF(2)

# 16 διαφορετικά μηνύματα(2^4)
# 128 διαφορετικοί vectors(2^7)

G = matrix(M, [                # generator matrix απο το βιβλιιο (7,4)
          [1,0,0,0,1,1,1],
          [0,1,0,0,1,1,0],
          [0,0,1,0,1,0,1],
          [0,0,0,1,0,1,1]
          ])           

H =  matrix(M, [              # πίνακας ελέγχου από το βιβλίο (7,3)
            [1,1,1,0,1,0,0],
            [1,1,0,1,0,1,0],
            [1,0,1,1,0,0,1]
            ])

# Κάθε vector() ή tuple() αλλάζει τον τύπο τις μεταβλητής όπως χρειάζεται για να μπορέσουν να γίνουν οι πράξεις

def encode(c):                # πολλαπλασιαζμός μηνύματος(c) με generator matrix
  return vector(M, c) * G

def error_syndrome(r):        # πολλαπλασιαμός με πίνακα ελέγχου. r = c + e(error)
   return H * vector(M, r)

# 128/16 = 8 σύμπλοκα

def build_error_syndrome_table():
  table = {}
  zero = vector(M, [0,0,0,0,0,0,0])
  table[tuple(error_syndrome(zero))] = zero # no error
  for i in range(7):
    e = [0,0,0,0,0,0,0]
    e[i] =  1
    e = vector(F, e)
    s = error_syndrome(e)
    table[tuple(s)] = e
  return table    

error_syndrome_table = build_error_syndrome_table()


def decode(r):
  r = vector(M, r)
  s = tuple(error_syndrome(r))
  if all (v == 0 for v in s):
    print(f"No errors")
    corrected = r
  elif s in error_syndrome_table:
    e = error_syndrome_table[s]
    corrected = r - e
  else:
    print(f"Uncorrectable error")
    return None

  message = list(corrected)[:4]
  print(f"Decoded message: {message}")
  return message
