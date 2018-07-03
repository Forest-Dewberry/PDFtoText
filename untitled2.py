import pdftotext

import os 
mypath = os.path.dirname(os.path.realpath(__file__))
mypath = mypath
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

myList = []
for pdfFile in onlyfiles:

	with open((pdfFile),"rb") as f:
		pdf = pdftotext.PDF(f)

	for line in pdf[0].split("\n"):
		if "Pellet Weight" in line:
			backwardsLine = line[::-1]
			testWt = line[(len(line)-backwardsLine.find(" ")):]
			myList.append(testWt)
