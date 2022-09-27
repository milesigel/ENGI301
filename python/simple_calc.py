"""
--------------------------------------------------------------------------
Simple Calculator
--------------------------------------------------------------------------
License:   
Copyright 2022 - Miles Sigel

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Simple calculator that will 
  - Take in two numbers from the user
  - Take in an operator from the user
  - Perform the mathematical operation and provide the number to the user
  - Repeat

Operations:
  - addition
  - subtraction
  - multiplication
  - division

Error conditions:
  - Invalid operator --> Program should exit
  - Invalid number   --> Program should exit

--------------------------------------------------------------------------
"""

# NOTE - Add import statements to allow access to Python library functions

import operator
from re import T

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# NOTE - No constants are needed for this example 

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# NOTE - Need a global variable to map an operator string (e.g. "+") to 
# NOTE - the appropriate function.

operators = {
  "+" : operator.add,
  "-" : operator.sub, 
  "/" : operator.truediv,
  "*" : operator.mul,
  "<<" : operator.lshift,
  ">>" : operator.rshift,
  "%" : operator.mod,
  "**" : operator.pow
}

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------
def get_user_input():
  try:
    number1 = float(input("Enter first number here : "))
    number2 = float(input("Enter second number here : "))
    op = input("Enter function name here (valid values are +, - , *, /, <<, >>, %, **): ")
  except:
    return (None, None, None)

  func = operators.get(op)
  return (number1, number2, func)


# NOTE - Add function "get_user_input()".  This function will:
# NOTE -     """Get input from the user.
# NOTE -          Returns tuple:  (number, number, function) or
# NOTE -          (None, None, None) if inputs invalid
# NOTE -     """
# NOTE - 
# NOTE - User input is generally returned as a string and must be translated.

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

# NOTE - The python variable "__name__" is provided by the language and can 
# NOTE - be used to determine how the file is being executed.  For example,
# NOTE - if the program is being executed on the command line:
# NOTE -   python3 simple_calc.py
# NOTE - then the "__name__" will be the string:  "__main__".  If the file 
# NOTE - is being imported into another python file:
# NOTE -   import simple_calc
# NOTE - the the "__name__" will be the module name, i.e. the string "simple_calc"

if __name__ == "__main__":
  # NOTE - Use "pass" statements to allow code to be run without having to 
  # NOTE - fill out the contents.  This pass statement should be removed    
  try:
    input = raw_input
  except NameError:
    pass

  # NOTE - Need to add main calculator functionality:
  # NOTE -   - Use a loop construct to repeat the operation
  # NOTE -   - Get the input from the user (i.e. use function created above)    
  # NOTE -   - Check that all inputs are valid
  # NOTE -   - Execute the function on the numbers and print the results
  while 1:
    (num1, num2, func) = get_user_input()
    if (num1 == None) or (num2 == None) or (func == None):
      break
    
    print(func(num1, num2))

