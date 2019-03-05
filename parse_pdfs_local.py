import os
import pdf_utils

pdf_dir = '/Users/eisner/data/pdfs_coe/'

outputdir = "output/"
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

file_limit = 20000
min_chars_in_file = 50
count = 0
count_had_data = 0

print("Parsing files ...", end = '')
for filename in os.listdir(pdf_dir):
    count += 1

    if (count % 500 == 0):
        print(str(count) + "...", end = '')

    found_data = pdf_utils.process_file(pdf_dir + filename, outputdir + str(count) + ".txt", min_chars_in_file)

    if found_data: count_had_data += 1

    if count >= file_limit: break

print("Done.\n\n")
print("Found data in " + str(count_had_data) + " out of " + str(count) + " PDF files.")