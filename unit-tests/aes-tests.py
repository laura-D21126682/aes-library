import unittest
from ctypes import *
from pathlib import Path
import sys
import secrets

# Path for AES python submodule  
python_aes_path = Path(__file__).resolve().parent.parent / 'python-aes'
python_aes_path = python_aes_path.resolve().absolute()
sys.path.append(str(python_aes_path))
import aes as aes_python
# Paths for .so file (shared object)
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
  Sub-Bytes Unit Test
  '''
  def test_sub_bytes(self):
    buffers = random_buffer_generator()
    test_results = []
    for buffer in buffers:
      # Instantiate buffers
      c_buffer = create_string_buffer(buffer, 16).raw; # C expects 16 byte flat array
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)] # Python expects 4*4 matrix

      # Call sub-bytes
      aes_c.sub_bytes(c_buffer)
      aes_python.sub_bytes(py_buffer)

      # Convert results to common format for fair comparison
      c_result = list(c_buffer) # converts to python list
      py_result = sum(py_buffer, []) # flattens 4*4 matrix to python list

      # Tests
      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "C and Python results should be the same")

    print("Sub-Bytes--------------Test Results: ", test_results)


  '''
  Invert Sub-Bytes Unit Test
  '''
  def test_invert_sub_bytes(self):
    buffers = random_buffer_generator()
    test_results = []
    for buffer in buffers:
      # Instantiate buffers
      c_buffer = create_string_buffer(buffer, 16).raw; 
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)] 

      # Call invert sub bytes
      aes_c.invert_sub_bytes(c_buffer)
      aes_python.inv_sub_bytes(py_buffer)

      # Results
      c_result = list(c_buffer) 
      py_result = sum(py_buffer, []) 

      # Tests
      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "C and Python results should be the same")
    
    print("Inv-Sub-Bytes----------Test Results: ", test_results)


  '''
  Shift-Row Unit Test
  '''
  def test_shift_rows(self):
    buffers = random_buffer_generator()
    test_results = []
    for buffer in buffers:
      # Instantiate buffers
      c_buffer = create_string_buffer(buffer, 16).raw; 
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)]

      # Call shift rows
      aes_c.shift_rows(c_buffer)
      aes_python.shift_rows(py_buffer)

      # Results
      c_result = list(c_buffer) 
      py_result = sum(py_buffer, [])

      # Tests
      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "c and Python results should be the same")
      
    print("Shift-Rows-------------Test Results: ", test_results)


  '''
  Invert Shift-Row Unit Test
  '''
  def test_invert_shift_rows(self):
    buffers = random_buffer_generator()
    test_results = []
    for buffer in buffers:
      # Transform buffers
      c_buffer = create_string_buffer(buffer, 16).raw;
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)] 
      
      # Call invert shift_rows
      aes_c.invert_shift_rows(c_buffer)
      aes_python.inv_shift_rows(py_buffer)

      # Results
      c_result = list(c_buffer) 
      py_result = sum(py_buffer, []) 

      # Tests
      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "C and Python results should be the same")
    
    print("Inv-Shift-Rows---------Test Results: ", test_results)

  
  '''
  Mix-Columns Unit Test
  '''
  def test_mix_columns(self):
    test_results = []
    buffers = random_buffer_generator()
    for buffer in buffers:
      # Instantiate Buffers
      c_buffer = create_string_buffer(buffer, 16).raw;
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)]

      # Call Mix Columns
      aes_c.mix_columns(c_buffer)
      aes_python.mix_columns(py_buffer)

      # Results
      c_result = list(c_buffer)
      py_result = sum(py_buffer, [])

      # Tests
      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "C and Python results should be the same")
      
    print("Mix-Columns------------Test Results: ", test_results)


  '''
  Invert Mix-Columns Unit Test
  '''
  def test_invert_mix_columns(self):
    buffers = random_buffer_generator()
    test_results = []
    for buffer in buffers:
      # Instantiate Buffers
      c_buffer = create_string_buffer(buffer, 16).raw;
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)]

      # Call Invert Mix Columns
      aes_c.invert_mix_columns(c_buffer)
      aes_python.inv_mix_columns(py_buffer)

      # Results
      c_result = list(c_buffer)
      py_result = sum(py_buffer, [])

      # Tests
      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "C and Python results should be the same")
    
    print("Inv-Mix-Cols-----------Test Results: ", test_results)

  '''
  Add Round Key Unit Test
  '''
  def test_add_round_key(self):
    buffers = random_buffer_generator()
    keys = random_buffer_generator()
    test_results = []
    for buffer, key in zip(buffers, keys):
      # Instantiate Buffers
      c_buffer = create_string_buffer(buffer, 16).raw;
      py_buffer = [list(buffer[i * 4:(i + 1) * 4]) for i in range(4)]

      # Instantiate Keys
      c_key = create_string_buffer(key, 16).raw;
      py_key = [list(key[i * 4:(i + 1) * 4]) for i in range(4)]

      # Call Add Round Key
      aes_c.add_round_key(c_buffer, c_key)
      aes_python.add_round_key(py_buffer, py_key)

      # Results
      c_result = list(c_buffer)
      py_result = sum(py_buffer, [])

      # Tests
      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "C and Python results should be the same")
    
    print("Add-Round-Key----------Test Results: ", test_results)

  '''
  Expand Key Unit Test
  '''
  def test_expand_key(self):
    keys = random_buffer_generator()
    test_results = []

    # Set C return and arg types 
    aes_c.expand_key.restype = POINTER(c_ubyte * 176) # Expand key function returns: 176 Byte pointer array
    aes_c.expand_key.argtypes = [POINTER(c_ubyte * 16)] # Expand key function param: pointer to 16 byte array
    
    for key in keys:
      # Instiantiate keys
      c_key = (c_ubyte * 16)(*key) #transform key for C
      py_key = key
     
      # Python setup
      py_aes_class = aes_python.AES(py_key) # Initialise Py AES Class and pass it the generated key
      py_expand_key = py_aes_class._expand_key(py_key) # Call Py expand key function
      py_result = [byte for block in py_expand_key for row in block for byte in row] # convert to flat list for comparison
     
      # C setup
      c_pointer = aes_c.expand_key(byref(c_key)) # Call C expand key function with pointer to key
      c_result = list(c_pointer.contents) # Convert to list for comparison
      
      # Tests
      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "C and Python results should be the same")
    
    print("Expand-Key-------------Test Results: ", test_results)



  '''
  Set C return & arg types for Encypt/Decrypt Functions
  '''
  # Set C Encrypt Pointers
  aes_c.aes_encrypt_block.restype = POINTER(c_ubyte * 16) # Encrypt function returns: 16 Byte pointer array
  aes_c.aes_encrypt_block.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte)] # Encrypt function params:
  # Set C Decrypt Pointers
  aes_c.aes_decrypt_block.restype = POINTER(c_ubyte * 16) # Decrypt function returns: 16 Byte pointer array
  aes_c.aes_decrypt_block.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte)] # Decrypt function params:

  
  '''
  AES Encrypt Block Unit Test
  '''
  def test_encrypt_block(self):
    plaintexts = random_buffer_generator()
    keys = random_buffer_generator()
    test_results = []
    
    for plaintext, key in zip(keys, plaintexts):
      # Instantiate keys
      c_key = (c_ubyte * 16)(*key)
      py_key = key
      # Instantiate plaintext
      c_plaintext = (c_ubyte * 16)(*plaintext) # Transform plaintext for C
      py_plaintext = plaintext

      # python setup
      py_aes_class = aes_python.AES(py_key) # Initialise Py AES Class
      py_encrypt_block = py_aes_class.encrypt_block(py_plaintext) # Call Py encrypt block function
      py_result = list(py_encrypt_block) # convert to flat list for comparison

      # C setup
      c_pointer = aes_c.aes_encrypt_block(c_plaintext, c_key)  # Call C encrypt block function with pointer to key & plaintext
      c_result = list(c_pointer.contents) # Convert to list for comparison

      # Tests
      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "C and Python results should be the same")
    
    print("Encrypt----------------Test Results: ", test_results)


  '''
  AES Decrypt Block Unit Test
  '''
  def test_decrypt_block(self):
    plaintexts = random_buffer_generator()
    keys = random_buffer_generator()
    test_results = []
    
    for plaintext, key in zip(keys, plaintexts):
      # Instantiate keys
      c_key = (c_ubyte * 16)(*key)
      py_key = key
      # Instantiate plaintext
      c_plaintext = (c_ubyte * 16)(*plaintext) 
      py_plaintext = plaintext

      # python setup
      py_aes_class = aes_python.AES(key)  # Initialise Py AES Class
      py_decrypt_block = py_aes_class.decrypt_block(py_plaintext) # Call Py encryption
      py_result = list(py_decrypt_block) # convert to list for comparison

      # C setup
      c_pointer = aes_c.aes_decrypt_block(c_plaintext, c_key) # Call C encryption
      c_result = list(c_pointer.contents) # Convert to list for comparison

      # Tests
      test_results.append((c_result == py_result))
      self.assertEqual(c_result, py_result, "C and Python results should be the same")
    
    print("Decrypt----------------Test Results: ", test_results)
  

  '''
  AES Full Encrypt/Decrypt Process Unit Test
  '''
  def test_encrypt_decrypt(self):
    plaintexts = random_buffer_generator()
    keys = random_buffer_generator()
    test_results = []
    
    for plaintext, key in zip(keys, plaintexts):
      # Instantiate keys
      c_key = (c_ubyte * 16)(*key)
      py_key = key
      # Instantiate plaintext
      c_plaintext = (c_ubyte * 16)(*plaintext) 
      py_plaintext = plaintext

      #AES Encryption
      # Python setup
      py_aes_class = aes_python.AES(py_key)
      encrypted_py = py_aes_class.encrypt_block(py_plaintext) 
      encrypted_py_result = list(encrypted_py) 
      # C setup
      encrypted_c = aes_c.aes_encrypt_block(c_plaintext, c_key) 
      encrypted_c_result = list(encrypted_c.contents)
      # Encryption Test
      test_results.append((encrypted_c_result == encrypted_py_result))
      self.assertEqual(encrypted_c_result, encrypted_py_result, "C and Python encryption results should be the same")

      # AES Decryption 
      # Python setup
      decrypted_py = py_aes_class.decrypt_block(encrypted_py) # Call Py encryption with encrypted plaintext
      decrypted_py_result = list(decrypted_py) 
      # C setup
      c_encrypted = (c_ubyte * 16)(*encrypted_c_result) # Transform for C decryption
      decrypted_c = aes_c.aes_decrypt_block(c_encrypted, c_key) # Call C decryption with encrypted plaintext
      decrypted_c_result = list(decrypted_c.contents) 
      # Decryption Test
      test_results.append((decrypted_c_result == decrypted_py_result))
      self.assertEqual(decrypted_c_result, decrypted_py_result, "C and Python results should be the same")

      # Tests
      test_results.append((decrypted_py_result == list(plaintext)))
      test_results.append((decrypted_c_result == list(plaintext)))
      self.assertEqual(decrypted_py_result, list(plaintext), "Python decryption results should be the same as the original plaintext")
      self.assertEqual(decrypted_c_result, list(plaintext), "C decryption results should be the same as the original plaintext")

    print("Encrypt-Decrypt--------Test Results: ", test_results)

if __name__ == '__main__':
  unittest.main()