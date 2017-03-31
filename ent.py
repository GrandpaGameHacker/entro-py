"""
This module contains functions that measure amount of information
entropy in byte-type buffers using the shannon entropy algorthmn
Reference: - https://en.wikipedia.org/wiki/Shannon_entropy
Algorithm based on C++ code from x64dbg project at
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

	
def listent(buffer, blocksize):
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


def bitent(buffer):
	"""Measure the entropy of a group of bytes
	Returns a floating point entropy value between 0 and 8 (bits per byte)

	Keyword arguments:
	buffer -- a byte like buffer (bytearray, bytes) to measure
	"""
	entropy = ent(buffer)*8
	return entropy

def listbitent(buffer, blocksize):
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
		entropylist.append(bitent(buffer[currentblock:nextblock]))
		currentblock+=blocksize
		nextblock+=blocksize
	return entropylist

