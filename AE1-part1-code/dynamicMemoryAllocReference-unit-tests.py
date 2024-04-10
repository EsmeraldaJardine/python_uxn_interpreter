#!/usr/bin/env python3

# Dynamic memory allocation using pages and a bitmap

from DynamicMemoryAllocReference import *

# We allocate 16 bytes per page
# PAGE_SZ = 16 # in bytes
# We have a total of 256 pages, so we can allocate at most 4kB
# N_PAGES = 1024>>2 
# VMEM_START = 64*1024-PAGE_SZ*N_PAGES

# N_PAGES bits, packed in bytes mean N_PAGES/8 entries, so with the above, the bitmap will take 64 bytes
# 0 means free
# bitmap = [0] * (N_PAGES>>3)


def testMaskClear():
    print("Test for mask_clear(bit_idx)")
    print( mask_clear(0x000) == 0xfe )
    print( mask_clear(0x0001) == 0xfd )
    print( mask_clear(0x0002) == 0xfb )
    print( mask_clear(0x0003) == 0xf7 )
    print( mask_clear(0x0004) == 0xef )
    print( mask_clear(0x0005) == 0xdf )
    print( mask_clear(0x0006) == 0xbf )
    print( mask_clear(0x0007) == 0x7f )

def testMaskSet():
    print("Test for mask_set(bit_idx)")
    print( mask_set(0x0000) == 0x01 )
    print( mask_set(0x0001) == 0x02 )
    print( mask_set(0x0002) == 0x04 )
    print( mask_set(0x0003) == 0x08 )
    print( mask_set(0x0004) == 0x10 )
    print( mask_set(0x0005) == 0x20 )
    print( mask_set(0x0006) == 0x40 )
    print( mask_set(0x0007) == 0x80 )

# ( define your tests here )
# ( 1/ test with 8 bytes in different locations with a different bit set )
# ( 2/ test with 8 bytes in different locations with multiple bits set )
# ( In both cases, read bits that are set and not set )
def testGetBit():
    print("Test for get_bit(idx)")
    bitmap[0x0001] = 0x01 # positions: 16=1,15=0 ) 
    bitmap[0x0003] = 0x80 # positions: 24=1,25=0 )
    bitmap[0x0004] = 0x02 # positions: 39=1,40=0 )
    bitmap[0x0008] = 0x40 # positions: 65=1,66=0 ) 
    bitmap[0x000c] = 0x04 # positions: 101=1,102=0 )
    bitmap[0x000d] = 0x20 # position: 114=1,115=9 )

    print( get_bit(0x000f) , get_bit(0x000e) )
    print( get_bit(24) , get_bit(25) )
    print( get_bit(38) , get_bit(39) )
    print( get_bit(65) , get_bit(66) )
    print( get_bit(101) , get_bit(102) )
    print( get_bit(106) , get_bit(107) )

    bitmap[0x0001] = 0x03 # positions: 16=1,15=0 ) 
    bitmap[0x0003] = 0xc0 # positions: 24=1,25=0 )
    bitmap[0x0004] = 0x06 # positions: 39=1,40=0 )
    bitmap[0x0008] = 0x60 # positions: 65=1,66=0 ) 
    bitmap[0x000c] = 0x0c # positions: 101=1,102=0 )
    bitmap[0x000d] = 0x30 # position: 114=1,115=9 )

    print( get_bit(0x000f) , get_bit(0x000e) )
    print( get_bit(24) , get_bit(25) )
    print( get_bit(38) , get_bit(39) )
    print( get_bit(65) , get_bit(66) )
    print( get_bit(101) , get_bit(102) )
    print( get_bit(106) , get_bit(107) )

def testClearBit():
    print("Test for clear_bit(idx)")
    clear_bit(15)
    clear_bit(14)
    clear_bit(24)
    clear_bit(25)
    clear_bit(38)
    clear_bit(39)
    clear_bit(65)
    clear_bit(66)
    clear_bit(101)
    clear_bit(102)
    clear_bit(106)
    clear_bit(107)

    print( get_bit(15) , get_bit(14) )
    print( get_bit(24) , get_bit(25) )
    print( get_bit(38) , get_bit(39) )
    print( get_bit(65) , get_bit(66) )
    print( get_bit(101) , get_bit(102) )
    print( get_bit(106) , get_bit(107) )

def testSetBit():
    print("Test for set_bit(idx)")
    set_bit(15)
    set_bit(14)
    set_bit(24)
    set_bit(25)
    set_bit(38)
    set_bit(39)
    set_bit(65)
    set_bit(66)
    set_bit(101)
    set_bit(102)
    set_bit(106)
    set_bit(107)

    print( get_bit(15) , get_bit(14) )
    print( get_bit(24) , get_bit(25) )
    print( get_bit(38) , get_bit(39) )
    print( get_bit(65) , get_bit(66) )
    print( get_bit(101) , get_bit(102) )
    print( get_bit(106) , get_bit(107) )


def testAllocSzIsFreeAtIdx():
    print("Test for alloc_sz_is_free_at_idx(idx,alloc_sz)")
# All 0
    print("part1")
    print (alloc_sz_is_free_at_idx(15, 1))
    print (alloc_sz_is_free_at_idx(15, 2))
    print (alloc_sz_is_free_at_idx(15, 4))
    print (alloc_sz_is_free_at_idx(15, 8))
    print (alloc_sz_is_free_at_idx(15, 16))
# Last is 0 because 24 is set
    print("part2")
    print (alloc_sz_is_free_at_idx(16, 1))
    print (alloc_sz_is_free_at_idx(16, 2))
    print (alloc_sz_is_free_at_idx(16, 4))
    print (alloc_sz_is_free_at_idx(16, 8))
    print (alloc_sz_is_free_at_idx(16, 16))
# 11100 because 24 is set
    print("part3")
    print (alloc_sz_is_free_at_idx(17, 1))
    print (alloc_sz_is_free_at_idx(17, 2))
    print (alloc_sz_is_free_at_idx(17, 4))
    print (alloc_sz_is_free_at_idx(17, 8))
    print (alloc_sz_is_free_at_idx(17, 16))
# All one
    print("part4")
    print (alloc_sz_is_free_at_idx(108, 1))
    print (alloc_sz_is_free_at_idx(108, 2))
    print (alloc_sz_is_free_at_idx(108, 4))
    print (alloc_sz_is_free_at_idx(108, 8))
    print (alloc_sz_is_free_at_idx(108, 16))

def testClaimAllocSzAtIdx() : 
    print("Test for claim_alloc_sz_at_idx(idx,alloc_sz)")
    print("part1")
    # claim alloc of 1,2,3,4,5 starting at 0 
    b0=bitmap[0] # stash first 2 bytes 
    b1=bitmap[1]
    bitmap[0]=0
    bitmap[1]=0 # clear the bitmap's first 2 bytes 
    claim_alloc_sz_at_idx(0x0000, 0x0001) # ( 1000 000 )
    print(hex( bitmap[0]), bitmap[0] == 0x80)  
    claim_alloc_sz_at_idx(0x0001, 0x0002) #  ( 1110 0000, is 1100 0000 )
    print(hex( bitmap[0]), bitmap[0] == 0xe0 )
    claim_alloc_sz_at_idx(0x0003, 0x0003) #  ( 1111 1100, is 1101 1100 )
    print(hex(bitmap[0]), bitmap[0] == 0xfc )
    claim_alloc_sz_at_idx(0x0006, 0x0004 ) #  ( 1111 1111 1100 0000 , is 1101 1111 1000 0011 )
    print(hex(bitmap[0]), hex(bitmap[1]),end=' ')
    print(bitmap[0]== 0xff and bitmap[1] == 0xc0)
    claim_alloc_sz_at_idx(0x000a, 0x0005 ) #  ( 1111 1111 1100 0000 , is 1101 1111 1000 0011 )
    print(hex(bitmap[0]),hex(bitmap[1]),end=' ')
    print( bitmap[0]==0xff and bitmap[1] == 0xfe)
    # restore to previous state 
    bitmap[0]=b0
    bitmap[1]=b1

    print("part2")
    # claim alloc
    claim_alloc_sz_at_idx(108, 16)
    # check if region beyond it is free, prints 1
    print (alloc_sz_is_free_at_idx(124, 16))
    # check if region itself is claimed, prints 0
    print (alloc_sz_is_free_at_idx(108, 16))
    
def testFreeAllocSzAtIdx() : 
    print("Test for free_alloc_sz_at_idx(idx,alloc_sz)")
    free_alloc_sz_at_idx(108,16)
    print (alloc_sz_is_free_at_idx(124, 16))
    print (alloc_sz_is_free_at_idx(108, 16))

# unit tests
testMaskClear()
testMaskSet()
testGetBit()
testClearBit()
testSetBit()
setBitmap()
testAllocSzIsFreeAtIdx()
testClaimAllocSzAtIdx()
testFreeAllocSzAtIdx()