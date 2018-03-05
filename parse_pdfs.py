from googlesearch import search # pip install google
import textract
import requests
import wget

google_search_query = 'site:www.edmonton.ca bike lanes'
# Limit to PDFs
google_search_query = 'filetype:pdf ' + google_search_query

limit = 1
count = 0
tempfile = "temp.pdf"
for file_url in search(google_search_query):#, tld="co.in", num=10, stop=1, pause=2):
    count += 1
    if count > limit: break
    print(file_url)
    print("\n\n")

    wget.download(file_url, tempfile)

    text = textract.process(tempfile) #method='tesseract', language='eng')
    print(text)

    break
