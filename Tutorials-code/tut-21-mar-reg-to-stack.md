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

We can mark every line with a label, and this label can be used as an address, for example:

	ADD_LINE:
		ADD r1 r2 r3
	JMP_LINE:
		JNZ r3 ADD_LINE

We can also store the label in a register (the assembler will turn it into an address).

	CONST LOOP r1
	LOOP:
		ADD r1 r2 r3
		JNZ r3 r1


Suppose we have the following program:

	CONST 0x1 r0
	CONST 0x5 r1
	CONST 0x1 r2
	LOOP:
		MUL r1 r2 r2
		SUB r1 r0 r1
		JNZ r1 LOOP
	HALT

### Question 1

Explain the program:
* What does every instruction in this program do?
* What does the overall program do?

### Question 2

Suppose that instead of these 4 registers, you have a single 4-element stack, so we have a stack machine. This means any instruction must operate on the stack: 
- either it pushes arguments onto the stack 
- or it takes arguments off the stack and pushes its result(s) onto the stack

If we try to take an item off an empty stack, the machine will raise a stack underflow exception
If we try to push an item onto a full stack, the machine will raise a stack overflow exception

* How would the instructions change? Write out the modified instructions.

* What would need to change to the instruction set so that the program can work? You don't have to come up with a working instruction set, only identify what kind of instructions are missing from the instruction set. You don't have to design a working program either.

### Question 3

Suppose that the register machine had a memory, and you could access it with two extra instructions:

	LOAD <register, memory address or label> <register for result>
	STORE <register or constant> <register, memory address or label>

* What would these instructions look like for the stack machine?
* Would you still need to change the instruction set to make the program work?



