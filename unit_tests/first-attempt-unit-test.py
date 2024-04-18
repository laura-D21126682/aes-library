from ctypes import *

so_file = "/home/runner/work/aes-library/aes-library/multiplyByThree.so"

function_test = CDLL(so_file)

print(function_test.multiplyByThree(5))