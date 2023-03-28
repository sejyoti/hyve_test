import io
import os
import unittest
from decoding import decode_data

class TestDecoding(unittest.TestCase):
    
    def test_decode_data(self):
        # Example input from the prompt
        input_data = b'\x00\x61\x01\x01\x00\x62\x03\x02\x03\x03'
        expected_output = b'\x61\x61\x62\x61\x61\x62\x61\x61\x62\x61\x61\x62\x61\x61'
        
        # Redirect stdout to a buffer
        stdout_backup = sys.stdout
        sys.stdout = io.StringIO()
        
        # Call decode_data on the input data
        decode_data(input_data)
        
        # Get the decoded data from stdout buffer
        decoded_output = sys.stdout.getvalue().encode()
        
        # Check if decoded_output matches expected_output
        self.assertEqual(decoded_output, expected_output)
        
        # Get the re-encoded data from stderr buffer
        re_encoded_data = sys.stderr.getvalue().encode()
        
        # Check if the re-encoded data matches the input data
        self.assertEqual(re_encoded_data, input_data)
        
        # Clean up stdout and stderr
        sys.stdout = stdout_backup
        sys.stderr.seek(0)
        sys.stderr.truncate(0)
