#!/usr/bin/python3

import fileinput
import os
import sys

# Generated valid .cpp and .h files from stdin

# Run Command: python3 makeClasses.py
# Input: className1 [ENTER] className2 [ENTER] etc..

def makeCPP(className):
	with open(className.lower() + ".cpp", 'w') as classFile:
		classFile.write("#include <iostream>\n#include <string>\n#include <sstream>\n#include <stdio.h>\n#include <stdlib.h>\n#include <ctype.h>\n#include <string.h>\n\n")
		classFile.write("#include \"" + className.lower() + ".h\"\n\n")
		classFile.write("using namespace std;\n\n")


def makeH(className):
	with open(className.lower() + ".h", 'w') as classFile:
		classFile.write("#ifndef " + className.upper() + "_H\n")
		classFile.write("#define " + className.upper() + "_H\n\n")
		classFile.write("#include <string>\n\n")
		classFile.write("class " + className + "\n" + "{\n")
		classFile.write("private:\n\t\n\n")
		classFile.write("public:\n\t\n\n")
		classFile.write("};\n\n")
		classFile.write("#endif //" + className.upper() + "_H\n")


for argv in sys.stdin:
	file = argv.strip('\n')
	if os.path.isfile(file):
		print("File has already been created. Remove to re-write")
	else:
		makeCPP(file)
		makeH(file)