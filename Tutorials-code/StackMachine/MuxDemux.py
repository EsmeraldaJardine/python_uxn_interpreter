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

# Bit-size demux, 2 bits control, data 1 in to 4 out
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

# Word-size mux, 1-bit control, 2 in to 1 out, implemented high-level to work with words of arbitrary size
def mux2word(ctrl,in2):
    return in2[ctrl]

# Word-size mux, 4 in to 1 out, implemented high-level to work with words of arbitrary size
def mux4word(ctrl4,in4):
    ctrl = ctrl4[0]+2*ctrl4[1]
    return in4[ctrl]

# Word-size demux, 1 in to 4 out, implemented high-level to work with words of arbitrary size
def demux4word(ctrl4,in1):
    ctrl = ctrl4[0]+2*ctrl4[1]
    out4 = (0,0,0,0)
    out4[ctrl]=in1
    return out4

#! Create a 2-port mux for 4-bit words, mux2word4bits, out of low-level components
#! Create a 4-port demux for 4-bit words, demux4word4bits, out of low-level components
#! Create a 4-port mux for 4-bit words, mux4word4bits, out of low-level components
