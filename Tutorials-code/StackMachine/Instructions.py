
# We have the following 4-bit instructions implemented as 4-bit words
# The LSB (bit 0) indicates a PUSH if 0, bit 1 controls a mux for result=1/constant=0
# Bits 2 and 3 are the opcode for the ALU, so we have only 4 ALU operations

# Push a constant onto the stack. 
PUSHCONST = 0x00 # 0000
# Push the result of the ALU calculation onto the stack
PUSHRES = 0x02 # 0010
# ALU operations
ADD = 0x01 # 0001, +
SUB = 0x05 # 0101, -
MUL = 0x09 # 1001, *
EQ = 0x0d # 1101, ==

# This is purely for pretty-printing
mnemonics = [''] * 16
mnemonics[0x00] = 'PUSHCONST'  # 0000
mnemonics[0x02] = 'PUSHRES'   # 0010
mnemonics[0x01] = 'ADD'   # 0001
mnemonics[0x05] = 'SUB'   # 0101
mnemonics[0x09] = 'MUL'   # 1001
mnemonics[0x0d] ='EQ'   # 1101
