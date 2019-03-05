import textract
import os

pdf_dir = '/Users/eisner/data/pdfs_coe/'

outputdir = "output/"
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

file_limit = 10
min_chars_in_file = 50
count = 0
count_had_data = 0

print("Parsing files ...", end = '')
for filename in os.listdir(pdf_dir):
    count += 1

    if (count % 3 == 0):
        print(str(count) + "...", end = '')

    text = textract.process(pdf_dir + filename) #method='tesseract', language='eng')
    text = text.strip()

    if (len(text) >= min_chars_in_file):
        count_had_data += 1
        f = open(outputdir + str(count) + ".txt","w+")
        f.write(text.decode("utf-8"))
        f.close()

    if count >= file_limit: break

print("Done.\n\n")
print("Found data in " + str(count_had_data) + " out of " + str(count) + " PDF files.")
