for i, chunk in enumerate(chunks):
    bits = [int(b) for b in chunk]
    codeword = encode(bits)
    print(f"Chunk {i}: {bits} → encoded: {list(codeword)}")

    decoded = decode(received)
    print()
