from ctypes import *
import os

base_path = os.path.dirname(os.path.abspath(__file__))  # Gets the directory of the script
so_file = os.path.join(base_path, '../rijndael.so')


function_test = CDLL(so_file)

print(function_test.multiplyByThree(5))