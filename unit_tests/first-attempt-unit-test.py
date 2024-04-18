from ctypes import *

so_file = "./unit_tests/multiplyByThree.so"

function_test = CDLL(so_file)

print(function_test.multiplyByThree(5))