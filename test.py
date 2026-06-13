image = "101011001111"  # example binary string

while len(image) % 4 != 0:    # pad to multiple of 4
    image += "0"

chunks = [image[i:i+4] for i in range(0, len(image), 4)]

print(f"Original chunks: {chunks}\n")

for i, chunk in enumerate(chunks):
    bits = [int(b) for b in chunk]
    codeword = encode(bits)
    print(f"Chunk {i}: {bits} → encoded: {list(codeword)}")

    # Simulate a 1-bit error in position 2
    received = list(codeword)
    received[2] = int(received[2]) ^ 1
    print(f"  Received (with error): {received}")

    decoded = decode(received)
    print()
