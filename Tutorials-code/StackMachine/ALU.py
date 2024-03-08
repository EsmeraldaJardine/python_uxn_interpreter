from MuxDemux import *
# Combinational arithmetic operations, implemented high-level to work with words of any size

def ALU(a,b,opcode):
    ctrl = (opcode&1,opcode>>1)
    ops=(a+b,a-b,a*b,a==b) # so we execute them in parallel and select the result with the mux
    res = mux4word(ctrl,ops)
    return res

