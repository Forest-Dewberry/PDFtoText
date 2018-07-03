myS = 'Pellet Weight (grams/100)                 1.00 - 1.70                           '
aList = []
for file in myL:
     with open(file,"rb") as f:
             pdf = pdftotext.PDF(f)
     myText = pdf[0][pdf[0].find(myS)+len(myS):pdf[0].find(myS)+len(myS)+4]
     aList.append(myText)
     print myText