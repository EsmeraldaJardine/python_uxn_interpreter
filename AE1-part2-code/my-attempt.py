# name: Esmeralda Jardine
# ID: 2391491
# Python Interpreter Program for uxntal
from enum import Enum

WW = False
V = False
VV = False
DBG = False
 
programText = """
( A Hello World example )
|0100
 
    ;hello_world
    &while

        LDAk #18 DEO ( what we do here is read a character from the string and print it
        But the 'k' means we keep the address on the stack as well )
        INC2 LDAk ( we increment the address and load it to get the next character.
        Again we keep the address on the stack )
        #00 NEQ ( so we test if the character value is not equal to zero )
        ,&while JCN ( JCN means "jump with condition, it means we go back to the label &while as long as the condition is true. The last character in the string is a zero byte, so when we read that the condition is false and we finish )
    POP2 ( clean up the stack )
BRK
( Constant strings are usually stored with a label like this )
( In Java this would be
public static final String hello_world = "Hello, World!";
The reason for the 20 is that in Uxntal, you can't have a space in a string, so you need to write the ASCII value for the space instead. )
@hello_world "Hello, 20 "World! 00
 
"""

 

class T(Enum):
    MAIN = 0 # Main program
    LIT = 1 # Literal
    INSTR = 2 # Instruction
    LABEL = 3 # Label
    REF = 4 # Address reference (rel=1, abs=2)
    RAW = 5 # Raw values (i.e. not literal)
    ADDR = 6 # Address (absolute padding)
    PAD = 7 # Relative padding)
    EMPTY = 8 # Memory is filled with this by default

 

class Uxn:
    memory = [(T.EMPTY,)] * 0x10000
    stacks = ([],[])
    progCounter = 0
    symbolTable={}
    free = 0

 

def parseToken(tokenStr):
    if tokenStr[0] == '#':
        valStr=tokenStr[1:]
        val = int(valStr,16)
        if len(valStr)==2:
            return (T.LIT,val,1)
        else:
            return (T.LIT,val,2)
    if tokenStr[0] == '"':
        chars =list(tokenStr[1:])
        return list(map(lambda c: (T.LIT, ord(c),1),chars))
    elif tokenStr[0] == ';':
        val = tokenStr[1:]
        return (T.REF,val,2)
    elif tokenStr[0:2] == ',&':
        val = tokenStr[2:]
        return (T.REF,val,1)
    elif tokenStr[0] == '@':
        val = tokenStr[1:]
        return (T.LABEL,val,)
    elif tokenStr[0] == '&':
        val = tokenStr[1:]
        return (T.LABEL, val)
    elif tokenStr == '|0100':
        return (T.MAIN,)
    elif tokenStr[0] == '|':
        val = int(tokenStr[1:],16)
        return (T.ADDR, val)
    elif tokenStr[0] == '$':
        val = int(tokenStr[1:],16)
        return (T.PAD, val)
    elif tokenStr[0].isupper():
        if len(tokenStr) == 3:
            return (T.INSTR,tokenStr[0:len(tokenStr)],1,0,0)
        elif len(tokenStr) == 4:
            if tokenStr[-1] == '2':
                return (T.INSTR,tokenStr[0:len(tokenStr)-1],2,0,0)
            elif tokenStr[-1] == 'r':
                return (T.INSTR,tokenStr[0:len(tokenStr)-1],1,1,0)
            elif tokenStr[-1] == 'k':
                return (T.INSTR,tokenStr[0:len(tokenStr)-1],1,0,1)
        elif len(tokenStr) == 5:
            if tokenStr[len(tokenStr)-2:len(tokenStr)] == '2r':
                return (T.INSTR,tokenStr[0:len(tokenStr)-2],2,1,0)
            elif tokenStr[len(tokenStr)-2:len(tokenStr)] == '2k':
                return (T.INSTR,tokenStr[0:len(tokenStr)-2],2,0,1)
            elif tokenStr[len(tokenStr)-2:len(tokenStr)] == 'rk':
                return (T.INSTR,tokenStr[0:len(tokenStr)-2],1,1,1)
        elif len(tokenStr) == 6:
            return (T.INSTR,tokenStr[0:len(tokenStr)-1],2,1,1)
    else:
        return (T.RAW,int(tokenStr,16))

 

# These are the actions related to the various Uxn instructions
# Memory operations

def store(args,sz,uxn):
    uxn.memory[args[0]] = ('RAW',args[1],0)

def load(args,sz, uxn):
    return uxn.memory[args[0]][1]

# Control operations
def call(args,sz,uxn):
    uxn.stacks[1].append( (uxn.progCounter,2) )
    uxn.progCounter = args[0]-1
 
def jump(args,sz,uxn):
    uxn.progCounter = args[0]
   
def condJump(args,sz,uxn):
    if args[1] == 1 :
        uxn.progCounter = args[0]-1


# Stack manipulation operations
def stash(rs,sz,uxn):
    uxn.stacks[1-rs].append(uxn.stacks[rs].pop())
 
def pop(rs,sz,uxn):
    uxn.stacks[rs].pop()
 
def swap(rs,sz,uxn):
        b = uxn.stacks[rs].pop()
        a = uxn.stacks[rs].pop()
        uxn.stacks[rs].append(b)
        uxn.stacks[rs].append(a)
 
def nip(rs,sz,uxn):
        b = uxn.stacks[rs].pop()
        if b[1]==sz:
            a = uxn.stacks[rs].pop()
            if a[1]==sz:
                uxn.stacks[rs].append(b)
            else:
                print("Error: Args on stack for NIP",sz,"are of wrong size")
                exit()
        elif b[1]==2 and sz==1:
            bb = b[0]&0xFF
            uxn.stacks[rs].append( (bb,1) )
        elif b[1]==1 and sz==2:
            print("Error: Args on stack for NIP",sz,"are of wrong size")
            exit()

def rot(rs,sz,uxn):
        c = uxn.stacks[rs].pop()
        b = uxn.stacks[rs].pop()
        a = uxn.stacks[rs].pop()
        uxn.stacks[rs].append(b)
        uxn.stacks[rs].append(c)
        uxn.stacks[rs].append(a)
 
def dup(rs,sz,uxn):
        a = uxn.stacks[rs][-1]
        uxn.stacks[rs].append(a)
 
def over(rs,sz,uxn):
        a = uxn.stacks[rs][-2]
        uxn.stacks[rs].append(a)
 
# ALU operations
def add(args,sz,uxn):
    return args[0] + args[1]
 
def sub(args,sz,uxn):
    return args[1] - args[0]

def mul(args,sz,uxn):
    return args[0] * args[1]
 
def div(args,sz,uxn):
    return args[1] // args[0]
 
def inc(args,sz,uxn):
    return args[0] + 1
 
def equ(args,sz,uxn):
    if args[0] == args[1]:
        return 1
    else:
        return 0
 
def neq(args,sz,uxn):
    if args[0] != args[1]:
        return 1
    else:
        return 0
 
def lth(args,sz,uxn):
    if args[0] < args[1]:
        return 1
    else:
        return 0
 

def gth(args,sz,uxn):
    if args[0] > args[1]:
        return 1
    else:
        return 0

 
callInstr = {
    'ADD' : (add,2,True),
    'SUB' : (sub,2,True),
    'MUL' : (mul,2,True),
    'DIV' : (div,2,True),
    'INC' : (inc,1,True),
    'EQU' : (equ,2,True),
    'NEQ' : (neq,2,True),
    'LTH' : (lth,2,True),
    'GTH' : (gth,2,True),
    'DEO' : (lambda args,sz,uxn : print(chr(args[1]),end=''),2,False),
    'JSR' : (call,1,False),
    'JMP' : (jump,1,False),
    'JCN' : (condJump,2,False),
    'LDA' : (load,1,True),
    'STA' : (store,2,False),
    'STH' : (stash,0,False),
    'DUP' : (dup,0,False),
    'SWP' : (swap,0,False),
    'OVR' : (over,0,False),
    'NIP' : (nip,0,False),
    'POP' : (pop,0,False),
    'ROT' : (rot,0,False)
}
 
def executeInstr(token,uxn):
    _t,instr,sz,rs,keep = token
    if instr == 'BRK':
        if V:
            print("\n",'*** DONE *** ')
        else:
            print('')
        if VV:
            print('PC:',uxn.progCounter,' (WS,RS):',uxn.stacks)
        exit(0)
    action,nArgs,hasRes = callInstr[instr]
    if nArgs==0:
        action(rs,sz,uxn)
    else:
        args=[]
        for i in reversed(range(0,nArgs)):
            if keep == 0:
                arg = uxn.stacks[rs].pop()
                if arg[1]==2 and sz==1 and (instr != 'LDA' and instr!= 'STA'):
                    if WW:
                        print("Warning: Args on stack for",instr,sz,"are of wrong size (short for byte)")
                    uxn.stacks[rs].append((arg[0]>>8))
                    args.append((arg[0]&0xFF))
                else:
                    args.append(arg[0])
                    if arg[1]==1 and sz==2:
                        arg1 = arg
                        arg2 = uxn.stacks[rs].pop()
                        if arg2[1]==1 and sz==2:
                            arg = (arg2[0]<<8) + arg1[0]
                            args.append(arg)
                        else:
                            print("Error: Args on stack are of wrong size (short after byte)")
                            exit()
            else:
                arg = uxn.stacks[rs][i]
                if arg[1]!= sz and (instr != 'LDA' and instr!= 'STA'):
                    print("Error: Args on stack are of wrong size (keep)")
                    exit()
                else:
                    args.append(arg[0])
        if VV:
            print('EXEC INSTR:',instr, 'with args', args)
        if hasRes:
            res = action(args,sz,uxn)
            if instr == 'EQU' or instr == 'NEQ' or instr == 'LTH' or instr == 'GTH':
                uxn.stacks[rs].append( (res,1) )
            else:
                uxn.stacks[rs].append( (res,sz) )
        else:
            action(args,sz,uxn)
 
def tokeniseProgramText(programText):
    tokenStrings = []
    strippedProgramText = stripComments(programText)
    tokens = strippedProgramText.split()
    tokenStrings.extend(tokens)
    return tokenStrings
 

def stripComments(programText):
    lines = programText.split('\n')
    strippedLines = []
    withinComment = False
    for line in lines:
        if not withinComment:
            if '(' in line:
                if ')' not in line:
                    withinComment = True
                strippedLine = line[:line.index('(')]
            else:
                strippedLine = line
        else:
            if ')' in line:
                withinComment = False
                strippedLine = line[line.index(')')+1:]
            else:
                strippedLine = ''
        if strippedLine:
            strippedLines.append(strippedLine)
    return '\n'.join(strippedLines)
        

        
def populateMemoryAndBuildSymbolTable(tokens,uxn):
    pc = 0
    for token in tokens:
        if token == (T.MAIN,):
            pc = 0x0100
        elif token[0] == T.ADDR:
            pc = token[1]
        elif token[0] == T.PAD:
            pc = pc + token[1]
        elif token[0] == T.LABEL:
            labelName = token[1]
            uxn.symbolTable[labelName]=pc
        else:
            uxn.memory[pc]=token
            pc = pc + 1
    uxn.free = pc
 
def resolveSymbols(uxn):
        for i, token in enumerate(uxn.memory):
            if token[0] == T.REF:
                refAddressToken = (T.LIT, uxn.symbolTable[token[1]], token[2])
                uxn.memory[i] = refAddressToken
 
def runProgram(uxn):
    if VV:
        print('*** RUNNING ***')
    uxn.progCounter = 0x100
    while True:
        token = uxn.memory[uxn.progCounter]
        if DBG:
            print('PC:',uxn.progCounter,' TOKEN:',token)
        if token[0] == T.LIT:
            uxn.stacks[0].append(token[1:])
        elif token[0] == T.INSTR:
            executeInstr(token,uxn)
        else:
            print("Error: Unknown token type")
        uxn.progCounter = uxn.progCounter + 1
        if DBG:
            print('(WS,RS):',uxn.stacks)
 

uxn = Uxn()
tokenStrings = tokeniseProgramText(programText)
tokensWithStrings = map(parseToken,tokenStrings)
tokens=[]
for item in tokensWithStrings:
    if type(item) == list:
        for token in item:
            tokens.append(token)
    else:
        tokens.append(item)
populateMemoryAndBuildSymbolTable(tokens,uxn)
resolveSymbols(uxn)
if DBG:
    for pc in range(256,uxn.free):
        print(pc,':',uxn.memory[pc])
    print('')
if VV:
    print(programText)
runProgram(uxn)