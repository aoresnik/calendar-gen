#! /usr/bin/env python3

import sys
import subprocess
import calendar
import locale

# Must be set in order to take into account system locale, otherwise defaults to English!? (see https://stackoverflow.com/a/17903086)
locale.setlocale(locale.LC_ALL, '')

if len(sys.argv) == 2:
    year = int(sys.argv[1])
    year_to = year + 9
else:
    print("Usage: " + sys.argv[0] + " <year>", file=sys.stderr)
    sys.exit(1)

print("Generating monthly multi-item calendar for year " + str(year), file=sys.stderr)

file_name_base = "calendar_" + str(year) + "_monthly_multiitem"
file_name_html = file_name_base + ".html"
print("Writing file " + file_name_html, file=sys.stderr)
f = open(file_name_html, "w")

f.write("""<html>
<head><title>Monthly tasks """ + str(year) + """</title>
<style>

body {
  font-family: "sans-serif";
}

td {
  border: 1px solid black;
  vertical-align: top;
}

td.task-title-cell {
  height: 2em; 
}

td.checkmark-cell {
  width: 2em;
}

</style>
</head>
""")
f.write("<body>")

f.write('<p style="text-align: center; font-size: 1.5em">'+ str(year) + '</p>')

f.write('<p><table style="border-spacing: 0; border-collapse: collapse; width: 100%;">')

months = [calendar.month_abbr[i] for i in range(1,13)]

def format_day(d):
    return "{}.{}".format(d.day, d.month) if d.year==year else "{}.{}.{}".format(d.day, d.month, d.year)

# Chosen to fit an A4 page
N_ENTRIES = 38

f.write("<tr>")
f.write('<td style="text-align: right;"></td>')
for month in months:
    f.write('<td class="checkmark-cell" style="text-align: center;">' + month[0] + '</td>')
f.write("</tr>")

for i in range(N_ENTRIES):
    f.write("<tr>")
    f.write('<td class="task-title-cell" style="text-align: right;">&nbsp;</td>')
    for month in months:
        f.write('<td class="checkmark-cell"></td>')
    f.write("</tr>")

f.write("</table></p>")

f.write("</body>")
f.write("</html>")

f.close()

file_name_pdf = file_name_base + ".pdf"
print("Generating PDF " + file_name_pdf + " with wkhtmltopdf", file=sys.stderr) 
try:
  subprocess.run(["wkhtmltopdf", file_name_html, file_name_pdf])
except FileNotFoundError:
  print("ERROR: Could not find wkhtmltopdf - not generating PDF output. Plese install it to generate PDF output.", file=sys.stderr)
  sys.exit(1)