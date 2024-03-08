---
linkcolor: blue
---
# Tutorial 12 March 2024: Stack Machine

* From the git repo [https://git.dcs.gla.ac.uk/wim/cans/-/tree/main/Tutorials-code/StackMachine](https://git.dcs.gla.ac.uk/wim/cans/-/tree/main/Tutorials-code/StackMachine), get the Python source files.
* This is a Python implementation of a stack machine starting from basic gates. We use them to construct multiplexers and the register file.

## Task 1

* Go through the source files and familiarise yourself with the content
* Comments with a `#!` indicate something to add or modify to the source. The current code uses muxes and demuxes that are implemented in a high-level way so that they can work with words of any size. The aim of this task is to create corresponding muxes and demuxes for 4-bit words in `MuxDemux.py` and use these in `Stack.py` and `StackMachine.py`.

## Task 2

* Draw the block diagram for stack machine based on the source code. In particular, think of which parts of the circuit need a clock.