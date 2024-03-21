#!/usr/bin/env python3

# Dynamic memory allocation using pages and a bitmap

# We allocate 16 bytes per page
PAGE_SZ = 16 # in bytes
# We have a total of 256 pages, so we can allocate at most 4kB
N_PAGES = 1024>>2 
VMEM_START = 64*1024-PAGE_SZ*N_PAGES

# N_PAGES bits, packed in bytes mean N_PAGES/8 entries, so with the above, the bitmap will take 64 bytes
# 0 means free
bitmap = [0] * (N_PAGES>>3)

# Takes the number of bytes to be allocated
# returns a pointer, i.e. the address of the start of the allocated memory region
def malloc(n_bytes) :
    for idx in range(N_PAGES):
        if alloc_sz_is_free_at_idx(idx, n_bytes):
            claim_alloc_sz_at_idx(idx, n_bytes)
            return (idx*PAGE_SZ+VMEM_START)
    return 0 # Null pointer

def free(ptr,n_bytes) :
    idx = (ptr-VMEM_START)/PAGE_SZ
    free_alloc_sz_at_idx(idx, n_bytes)

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
