#! Comments of this style (`#!` or `#!!`) indicate code that needs completing or changing
#! A `#!!` means "must"
#! "should" or "must" means you'll lose marks if you don't do it
#! "could" or "(optional)" means you can get extra marks for doing it, but you don't lose marks for not doing it

from enum import Enum

#! Your program could set these flags on command line
V = False # Verbose, explain a bit what happens
VV = False # More verbose, explain in more detail what happens
DBG = False # Debug info

#!! Your program should read the program text from a `.tal` file
programText = """
|0100 
;array LDA 
;array #01 ADD LDA 
ADD 
;print JSR2 
BRK 

@print 
    #18 DEO 
JMP2r 

@array 11 22 33
"""

# These are the different types of tokens
class T(Enum):
    MAIN = 0
    LIT = 1
    INSTR = 2
    LABEL = 3
    REF = 4
    RAW = 5
    ADDR = 6
    PAD = 7
    EMPTY = 8

# We use an object to group the data structures used by the Uxn interpreter
class Uxn:
    memory = [(T.EMPTY,)] * 0x10000 # The memory stores *tokens*, not bare values
    stacks = ([],[]) # ws, rs # The stacks store bare values, i.e. bytes
    progCounter = 0 
    symbolTable={}
    # First unused address, only used for verbose
    free = 0

# These are the actions related to the various Uxn instructions

# Memory operations
# STA
def store(args,uxn):
    uxn.memory[args[1]] = ('RAW',args[0],0)
# LDA
def load(args, uxn):
    return uxn.memory[args[0]][1] # memory has tokens, stacks have values

# Control operations
# JSR
def call(args,uxn):
    # print("CALL:",args[0],uxn.progCounter)
    uxn.stacks[1].append(uxn.progCounter)
    uxn.progCounter = args[0]-1
# JMP
def jump(args,uxn):
    uxn.progCounter = args[0]
# JCN
def condJump(args,uxn):
    if args[0] ==0 :
        uxn.progCounter =  uxn.progCounter+1 
    else:
        uxn.progCounter = args[0]
# Stack manipulation operations
# STH
def stash(rs,uxn):
    uxn.stacks[1-rs].append(uxn.stacks[rs].pop())
# SWP
def swap(rs,uxn):
    a = uxn.stacks[rs].pop()
    b = uxn.stacks[rs].pop()
    uxn.stacks[rs].append(a)
    uxn.stacks[rs].append(b)

#!! Implement NIP
#! def nip(rs,uxn):
#!    ...

# ALU operations
# ADD
def add(args,uxn):
    return args[0] + args[1]

#!! Implement SUB, MUL, DIV
#! def sub(args,uxn):
#!    ...
# def mul(args,uxn):
#!    ...
# def div(args,uxn):
#!    ...

#!! Implement EQU, NEQ, LTH, GTH
#! def equ(args,uxn):
#!    ...
# def neq(args,uxn):
#!    ...
# def lth(args,uxn):
#!    ...
# def gth(args,uxn):
#!    ...

callInstr = {
    'ADD' : (add,2,True),
#!! Add SUB, MUL, DIV; EQU, NEQ, LTH, GTH
    'DEO' : (lambda args,uxn : print(args[1]),2,False),
    'JSR' : (call,1,False),
    'JMP' : (jump,1,False),
    'JCN' : (condJump,2,False),
    'LDA' : (load,1,True),
    'STA' : (store,2,False), 
    'STH' : (stash,0,False),
#!! Add NIP 
    'POP' :(lambda rs,uxn : uxn.stacks[rs].pop(),0,False)
}

def executeInstr(token,uxn):
    _t,instr,sz,rs,keep = token
    if instr == 'BRK':
        print('*** DONE *** ')
        if V:
            print('PC:',uxn.progCounter,' (WS,RS):',uxn.stacks)
        exit(0)
    action,nArgs,hasRes = callInstr[instr]
    if nArgs==0: # means it is a stack manipulation
        action(rs,uxn)
    else:
        args=[]
        for i in range(0,nArgs):
            if keep == 0:
                args.append(uxn.stacks[rs].pop())
            else:
                args.append(uxn.stacks[rs][i])
        if hasRes:
            res = action(args,uxn)
            uxn.stacks[rs].append(res)
        else:
            action(args,uxn)

#!! Tokenise the program text using a function `tokeniseProgramText` 
#! That means splitting the string `programText` on whitespace 
#! You must remove any comments first, I suggest you use a helper function stripComments
#! `tokenStrings` is a list of all tokens as strings
def tokeniseProgramText(programText):
    #! ...
    return [] #! replace this with the actual code

#!! Complete the parser
def parseToken(tokenStr):
    if tokenStr[0] == '#':
        valStr=tokenStr[1:]
        val = int(valStr,16)
        if len(valStr)==2:
            return (T.LIT,val,1)
        else:
            return (T.LIT,val,2)        
    elif tokenStr[0] == ';':
        val = tokenStr[1:]
        return (T.REF,val)
#!! Handle relative references `,`
    # elif tokenStr[0] == ...
    #     ...
    #     return (...)
    elif tokenStr[0] == '@':
        val = tokenStr[1:]
        return (T.LABEL,val)
#!! Handle relative labels `&`
    # elif tokenStr[0] == ...
    #     ...
    #     return (...)
    elif tokenStr == '|0100':
        return (T.MAIN,)
#! Handle absolute padding (optional)
    # elif tokenStr[0] == ...
    #     ...
    #     return (...)
#! Handle relative padding (optional)
    # elif tokenStr[0] == ...
    #     ...
    #     return (...)
    elif tokenStr[0].isupper():
        # Any token string starting with an uppercase letter is considered an instruction
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
            # Order must be size:stack:keep
            if tokenStr[len(tokenStr)-2:len(tokenStr)] == '2r':
                return (T.INSTR,tokenStr[0:len(tokenStr)-2],2,1,0)
            elif tokenStr[len(tokenStr)-2:len(tokenStr)] == '2k':
                return (T.INSTR,tokenStr[0:len(tokenStr)-2],2,0,1)
            elif tokenStr[len(tokenStr)-2:len(tokenStr)] == 'rk':
                return (T.INSTR,tokenStr[0:len(tokenStr)-2],1,1,1)
        elif len(tokenStr) == 6:
            return (T.INSTR,tokenStr[0:len(tokenStr)-1],2,1,1)
    else:
        # we assume this is a 'raw' byte or short
        return (T.RAW,int(tokenStr,16))

# This is the first pass of the assembly process
# We store the tokens in memory and build a dictionary
# uxn.symbolTable: label => address 
def populateMemoryAndbuildSymbolTable(tokens,uxn):
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

# Once the symbol table has been built, replace every symbol by its address
#!! Implement the code to replace every label reference by an address
#! Note that label references are `REF` tokens and the memory stores the symbolTable as `LIT` tokens
    
#! def resolveSymbols(uxn):
#!  ...

# Running the program mean setting the program counter `uxn.progCounter` to the address of the first token;
#  - read the token from memory at that address
# - if the token is a LIT, its *value* goes on the working stack
# - otherwise it is an instruction and it is executed using `executeInstr(token,uxn)`
# - then we increment the program counter
#!! Implement the above functionality
def runProgram(uxn):
    if VV:
        print('*** RUNNING ***')
    uxn.progCounter = 0x100 # all programs must start at 0x100
    while True:
#!! read the token from memory at that address
        #! token = ...
        if DBG:
            print('PC:',uxn.progCounter,' TOKEN:',token)
        #! You can use an if/elif if you prefer
        #! match ...:
        #!     case ...:
        #!         ...
        #!     case ...:
        #!         ...
#!! Increment the program counter
        #! ...
        if DBG:
            print('(WS,RS):',uxn.stacks)

uxn = Uxn()

tokenStrings = tokeniseProgramText(programText)
tokens = map(parseToken,tokenStrings)

populateMemoryAndbuildSymbolTable(tokens,uxn)

resolveSymbols(uxn)

if DBG:
    for pc in range(256,uxn.free):
        print(pc,':',uxn.memory[pc])
if VV:
    print(programText)

runProgram(uxn)

