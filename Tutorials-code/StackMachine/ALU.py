# Combinational arithmetic operations, implemented high-level
def ALU(a,b,opcode):
    match opcode:
        case 0:
            res = a+b
            # print('+',a,b,res)
        case 1:
            res = a-b
        case 2:
            res = a*b
            # print('*',a,b,res)
        case 3:
            res=int(a/b)
    return res
