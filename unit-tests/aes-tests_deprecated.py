from ctypes import *
from pathlib import Path
import sys
import secrets
# import numpy as np

# Path for AES python submodule  
python_aes_path = Path(__file__).resolve().parent.parent / 'python-aes'
sys.path.append(str(python_aes_path))

import aes as aes_python

# Path for .so file (shared object)
base_path = Path(__file__).resolve().parent
so_file = base_path / '../rijndael.so'

# Load .so file
aes_c = CDLL(so_file)

# Create buffer
buffer =  b'\x00\x01\x02\x03'
buffer += b'\x04\x05\x06\x07'
buffer += b'\x08\x09\x0A\x0B'
buffer += b'\x0C\x0D\x0E\x0F'


def random_buffer_generator():
  buffers = [] 
  for i in range(3):
    buffers.append(secrets.token_bytes(16))
  return buffers


def test_sub_bytes(buffers):
  # Convert buffer to expected formats for C and Python
  for buffer in buffers:
    c_buffer = create_string_buffer(buffer, 16).raw; # C expects 16 byte flat array
    py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)] # Python expects 4*4 matrix

    # Call sub-byte functions
    aes_c.sub_bytes(c_buffer)
    aes_python.sub_bytes(py_buffer) 

    # Convert data types of sub-byte results for unit test comparison
    c_result = list(c_buffer) # converts to python list
    py_result = sum(py_buffer, []) # flattens 4*4 matrix to python list

    print("C Sub-Byte Encryption  : ", c_result)
    print("PY Sub-Byte Encryption : ", py_result)
    compare_functions = c_result == py_result
    print("Results are the same? ", c_result == py_result)


buffers = random_buffer_generator()
print(test_sub_bytes(buffers))












