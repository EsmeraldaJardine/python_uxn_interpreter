from Stack import *
from ALU import *
from Instructions import *

# The instructions are explained in `Instructions.py`
# I use tuples where the constant is the second word in a tuple if the first word is PUSHCONST
# Otherwise the second word is not used

#! See if you can change this so that the instruction is combined with a 4-bit constant into a byte 

# 3 1 2 ADD 4 MUL ADD
# 3+(1+2)*4 = 15
words = [
         (PUSHCONST,0x3),
         (PUSHCONST,0x1),
         (PUSHCONST,0x2),
         (ADD,0x0),
         (PUSHRES,0x0),
         (PUSHCONST,0x4),
         (MUL,0x0),
         (PUSHRES,0x0),
         (ADD,0x0),
         (PUSHRES,0x0),
        ]

# 2-bit stack pointer
sp=(0,0)

# 4-register stack, each register holds a word
stack=[0,0,0,0]

# result of the computation, this is conceptually a wire
res=0

for word in words:
    # unpack the tuple
    #! If you change from tuples to bytes, this is the only line that needs changing
    instr,x = word
    # print the mnemonic for the instruction and the constant as hexadecimal
    print(mnemonics[instr],hex(x))
    # `push` control signal
    push = NOT(instr & 0x01)
    # `const_res` controls the demux between constant and ALU result
    const_res = (instr >> 1 ) & 0x01
    # Get `opcode` from the instruction word. This removes bits 0 and 1.
    opcode = instr >> 2
    # `val` is either `x` or `res` depending on `const_res`
    #! Change this to use the 4-bit-word mux `mux2word4bits` which you created in `MuxDemux.py`
    val = mux2word(const_res,(x,res))

    # push the value onto the stack if `push`==1
    stack = pushOntoStack(val,push,stack,sp)

    # Sequential: increment the stack pointer
    if push==1:
        sp = incSP(sp)

    # read the values `a` and `b` from the top two stack positions
    a,b = readAB(stack,sp)
    # calculate the result of the operation identified by `opcode` on `a` and `b`
    res = ALU(a,b,opcode)
    
    # Sequential: dencrement the stack pointer to remove `a` and `b` from the stack
    if push==0:
        sp = decSP(sp)
        sp = decSP(sp)

    # print out the stack as hexadecimals and the stack pointer
    print(list(map(hex,stack)),sp) 

