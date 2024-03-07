
# let's say we have the following 4-bit instructions
# We operate on 4-bit words, so 0 .. 15
# The LSB says PUSH if 0, the one after that controls a mux for res=1/const=0
# bits 2 and 3 are the opcodes

# Push a constant onto the stack. This constant is the second word in a tuple
# It could of course be combined with the instruction into a single word
PUSHCONST = 0x00 # 0000
# Push the result of the ALU calculation onto the stack
PUSHRES = 0x02 # 0010
# ALU operations
ADD = 0x01 # 0001, +
SUB = 0x05 # 0101, -
MUL = 0x09 # 1001, *
DIV = 0x0d # 1101, /


# This is purely for pretty-printing
mnemonics = [''] * 16
mnemonics[0x00] = 'PUSHCONST'  # 0000
mnemonics[0x02] = 'PUSHRES'   # 0010
mnemonics[0x01] = 'ADD'   # 0001
mnemonics[0x05] = 'SUB'   # 0101
mnemonics[0x09] = 'MUL'   # 1001
mnemonics[0x0d] ='DIV'   # 1101
