"""
This module contains functions that wrap ent.py for use with files
"""
import ent as e

def ent(file):
	"""
	Measure the entropy of a file (in binary mode)
	Returns a floating point entropy value between 0 and 1
	
	Keyword arguments:
	file -- The path of a file as a string
	"""
	f = open(file,"rb")
	bytes = f.read()
	f.close()
	return e.ent(bytes)
	
def listEnt(file, blocksize):
	"""Measure the entropy of a file in groups of bytes (blocks)
	Returns a list of floating point entropy values between 0 and 1
	
	Keyword arguments:
	file -- The path of a file as a string.
	blocksize -- integer number defining how large each block is.
	"""
	f = open(file,"rb")
	bytes = f.read()
	f.close()
	return e.listEnt(bytes, blocksize)


def bitEnt(file):
	"""
	Measure the entropy of a file (in binary mode)
	Returns a floating point entropy value between 0 and 8 (bits per byte)
	
	Keyword arguments:
	file -- The path of a file as a string
	"""
	f = open(file,"rb")
	bytes = f.read()
	f.close()
	return e.bitEnt(bytes)

def listBitEnt(file, blocksize):
	"""
	Measure the entropy of a file in groups of bytes (blocks)
	Returns a list of floating point entropy values between 0 and 8 (bits per byte)
	
	Keyword arguments:
	file -- The path of a file as a string.
	blocksize -- integer number defining how large each block is.
	"""
	f = open(file,"rb")
	bytes = f.read()
	f.close()
	return e.listBitEnt(bytes, blocksize)
	
def saveEntropyList(file, list):
	"""
	Writes a list of entropy values out to a file for use in spreadsheet programs
	No return value
	
	Keyword arguments:
	file -- The path of a file as a string.
	list -- The list of entropy values created by listEnt() or listBitEnt()
	"""
	f = open(file,"w+")
	for x in list:
		f.write(repr(x)+"\n")
	f.close()