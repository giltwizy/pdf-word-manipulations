import PyPDF2

#Change 'original.pdf' to your respective pdf filename and make sure the pdf file is in the same directory
#you can use path or filename directly,both works fine

with open("original.pdf", "rb") as pdf_in:	
	pdf_reader = PyPDF2.PdfFileReader(pdf_in)
	pdf_writer = PyPDF2.PdfFileWriter()

	#getting the number of pages from the pdf so as to perform rotation on all pages
	for pagenum in range(pdf_reader.numPages):
		page = pdf_reader.getPage(pagenum)
		#Change 90 to your desired rotation angle
		page.rotateClockwise(90)	
		pdf_writer.addPage(page)

	with open("rotated.pdf", 'wb') as pdf_out:	
		pdf_writer.write(pdf_out)

