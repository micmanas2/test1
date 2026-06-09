from sage.all import *

M = GF(2)

G = matrix(M, [                # generator matrix απο το βιβλιιο (7,4)
          [1,0,0,0,1,1,1]
          [0,1,0,0,1,1,0]
          [0,0,1,0,1,0,1]
          [0,0,0,1,0,1,1]
          ])           

Η =  matrix(M, [              # πίνακας ελέγχου από το βιβλίο (7,3)
            [1,1,1,0,1,0,0],
            [1,1,0,1,0,1,0]
            [1,0,1,1,0,0,1]
            ])

def encode(m):
  return vector(F, m) * G

def error_syndrome(r):
  return vector(F, r) * H

def build_error_syndrome_table():
  table = {}
  zero = vector(F, [0]*7)
  table[tuple(error_syndrome(zero))] = zero
  for i in range(7):
    e = [0]*7
    e[i] =  1
    e = vector(F, e)
    s = error_syndorme(e)
    table[tuple(s)] = e
  return table    

error_syndrome_table = build_error_syndorme_table()


def decode(r):
  r = vector(F, r)
  s = tuple(error_syndrome(s))
  if all (v == 0 for v in s):
    print(f"No errors")
    corrected = r
  elif s in error_syndrome_table:
    e = error_syndrome_table(s)
    corrected = r - e
  else:
    print(f"Uncorrectable error")
    return none

  message = list(corrected)[:4]
  print(f"Decoded message: {message}")
  return message
