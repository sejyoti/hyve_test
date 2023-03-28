import sys

def decode_data(encoded_data):
    print("Input data:", encoded_data)

    decoded_data = bytearray()

    # Loop through the input bytes
    for b in encoded_data:
        # Append the complement of each byte to the decoded data
        decoded_data.append(~b & 0xFF)

    print("Decoded data:", decoded_data)
    return decoded_data

if len(sys.argv) < 2:
    print('Usage: python data_decoder.py <filename>')
    sys.exit(1)

# Read the encoded data from the file
with open(sys.argv[1], 'rb') as f:
    encoded_data = f.read()

# Decode the data
decoded_data = decode_data(encoded_data)

# Write the decoded data to a file
with open('decoded_data.bin', 'wb') as f:
    f.write(decoded_data)
