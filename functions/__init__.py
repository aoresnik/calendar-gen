
import subprocess
import sys

def generate_pdf_file(file_name_html, file_name_pdf):
  print("Generating PDF " + file_name_pdf + " with wkhtmltopdf", file=sys.stderr) 
  try:
    subprocess.run(["wkhtmltopdf", "-O", "Landscape", file_name_html, file_name_pdf])
  except FileNotFoundError:
    print("ERROR: Could not find wkhtmltopdf - not generating PDF output. Plese install it to generate PDF output.", file=sys.stderr)
