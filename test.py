image = "101011001111"  # example binary string

while len(image) % 4 != 0:    # pad to multiple of 4
    image += "0"

chunks = [image[i:i+4] for i in range(0, len(image), 4)]

print(f"Original chunks: {chunks}\n")

for i, chunk in enumerate(chunks):
    bits = [int(b) for b in chunk]
    codeword = encode(bits)
    print(f"Chunk {i}: {bits} → encoded: {list(codeword)}")

    decoded = decode(received)
    print()
