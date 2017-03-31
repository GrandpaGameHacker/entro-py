"""
This module contains functions that wrap ent.py for use with files
"""
import ent as e

def ent(file):
	f = open(file,"rb")
	bytes = f.read()
	f.close()
	return e.ent(bytes)
	
def listent(file, blocksize):
	f = open(file,"rb")
	bytes = f.read()
	f.close()
	return e.listent(bytes, blocksize)


def bitent(file):
	f = open(file,"rb")
	bytes = f.read()
	f.close()
	return e.bitent(bytes)

def listbitent(file, blocksize):
	f = open(file,"rb")
	bytes = f.read()
	f.close()
	return e.listbitent(bytes, blocksize)
