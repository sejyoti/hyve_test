import os
import sys

# Constants
TRIVIAL_COMPRESSION_MODE = "0"
INVALID_PAIR = b"\xe2\x9c\xb8\xe2\x9d\x8b"

# Functions

def decode_pairs(pairs):
    decoded_data = bytearray()
    for p, q in pairs:
        if p == 0:
            decoded_data.append(q)
        else:
            start = len(decoded_data) - p
            end = start + q
            if start < 0 or end > len(decoded_data):
                decoded_data.extend(INVALID_PAIR)
            else:
                decoded_data.extend(decoded_data[start:end])
    return decoded_data


def encode_pairs(decoded_data):
    pairs = []
    start = 0
    while start < len(decoded_data):
        # Search for the longest match of previously decoded data
        # starting from the current position
        longest_match = 0
        match_offset = 0
        for p in range(min(start, 255), -1, -1):
            end = start + 1
            while end < len(decoded_data) and decoded_data[start:end] == decoded_data[start-p:end-p]:
                end += 1
            if end - start > longest_match:
                longest_match = end - start
                match_offset = p
        
        # If a match was found, encode it as a pair
        if longest_match > 2:
            pairs.append((match_offset, longest_match))
            start += longest_match
        # Otherwise, encode a single byte as a pair
        else:
            pairs.append((0, decoded_data[start]))
            start += 1
    
    return pairs


# Main program

# Check if we're in trivial compression mode
if os.environ.get("MYCOMPRESS_TRIVIAL_MODE") == TRIVIAL_COMPRESSION_MODE:
    encode_function = lambda x: [(0, b) for b in x]
else:
    encode_function = encode_pairs

# Read input from stdin
encoded_pairs = []
while True:
    # Read two bytes as a pair
    byte1 = sys.stdin.buffer.read(1)
    byte2 = sys.stdin.buffer.read(1)
    if not byte2:
        break
    encoded_pairs.append((byte1[0], byte2[0]))

# Decode the input and write it to stdout
decoded_data = decode_pairs(encoded_pairs)
sys.stdout.buffer.write(decoded_data)

# Encode the decoded data and write it to stderr
encoded_pairs = encode_function(decoded_data)
encoded_data = bytearray()
for p, q in encoded_pairs:
    encoded_data.append(p)
    encoded_data.append(q)
sys.stderr.buffer.write(encoded_data)
