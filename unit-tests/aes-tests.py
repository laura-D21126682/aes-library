import unittest
from ctypes import *
from pathlib import Path
import sys
import os
import secrets
import importlib.util


# Path for AES python submodule  
python_aes_path = Path(__file__).resolve().parent.parent / 'python-aes'
python_aes_path = python_aes_path.resolve().absolute()
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

  '''
  Sub-Bytes Unit Tests
  '''
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

  '''
  Invert Sub-Bytes Unit Tests
  '''
  def test_invert_sub_bytes(self):
    buffers = random_buffer_generator()
    test_results = []
    for buffer in buffers:
      # Convert buffer to C and Python expected formats
      c_buffer = create_string_buffer(buffer, 16).raw; # C expects 16 byte flat array
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)] # Python expects 4*4 matrix
      
      # Call invert sub-byte functions
      aes_c.invert_sub_bytes(c_buffer)
      aes_python.inv_sub_bytes(py_buffer)

      # Convert results for unit test comparison
      c_result = list(c_buffer) # converts to python list
      py_result = sum(py_buffer, []) # flattens 4*4 matrix to python list

      test_results.append((c_result == py_result))

      self.assertEqual(c_result, py_result, "C and Python results should be the same")
    
    print("Test Restults: ", test_results)


  '''
  Shift-Row Unit Tests
  '''
  def test_shift_rows(self):
    buffers = random_buffer_generator()
    test_results = []
    for buffer in buffers:
      # transform buffers
      c_buffer = create_string_buffer(buffer, 16).raw; 
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)]

      # Call shift-row
      aes_c.shift_rows(c_buffer)
      aes_python.shift_rows(py_buffer)

      # transform results for unit test
      c_result = list(c_buffer) 
      py_result = sum(py_buffer, [])

      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "c and Python results should be the same")
      
      print("Test Restults: ", test_results)


  '''
  Invert Shift-Row Unit Tests
  '''
  def test_invert_shift_rows(self):
    buffers = random_buffer_generator()
    test_results = []
    for buffer in buffers:
      # transform buffers
      c_buffer = create_string_buffer(buffer, 16).raw;
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)] 
      
      # Call invert shift_rows
      aes_c.invert_shift_rows(c_buffer)
      aes_python.inv_shift_rows(py_buffer)

      # transform results for unit test
      c_result = list(c_buffer) 
      py_result = sum(py_buffer, []) 

      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "C and Python results should be the same")
    
    print("Test Restults: ", test_results)

  
  '''
  Mix-Columns Unit Tests
  '''
  def test_mix_columns(self):
    test_results = []
    buffers = random_buffer_generator()
    for buffer in buffers:
      # transform buffers
      c_buffer = create_string_buffer(buffer, 16).raw;
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)]

      # Call mix_columns
      aes_c.mix_columns(c_buffer)
      aes_python.mix_columns(py_buffer)

      # transform results for unit test
      c_result = list(c_buffer)
      py_result = sum(py_buffer, [])

      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "C and Python results should be the same")
      
      print("Test Restults: ", test_results)


  '''
  Invert Mix-Columns Unit Tests
  '''
  def test_invert_mix_columns(self):
    buffers = random_buffer_generator()
    test_results = []
    for buffer in buffers:
      # transform buffers
      c_buffer = create_string_buffer(buffer, 16).raw;
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)]

      # Call mix_columns
      aes_c.invert_mix_columns(c_buffer)
      aes_python.inv_mix_columns(py_buffer)

      # transform results for unit test
      c_result = list(c_buffer)
      py_result = sum(py_buffer, [])

      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "C and Python results should be the same")
    
    print("Test Restults: ", test_results)



if __name__ == '__main__':
  unittest.main()
