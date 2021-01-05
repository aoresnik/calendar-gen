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

file_name = "calendar_" + str(year) + "_weekly.html"
print("Writing file " + file_name)
f = open(file_name, "w")

f.write("""<html>
<head><title>Koledar """ + str(year) + """</title>
<style>

body {
  font-family: "sans-serif";
}

td.month-cell {
  border: 0px;
}

td.empty-cell, td.week-cell {
  height: 3em;
}

td.empty-cell {
  border: 0px;
}

td.week-cell {
  border: 1px solid black;
  vertical-align: top;
  width: 19%;
}

span.week-text, span.date-end-text, span.date-text {
  font-size: 0.7em;
}

span.date-end-text { color: red; }


</style>
</head>
""")
f.write("<body>")

f.write('<p style="text-align: center; font-size: 1.5em">'+ str(year) + '</p>')

f.write('<p><table style="border-spacing: 0; border-collapse: collapse; width: 100%;">')

months = ['jan', 'feb', 'mar', 'apr', 'maj', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec']

day = datetime.date(year, 1, 1)
day_iso = day.isocalendar()

day = day + datetime.timedelta(days=-(day_iso[2]-1))
day_iso = day.isocalendar()

if day_iso[0] < year:
    # If first day is in previous ISO week year, move to first date that is in current is year, i.e. the first monday
    day = day + datetime.timedelta(7-day_iso[2]+1)
    day_iso = day.isocalendar()

def format_day(d):
    return "{}.{}".format(d.day, d.month) if d.year==year else "{}.{}.{}".format(d.day, d.month, d.year)

while day_iso[0] <= year:
    f.write("<tr>")

    # The day falls into the month 
    month = (day + datetime.timedelta(days=4)).month
    f.write('<td class="month-cell" style="text-align: right;">' + months[month-1] + '</td>')

    while (day + datetime.timedelta(days=4)).month == month:
        end_day = day + datetime.timedelta(days=6)
        f.write('<td class="week-cell">')
        f.write('<span class="date-text">' + format_day(day) + '</span> - <span class="date-end-text">' + format_day(end_day) + '</span><br/>')
        f.write('<span class="week-text"> W:' + str(day_iso[1]) + '</span>')
        f.write("</td>")
        day = day + datetime.timedelta(days=7)
        day_iso = day.isocalendar()

    f.write("</tr>")

f.write("</table></p>")

f.write("</body>")
f.write("</html>")
