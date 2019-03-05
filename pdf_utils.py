import textract

def process_file(filepath, outputfile, min_chars_in_file):
    text = textract.process(filepath) #method='tesseract', language='eng')
    text = text.strip()

    if (len(text) >= min_chars_in_file):
        f = open(outputfile, "w+")
        f.write(text.decode("utf-8"))
        f.close()
