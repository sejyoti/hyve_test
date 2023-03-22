import unittest

from io import BytesIO

from decoder import decode_pairs
from encoder import encode_pairs
from main import run

class TestDecoder(unittest.TestCase):

    def test_decode_pairs(self):
        # Test decoding a simple pair
        encoded_data = [(0, 97)]
        decoded_data = decode_pairs(encoded_data)
        self.assertEqual(decoded_data, b'a')

        # Test decoding a pair that references a previous position
        encoded_data = [(0, 97), (1, 1)]
        decoded_data = decode_pairs(encoded_data)
        self.assertEqual(decoded_data, b'aa')

        # Test decoding a pair that is too long
        encoded_data = [(0, 97), (2, 2)]
        decoded_data = decode_pairs(encoded_data)
        self.assertEqual(decoded_data, b'\xe2\x9c\xb8\xe2\x9d\x8b')

    def test_encode_pairs(self):
        # Test encoding a simple byte
        decoded_data = b'a'
        encoded_data = encode_pairs(decoded_data)
        self.assertEqual(encoded_data, [(0, 97)])

        # Test encoding a sequence with repeated bytes
        decoded_data = b'aaaaaa'
        encoded_data = encode_pairs(decoded_data)
        self.assertEqual(encoded_data, [(0, 97), (5, 1)])

        # Test encoding a sequence with a long repeated subsequence
        decoded_data = b'abcdefabcdefabcdef'
        encoded_data = encode_pairs(decoded_data)
        self.assertEqual(encoded_data, [(0, 97), (1, 1), (1, 1), (1, 1), (6, 6)])

class TestMain(unittest.TestCase):

    def test_run(self):
        # Test decoding and re-encoding a simple byte
        input_data = BytesIO(b'\x00a')
        output_data = BytesIO()
        error_data = BytesIO()
        run(input_data, output_data, error_data)
        self.assertEqual(output_data.getvalue(), b'a')
        self.assertEqual(error_data.getvalue(), b'\x00a')

        # Test decoding and re-encoding a sequence with repeated bytes
        input_data = BytesIO(b'\x00a\x05\x01')
        output_data = BytesIO()
        error_data = BytesIO()
        run(input_data, output_data, error_data)
        self.assertEqual(output_data.getvalue(), b'aaaaa')
        self.assertEqual(error_data.getvalue(), b'\x00a\x05\x01')

        # Test decoding and re-encoding a sequence with a long repeated subsequence
        input_data = BytesIO(b'\x00a\x01\x01\x01\x06\x06')
        output_data = BytesIO()
        error_data = BytesIO()
        run(input_data, output_data, error_data)
        self.assertEqual(output_data.getvalue(), b'abcdefabcdefabcdef')
        self.assertEqual(error_data.getvalue(), b'\x00a\x01\x01\x01\x06\x06')

if __name__ == '__main__':
    unittest.main()


These tests cover the basic functionality of the encoder, decoder, and main functions. However, additional tests could be written to test edge cases or more complex data.