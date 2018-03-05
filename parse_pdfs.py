from googlesearch import search # pip install google
import PyPDF2
import requests
import wget

google_search_query = 'site:www.edmonton.ca bike lanes'
# Limit to PDFs
google_search_query = 'filetype:pdf ' + google_search_query

limit = 1
count = 0
tempfile = "temp.pdf"
# for file in search(google_search_query):#, tld="co.in", num=10, stop=1, pause=2):
#     count += 1
#     if count > limit: break
#     print(file)
#     print("\n\n\n\n")
#
#     wget.download(file, tempfile)
#
#
#     break


pdf_file = open(tempfile, 'rb')
reader = PyPDF2.PdfFileReader(pdf_file)
text = ""
for page in range(1, reader.numPages + 1):
    page = reader.getPage(count)
    text += page.extractText()

print(text)
print(text == '')

# if text != "":
#    text = text
# #If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
# else:
#    text = textract.process(fileurl, method='tesseract', language='eng')
