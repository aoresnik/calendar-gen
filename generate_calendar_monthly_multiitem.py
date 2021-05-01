import datetime
import calendar
import sys

import dateutil.easter

if len(sys.argv) == 2:
    year = int(sys.argv[1])
    print("Generating calendar for year " + str(year) + " (specified on command line)")
else:
    year = datetime.datetime.now().year + 1
    print("Generating calendar for year " + str(year) + " (next year)")

file_name = "calendar_" + str(year) + "_monthly_multiitem.html"
print("Writing file " + file_name)
f = open(file_name, "w")

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

months = ['jan', 'feb', 'mar', 'apr', 'maj', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec']

def format_day(d):
    return "{}.{}".format(d.day, d.month) if d.year==year else "{}.{}.{}".format(d.day, d.month, d.year)

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

