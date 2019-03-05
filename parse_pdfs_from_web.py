from googlesearch import search # pip install google
import textract
import os
import requests
import wget

google_search_query = 'site:www.somewebsiteurlhere.ca bike lanes'
# Limit to PDFs
google_search_query = 'filetype:pdf ' + google_search_query

outputdir = "output/"
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

limit = 50
count = 0
min_chars_in_file = 50
tempfile = "temp.pdf"
if os.path.exists(tempfile):
    os.remove(tempfile)

for file_url in search(google_search_query):#, tld="co.in", num=10, stop=1, pause=2):
    count += 1
    if count > limit: break

    wget.download(file_url, tempfile)

    found_data = pdf_utils.process_file(tempfile, outputdir + str(count) + ".txt", min_chars_in_file)

    os.remove(tempfile)
