for file in myL:
     with open(file,"rb") as f:
             pdf = pdftotext.PDF(f)
     print pdf[0][pdf[0].find('Date:      ')+len('Date:      '):pdf[0].find('Date:      ')+len('Date:      ')+7]