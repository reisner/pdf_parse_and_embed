from googlesearch import search # pip install google
import textract
import os
import requests
import wget

google_search_query = 'site:www.edmonton.ca bike lanes'
# Limit to PDFs
google_search_query = 'filetype:pdf ' + google_search_query

outputdir = "output/"
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

limit = 1
count = 0
tempfile = "temp.pdf"
if os.path.exists(tempfile):
    os.remove(tempfile)

for file_url in search(google_search_query):#, tld="co.in", num=10, stop=1, pause=2):
    count += 1
    if count > limit: break

    wget.download(file_url, tempfile)

    text = textract.process(tempfile) #method='tesseract', language='eng')

    f = open(outputdir + str(count) + ".txt","w+")
    f.write(text.decode("utf-8"))
    f.close()

    os.remove(tempfile)

    break
