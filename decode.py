from sage.all import *
import base64 

with open("encoded.txt", "r") as c:
  data = c.read()
  
M = GF(2)


H = matrix(M, [                # parity check matrix
          [1,1,0,1,1,0,0,0],
          [1,0,1,1,0,1,0,0],
          [0,1,1,1,0,0,1,0],
          [1,1,1,0,0,0,0,1]
          ])
