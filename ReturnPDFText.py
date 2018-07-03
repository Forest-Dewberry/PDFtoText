if name=='__main__':
	outputFile = raw_input('Please enter the name of the output text file:\n')
	with open(outputFile, "w") as text_file:
    	text_file.write(ReturnPDFText())

def ReturnPDFText(path = 'none'):


	## FIND FILE INFORMATION:
	import os 
	mypath = os.path.dirname(os.path.realpath(__file__))
	print 'CURRENT DIRECTORY:', '\n', mypath, '\n'
	mypath = mypath + raw_input('Please enter the folder where the PDF files are located, relative to the current path, in the format: /folder/ \n')
	from os import listdir
	from os.path import isfile, join
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	onlyfiles = [f for f in onlyfiles if '.pdf' in f]
	print 'Returning these files in one text document:', '\n', onlyfiles, '\n'
	##

	## RETURN TEXT FILE:
	import pdftotext
	PDFlist = []
	for pdfFile in onlyfiles:

		pdfPages = []
		with open(pdfFile,"rb") as f:
			pdf = pdftotext.PDF(f)
		for page in pdf:
			pdfPages.append(page)
		PDFlist.append(	'\f'.join(pdfPages))

	return '\f\f'.join(PDFlist)




