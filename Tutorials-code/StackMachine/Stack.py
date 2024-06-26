from MuxDemux import *

# Combinational: Increment the stack pointer, modulo 4
def incSP(sp):
    a,b = sp
    inc_b = XOR(a,b)
    inc_a = NOT(a)
    return (inc_a,inc_b)

# Combinational: Decrement the stack pointer, modulo 4
def decSP(sp):
    a,b = sp
    dec_b = XNOR(a,b)
    dec_a = NOT(a)
    return (dec_a,dec_b)

# Combinational: update one of the registers that make up the stack
#! Change this to use the 4-bit-word mux `mux2word4bits` which you created in `MuxDemux.py`
def updateReg(reg,ld,x):
    return mux2word(ld,(reg,x))

# Combinational: read two values (`a` and `b`) from the top of the stack
def readAB(stack,sp):
    dsp = decSP(sp)
    ddsp = decSP(dsp)
    #! Change this to use the 4-bit-word mux `mux4word4bits` which you created in `MuxDemux.py`
    a = mux4word(dsp,stack)
    b = mux4word(ddsp,stack)
    t = (a,b)
    return t

# Combinational: push `x` onto the stack if `push` == 1
def pushOntoStack(x,push,stack,sp):
    out4 = demux4bit(sp,push)
    stack[0] = updateReg(stack[0],out4[0],x)
    stack[1] = updateReg(stack[1],out4[1],x)
    stack[2] = updateReg(stack[2],out4[2],x)
    stack[3] = updateReg(stack[3],out4[3],x)
    return stack




