from MuxDemux import *

# Sequential: Increment the stack pointer, modulo 4
def incSP(sp):
    b1,b2 =sp
    _sp = b1+2*b2
    _inc_sp = (_sp+1)%4
    inc_b1 = _inc_sp&0x01
    inc_b2 = _inc_sp>>1
    return (inc_b1,inc_b2)

# Sequential: Decrement the stack pointer, modulo 4
def decSP(sp):    
    b1,b2 =sp
    _sp = b1+2*b2
    _inc_sp = (_sp+-1)%4
    inc_b1 = _inc_sp&0x01
    inc_b2 = _inc_sp>>1
    return (inc_b1,inc_b2)
    
# Sequential: Update one of the registers that make up the stack
def updateReg(reg,ld,x):
    if ld==1:
        reg=x
    return reg

# Sequential: push `x` onto the stack if `push` == 1
def pushOntoStack(x,push,stack,sp):
    # high-level implementation:
    # stack[sp[0]+2*sp[1]]=x
    # using a demux:
    out4 = demux4bit(sp,push)
    stack[0] = updateReg(stack[0],out4[0],x)
    stack[1] = updateReg(stack[1],out4[1],x)
    stack[2] = updateReg(stack[2],out4[2],x)
    stack[3] = updateReg(stack[3],out4[3],x)
    # increment the stack pointer
    if push:
        sp = incSP(sp)
    return (stack,sp)

# Combinational: read two values (`a` and `b`) from the top of the stack
def readAB(stack,sp):
    a = mux4word(decSP(sp),stack)
    b = mux4word(decSP(decSP(sp)),stack)
    t = (a,b)
    return t


