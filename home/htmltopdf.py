import pdfkit as pdf
from django.template.loader import get_template
pdf.from_file('no adhd.html','file.pdf')