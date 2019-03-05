# pdf_parse_and_embed

Convert PDFs to text, from a website, or a local directory.

## Usage

Get PDFs from web:

```
python3 parse_pdfs_from_web.py
```

Or, get PDFS from a local directory:

```
python3 parse_pdfs_local.py
```

Then process and train embeddings:

```
Rscript read_text_and_embed.R
```
