# Combinational logic 

# Basic logic gates

def NOT(x): 
    return 1-x
    
def AND(a,b):
    return a*b

def OR(a,b):
    if a+b==0:
        return 0
    else:
        return 1 

# Derived logic gates
    
def XOR(a,b):
    return OR(AND(a,NOT(b)),AND(NOT(a),b))

    
def XNOR(a,b):
    return OR(AND(a,b),AND(NOT(a),NOT(b)))
    
def OR4(a,b,c,d):
    return OR(OR(a,b),OR(c,d))

def AND4(a,b,c,d):
    return AND(AND(a,b),AND(c,d))

