'''
Python does NOT directly run .py file:
#Steps:
->Reads .py file
->Converts it into bytecode (machine-friendly instructions)
->Executes that bytecode.

->Instead of doing this every time, Python:Saves bytecode as .pyc file
->Stores it in __pycache__
->So next time → faster execution
'''
from module1 import my_function
# from Advanced_python1.try_else_and_finally import fun
# fun()  for folder 
