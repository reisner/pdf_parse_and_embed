from googlesearch import search # pip install google
import requests
import wget

google_search_query = 'site:www.edmonton.ca bike lanes'
# Limit to PDFs
google_search_query = 'filetype:pdf ' + google_search_query

limit = 1
count = 0
tempfile = "temp.pdf"
for file in search(google_search_query):#, tld="co.in", num=10, stop=1, pause=2):
    count += 1
    if count > limit: break
    print(file)
    print("\n\n\n\n")

    wget.download(file, tempfile)


    break
