# Combinational logic 

# Basic logic gates

def NOT(x): 
    return 1-x
    
def AND(a,b):
    return a and b

def OR(a,b):
    return a or b

# Derived logic gates
    
def XOR(a,b):
    return OR(AND(a,NOT(b)),AND(NOT(a),b))

def XNOR(a,b):
    return OR(AND(a,b),AND(NOT(a),NOT(b)))
    
def OR4(a,b,c,d):
    return OR(OR(a,b),OR(c,d))

def AND4(a,b,c,d):
    return AND(AND(a,b),AND(c,d))

