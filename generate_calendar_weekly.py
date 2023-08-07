#! /usr/bin/env python3

import datetime
import sys
import calendar
import locale

import functions

# Must be set in order to take into account system locale, otherwise defaults to English!? (see https://stackoverflow.com/a/17903086)
locale.setlocale(locale.LC_ALL, '')

if len(sys.argv) == 2:
    year = int(sys.argv[1])
    year_to = year + 9
else:
    print("Usage: " + sys.argv[0] + " <year>", file=sys.stderr)
    sys.exit(1)

print("Generating weekly single-task calendar for year " + str(year), file=sys.stderr)

file_name_base = "calendar_" + str(year) + "_weekly"
file_name_html = file_name_base + ".html"
print("Writing file " + file_name_html, file=sys.stderr)
f = open(file_name_html, "w")

f.write("""<html>
<head><title>Weelky task for year """ + str(year) + """</title>
<style>

body {
  font-family: "sans-serif";
}

td.month-cell {
  border: 0px;
}

td.empty-cell, td.week-cell {
  height: 2em;
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
    f.write('<td class="month-cell" style="text-align: right;">' + calendar.month_abbr[month].encode('ascii', 'xmlcharrefreplace').decode('ascii') + '</td>')

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

f.close()

file_name_pdf = file_name_base + ".pdf"
functions.generate_pdf_file(file_name_html, file_name_pdf)
  
