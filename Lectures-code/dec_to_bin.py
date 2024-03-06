dec = 233
def dec_to_bin(dec):
	n=0
	bits = []
	while dec>0:
		m = 256>>n 
		remainder = dec % m
		n+=1
		bits.append(1 if (remainder != dec) else 0)
		dec = remainder
	return bits
bits = dec_to_bin(dec)
print(bits)

def bits_to_dec(bits):
	dec = 0
	n=0
	for bit in bits:
		dec+=bit*(256>>n) 
		n=n+1
	return dec

dec_rec = bits_to_dec(bits)
print(dec_rec)
