library(coeNLP)
library(dplyr)

text_file_dir = 'output/'

all_text = c()
files = list.files(text_file_dir)
cat("Reading", length(files), "Files...")
for (file in files) {
  filepath = paste0(text_file_dir, file)
  text_data = readLines(con = filepath, warn = FALSE)

  short = nchar(text_data) < 5
  # require(stringi)
  # df[stri_length(df)>5]

  num_words = unlist(purrr::map(text_data, function(str) stringi::stri_stats_latex(str)[['Words']]))

  # Remove short lines:
  remove_ind = which(short | (num_words < 2))

  if (length(remove_ind) > 0) {
    text_data = text_data[-remove_ind]
  }

  if (length(text_data) > 0) {
    doc_text = paste(text_data, collapse = '. ')
    all_text = append(all_text, doc_text)
  }
}

cat("Done. Found", length(all_text), "Docs.\n")
browser()

cat("Training Embedding...")
model = coeNLP::trainEmbeddings(all_text, vectors = 100, lemmatize = TRUE)
cat("Done.\n")

# > model = coeNLP::readEmbeddings()
# > wordVectors::closest_to(model, "bike")
