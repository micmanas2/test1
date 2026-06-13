import random

def add_errors(codeword, error_percent):
    """
    Introduces random bit flips into a codeword.
    error_percent: float between 0 and 1 (e.g. 0.1 = 10%)
    """
    codeword = list(codeword)
    n = len(codeword)
    
    num_errors = max(1, int(n * error_percent))  # at least 1 error
    
    # pick random unique positions to flip
    error_positions = random.sample(range(n), min(num_errors, n))
    
    for pos in error_positions:
        codeword[pos] = int(codeword[pos]) ^ 1   # flip bit with XOR
    
    print(f"  Errors introduced: {num_errors} ({error_percent*100}% of {n} bits)")
    print(f"  Error positions: {error_positions}")
    return codeword

for i, chunk in enumerate(chunks):
    bits = [int(b) for b in chunk]
    codeword = encode(bits)
    print(f"\nChunk {i}: {bits} → encoded: {list(codeword)}")

    # 10% error rate
    received = add_errors(codeword, error_percent=0.10)
    print(f"  Received: {received}")

    decoded = decode(received)
