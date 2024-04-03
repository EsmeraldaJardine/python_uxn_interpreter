---
linkcolor: blue
---
# Tutorial 21 March 2024: register machine versus stack machine

Let's assume we have a register machine with 4 general-purpose registers `r0`,`r1`,`r2`,`r3`.
We have an assembly language with the following instructions:

	CONST <integer in hex OR label> <register> 
	ADD <register> <register> <register for result> (a+b)
	SUB <register> <register> <register for result> (a-b)
	MUL <register> <register> <register for result> (a*b)
	EQU <register> <register> <register for result> (a==b)
	JNZ <register> <register for address OR label of address> (jump if operand is not zero)
	HALT

We can mark every line with a label, and this label can be used as an address, sfor example:

	LOOP:
		ADD r1 r2 r3
		JNZ r3 LOOP

We can also store the label in a register (the assembler will turn it into an address).

	CONST LOOP r1
	LOOP:
		ADD r1 r2 r3
		JNZ r3 r1


Suppose we have the following program:

	CONST 0x1 r0
	CONST 0xa r1
	CONST 0x1 r2
	LOOP:
		MUL r1 r2 r2
		SUB r1 r0 r1
		JNZ r1 LOOP
	HALT

### Question 1

Explain the program:
* What does every instruction in this program do?

        CONST 0x1 r0 ; r0 = 1
        CONST 0xa r1 ; r1 = 5
        CONST 0x1 r2 ; r2 = 1
        LOOP:
            MUL r1 r2 r2 ; r2 = r1*r2
            SUB r1 r0 r1 ; r1=r1-r0
            JNZ r1 LOOP ; if r1!=0 then goto LOOP
        HALT

* What does the overall program do?

    It will compute the factorial of 5 by multiplying r2 with r1 and then decrementing r1, until r1 is 0. In Python:

		r0=1
		r1=5
		r2=1
		while r1>0:
			r2=r2*r1
			r1=r1-r0
	
### Question 2

Suppose that instead of these 4 registers, you have a single 4-element stack, so we have a stack machine. This means any instruction must operate on the stack: 
- either it pushes arguments onto the stack 
- or it takes arguments off the stack and pushes its result(s) onto the stack

If we try to take an item off an empty stack, the machine will raise a stack underflow exception
If we try to push an item onto a full stack, the machine will raise a stack overflow exception

* How would the instructions change? Write out the modified instructions.

The main change is that, apart from CONST, the instructions take no arguments

	CONST <integer in hex OR label> 
	ADD 
	SUB 
	MUL 
	EQU 
	JNZ
	HALT

* What would need to change to the instruction set so that the program can work? You don't have to come up with a working instruction set, only identify what kind of instructions are missing from the instruction set. You don't have to design a working program either.

Ther key difference is that you don't have registers to store values in. Values on the stack don't stay in a fixed position. You have essentially two choices: either your operations consume the values from the stack (this is most common) or they leave them. 

In the first case:

	CONST 0x1
	CONST 0x5
	CONST 0x1
    ( 1 5 1 )
	LOOP:
		MUL  ( 1 5*1=5 )
		SUB  ( 1-5=-4 )
		CONST LOOP JNZ 
	HALT

As you can see, this won't work at all: JNZ will remove -4 from the stack, and the next MUL will raise a stack underflow exception.

In the second case:

	CONST 0x1
	CONST 0x5
	CONST 0x1
    ( 1 5 1 )
	LOOP:
		MUL  ( 1 5 1 5*1=5 )
		SUB  ( 1 5 1 5 -4 )
		CONST LOOP JNZ
	HALT

Recall we have a 4-register stack. So the SUB will raise a stack overflow exception. This is because we keep on adding to the stack.

From this is should be clear that we need some way to manipulate the stack: we need instructions to
- change the order of items on the stack
- remove items from the stack
- copy items on the stack

### Question 3

Suppose that the register machine had a memory, and you could access it with two extra instructions:

	LOAD <register, memory address or label> <register for result>
	STORE <register or constant> <register, memory address or label>

* What would these instructions look like for the stack machine?

	LOAD 
	STORE

* Would you still need to change the instruction set to make the program work?

No, because with these two instructions, you could use the memory in the same way as you used registers.

	CONST 0x1 CONST 0x00 STORE
	CONST 0x5 CONST 0x01 STORE 
	CONST 0x1 CONST 0x02 STORE 
    ( 1 5 1 )
	LOOP:
		CONST 0x02 LOAD CONST 0x01 LOAD MUL CONST 0x02 STORE
		CONST 0x01 LOAD CONST 0x00 LOAD SUB CONST 0x01 STORE
		CONST 0x01 LOAD LOOP JNZ 
	HALT
