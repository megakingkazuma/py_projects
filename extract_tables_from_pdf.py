import camelot

tables = camelot.read_pdf('PDF/foo.pdf', pages='1')
print(tables)

# doesnt work due to a requirement error 