"""
This module contains functions that measure amount of entropy
in byte-type buffers using the shannon entropy algorithm
Reference: - https://en.wikipedia.org/wiki/Shannon_entropy

Entropy in this context is measuring the disorder in sequences of bytes.
e.g. repeating byte values like '\x30\x30\x30' would produce entropy of 0.0,
while representing all possible byte values (0x00 to 0xFF) will produce an entropy of 1.0

This can be used to statistically analyse data to infer what type of data it is.
For example compressed or encrypted data can have a high entropy, and so it can be used to detect
if a data set is compressed or encrypted.

If data is has been processed with a basic substitution type cipher, or additive cipher such as exclusive or,
the entropy of the plaintext and ciphertext are exactly the same, and so entropy measurement is useless.
This is because the probabilities of each symbol are still the same.

Algorithm adapted from C++ code from x64dbg project at
Reference: - https://github.com/x64dbg/x64dbg/blob/development/src/gui/Src/QEntropyView/Entropy.h
"""
import math

def ent(buffer):
	"""Measure the entropy of a group of bytes
	Returns a floating point entropy value between 0 and 1

	Keyword arguments:
	buffer -- a byte like buffer (bytearray, bytes) to measure
	"""
	occurrences = [];
	for i in range(0,256):
		occurrences.append(0)
	for x in buffer:
		occurrences[x]+=1
	entropy = 0
	logbase = math.log(256)
	p = 0
	for i in range(0,256):
		if(occurrences[i] == 0):
			continue
		p = float(occurrences[i] / float(len(buffer)))
		entropy += p * math.log(p) / logbase
	return -entropy

	
def listEnt(buffer, blocksize):
	"""Measure the entropy of a group of bytes in blocks
	Returns a list of values between 0 and 1
	
	Keyword arguments:
	buffer -- a byte like buffer (bytearray, bytes) to measure
	blocksize -- integer number defining how large each block is.
	"""
	nblocks = int(math.trunc(len(buffer)/blocksize))
	if(nblocks == 0):
		return
	if(nblocks == 1):
		return
	entropylist = []
	entropylist.append(ent(buffer[0:blocksize]))
	currentblock = 0
	nextblock = blocksize
	for i in range(nblocks):
		entropylist.append(ent(buffer[currentblock:nextblock]))
		currentblock+=blocksize
		nextblock+=blocksize
	return entropylist


def bitEnt(buffer):
	"""Measure the entropy of a group of bytes
	Returns a floating point entropy value between 0 and 8 (bits per byte)

	Keyword arguments:
	buffer -- a byte like buffer (bytearray, bytes) to measure
	"""
	entropy = ent(buffer)*8
	return entropy

def listBitEnt(buffer, blocksize):
	"""Measure the entropy of a group of bytes in blocks
	Returns a list of values between 0 and 8 (bits per byte)
	
	Keyword arguments:
	buffer -- a byte like buffer (bytearray, bytes) to measure
	blocksize -- integer number defining how large each block is.
	"""
	nblocks = int(math.trunc(len(buffer)/blocksize))
	if(nblocks == 0):
		return 0
	if(nblocks == 1):
		return ent(buffer[0:blocksize])
	entropylist = []
	currentblock = 0
	nextblock = blocksize
	for i in range(nblocks):
		entropylist.append(bitEnt(buffer[currentblock:nextblock]))
		currentblock+=blocksize
		nextblock+=blocksize
	return entropylist

