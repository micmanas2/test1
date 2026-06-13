import random

def add_errors(codeword, error_percent):

    codeword = list(codeword)
    n = len(codeword)    # πάντα 7 
    num_errors =  int(n * error_percent))  # στρογγυλοποίηση προς τα κάτω -  θα βάλει 0 ως 7 μοναδικά σφάλματα(error_percent 0-1)
    
    error_positions = random.sample(range(n), min(num_errors, n)) # βρίσκει τις θέσεις στις οποίες θα βάλει τα σφάλματα
    
    for pos in error_positions:
         codeword[pos] = int(codeword[pos]) ^ 1   # στις θέσεις που υπολόγισε αλλάζει τα bits
         return codeword


for i, chunk in enumerate(chunks):
    bits = [tuple(b) for b in chunk]
    codeword = encode(bits)

    # 10% error rate
    received = add_errors(codeword, error_percent=0.10)
    print(f"  Received: {received}")
    decode(received)
