#! /usr/bin/env python3

import sys

if len(sys.argv) == 2:
    year = int(sys.argv[1])
    year_to = year + 9
else:
    print("Usage: " + sys.argv[0] + " <year>", file=sys.stderr)
    sys.exit(1)

print("Generating calendar for years " + str(year) + " to " + str(year_to), file=sys.stderr)

file_name = "calendar_" + str(year) + "_multiyear.html"
print("Writing file " + file_name, file=sys.stderr)
f = open(file_name, "w")

f.write("""<html>
<head><title>Yearly tasks """ + str(year) + """-""" + str(year_to) + """</title>
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

f.write('<p><table style="border-spacing: 0; border-collapse: collapse; width: 100%;">')

years = range(year, year + 10)

def format_day(d):
    return "{}.{}".format(d.day, d.month) if d.year==year else "{}.{}.{}".format(d.day, d.month, d.year)

# Chosen to fit an A4 page
N_ENTRIES = 31

f.write("<tr>")
f.write('<td style="text-align: right;"></td>')
for y in years:
    f.write('<td class="checkmark-cell" style="text-align: center;">' + str(y) + '</td>')
f.write("</tr>")

for i in range(N_ENTRIES):
    f.write("<tr>")
    f.write('<td class="task-title-cell" style="text-align: right;">&nbsp;</td>')
    for y in years:
        f.write('<td class="checkmark-cell"></td>')
    f.write("</tr>")

f.write("</table></p>")

f.write("</body>")
f.write("</html>")

f.close()

