from BasicGates import *
        
# Combinational: muxes and demuxes

# Helper circuit which turns a bus of n bits into 2^n wires of which only one is high
def control2BitsTo4Wires(ctrl4):
    
    t =(
        AND(NOT(ctrl4[0]),NOT(ctrl4[1])), # 00
        AND(ctrl4[0],NOT(ctrl4[1])), #01
        AND(NOT(ctrl4[0]),ctrl4[1]), #10
        AND(ctrl4[0],ctrl4[1]) #11
    )
    return t

# Bit-size demux, 1 in to 4 out
def demux4bit(ctrl4,in1):
    w4=control2BitsTo4Wires(ctrl4)
    out4 = (
        AND(in1,w4[0]),
        AND(in1,w4[1]),
        AND(in1,w4[2]),
        AND(in1,w4[3])
    )
    return out4

# Bit-size mux, 4 in to 1 out
def mux4bit(ctrl4,in4):
    w4=control2BitsTo4Wires(ctrl4)
    out = OR4(
        AND(in4[0],w4[0]),
        AND(in4[1],w4[1]),
        AND(in4[2],w4[2]),
        AND(in4[3],w4[3])
    )
    return out

# Word-size mux, 2 in to 1 out, implemented high-level to work with words of arbitrary size
# As exercise, create one out of low-level components that works for 4-bit words
def mux2word(ctrl,in2):
    return in2[ctrl]

# Word-size mux, 4 in to 1 out, implemented high-level to work with words of arbitrary size
# As exercise, create one out of low-level components that works for 4-bit words
def mux4word(ctrl4,in4):
    ctrl = ctrl4[0]+2*ctrl4[1]
    return in4[ctrl]

# Word-size demux, 1 in to 4 out, implemented high-level to work with words of arbitrary size
# As exercise, create one out of low-level components that works for 4-bit words
def demux4word(ctrl4,in1):
    ctrl = ctrl4[0]+2*ctrl4[1]
    out4 = (0,0,0,0)
    out4[ctrl]=in1
    return out4


