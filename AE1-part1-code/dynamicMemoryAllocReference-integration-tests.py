#!/usr/bin/env python3

# Dynamic memory allocation using pages and a bitmap
from DynamicMemoryAllocReference import malloc, free, N_PAGES


for mem_sz in range(1,55+1):
    ptr = malloc(mem_sz) # so for 1..16 we have 1 page each; for 17, 18 etc we need to pages 
    print(mem_sz,': ',ptr)
    if (mem_sz>=30 and mem_sz<=40 and ptr<N_PAGES):
        free(ptr,mem_sz)
