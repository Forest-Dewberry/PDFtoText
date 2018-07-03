import pdftotext

import os 
mypath = os.path.dirname(os.path.realpath(__file__))
print 'CURRENT DIRECTORY:', '\n', mypath, '\n'
mypath = mypath + raw_input('Please enter the folder where the PDF files are located, in the format: /folder/ \n')
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = [f for f in onlyfiles if '.pdf' in f]
print onlyfiles

