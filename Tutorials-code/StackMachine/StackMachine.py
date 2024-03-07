from Stack import *
from ALU import *
from Instructions import *

# I use tuples but of course this could be combined into a single word
# The instructions are explained in `Instructions.py`

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
    instr,x = word
    print(mnemonics[instr],hex(x))
    # `push` control signal
    push = NOT(instr & 0x01)
    # `const_res` controls the demux between constant and ALU result
    const_res = (instr >> 1 ) & 0x01
    # Get `opcode` from the instruction word
    opcode = instr >> 2
    # `val` is either `x` or `res` depending on `const_res`
    val = mux2word(const_res,(x,res))

    # push the value onto the stack if `push`==1
    stack, sp = pushOntoStack(val,push,stack,sp)
    # read the values `a` and `b` from the top two stack positions
    a,b = readAB(stack,sp)
    # calculate the result of the operation identified by `opcode` on `a` and `b`
    res = ALU(a,b,opcode)
    
    # remove `a` and `b` from the stack
    if push==0:
        sp = decSP(sp)
        sp = decSP(sp)

    print(list(map(hex,stack)),sp)

