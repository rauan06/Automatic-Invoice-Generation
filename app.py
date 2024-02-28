import os

os.add_dll_directory(r"C:\Users\ommir\OneDrive\Documents\GitHub\Automatic-Invoice-Generation")

from weasyprint import HTML
import flask

html = HTML('invoice.html')
html.write_pdf('invoice.pdf')