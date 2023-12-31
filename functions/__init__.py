
import subprocess
import sys

def generate_pdf_file(file_name_html, file_name_pdf, orientation="Landscape"):
  print("Generating PDF " + file_name_pdf + " with wkhtmltopdf", file=sys.stderr) 
  try:
    subprocess.run(["wkhtmltopdf", 
                    "-O", orientation, 
                    "--margin-top", "2cm",
                    "--margin-left", "2cm",
                    "--margin-right", "2cm",
                    "--margin-bottom", "2cm",
                    file_name_html, 
                    file_name_pdf])
  except FileNotFoundError:
    print("ERROR: Could not find wkhtmltopdf - not generating PDF output. Plese install it to generate PDF output.", file=sys.stderr)
