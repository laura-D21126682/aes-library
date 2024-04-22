from ctypes import *
from pathlib import Path
import sys
import secrets
import unittest

# Path for AES python submodule  
python_aes_path = Path(__file__).resolve().parent.parent / 'python-aes'
sys.path.append(str(python_aes_path))
import aes as aes_python

# Path for .so file (shared object)
base_path = Path(__file__).resolve().parent
so_file = base_path / '../rijndael.so'
aes_c = CDLL(so_file) # Load .so file


def random_buffer_generator():
  buffers = [] 
  for i in range(3):
    buffers.append(secrets.token_bytes(16)) # Secrets library - returns random byte string
  return buffers


class TestAESMethods(unittest.TestCase):

  def test_sub_bytes(self):
    buffers = random_buffer_generator()
    test_results = []
    for buffer in buffers:
      # Convert buffer to C and Python expected formats
      c_buffer = create_string_buffer(buffer, 16).raw; # C expects 16 byte flat array
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)] # Python expects 4*4 matrix
      
      # Call sub-byte functions
      aes_c.sub_bytes(c_buffer)
      aes_python.sub_bytes(py_buffer)

      # Convert data types of sub-byte results for unit test comparison
      c_result = list(c_buffer) # converts to python list
      py_result = sum(py_buffer, []) # flattens 4*4 matrix to python list

      test_results.append((c_result == py_result))

      self.assertEqual(c_result, py_result, "C and Python results should be the same")
    
    print("Test Restults: ", test_results)


if __name__ == '__main__':
  unittest.main()
