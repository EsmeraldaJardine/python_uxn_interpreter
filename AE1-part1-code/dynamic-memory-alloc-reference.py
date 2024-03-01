#!/usr/bin/env python3

# Dynamic memory allocation using pages and a bitmap

# We allocate 16 bytes per page, so 16kB
PAGE_SZ = 16 # in bytes
N_PAGES = 1024>>2 

# N_PAGES bits, packed in bytes mean N_PAGES/8 entries
# 0 means free
bitmap = [0] * (N_PAGES>>3)

def malloc(mem_sz) :
    for idx in range(N_PAGES):
        if alloc_sz_is_free_at_idx(idx, mem_sz):
            claim_alloc_sz_at_idx(idx, mem_sz)
            return (idx*PAGE_SZ)
    return N_PAGES*PAGE_SZ

def free(idx,mem_sz) :
    free_alloc_sz_at_idx(idx, mem_sz)

def get_bit(idx) :
    byte_idx = idx >> 3
    bit_idx = 7 - (idx - (byte_idx<<3))
    if byte_idx > N_PAGES-1:
        print("Outside of page range: ", byte_idx)
        exit(0)
    byte = bitmap[byte_idx]
    if byte is None:
        print("Invalid access:", byte_idx)
        exit(0)
    bit = (byte >> bit_idx) & 0x01
    return bit

def set_bit(idx) :
    byte_idx = idx >> 3
    bit_idx = 7 - idx + (byte_idx<<3)
    byte = bitmap[byte_idx]
    mask = 1 << bit_idx
    bitmap[byte_idx] = byte | mask

def clear_bit(idx) :
    byte_idx = idx >> 3
    bit_idx = 7 - idx + (byte_idx<<3)
    byte = bitmap[byte_idx]
    mask = 0xFF ^ (1 << bit_idx) # 1110111
    bitmap[byte_idx] = byte & mask


# allocation size is in pages
def alloc_sz_is_free_at_idx(idx, alloc_sz) :
    for jj in range(alloc_sz) :
        if(idx+jj>N_PAGES-1):
            return 0 
        if (get_bit(idx+jj)==1):
            return 0 
    return 1

def claim_alloc_sz_at_idx(idx, alloc_sz) : 
    for jj in range(alloc_sz) :
        set_bit(idx+jj)

def free_alloc_sz_at_idx(idx, alloc_sz) : 
    for jj in range(alloc_sz):
        clear_bit(idx+jj)

for mem_sz in range(1,55+1):
    ptr = malloc(mem_sz) 
    print(mem_sz,': ',ptr)
    if (mem_sz>=30 and mem_sz<=40 and ptr<N_PAGES):
        free(ptr,mem_sz)
