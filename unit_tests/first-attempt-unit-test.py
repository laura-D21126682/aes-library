from ctypes import *

so_file = "../c-aes/rijndael.so"

function_test = CDLL(so_file)

print(function_test.multiplyByThree(5))