#! /usr/bin/env python3

import datetime
import calendar
import sys
import subprocess
import calendar
import locale

import holidays

# Must be set in order to take into account system locale, otherwise defaults to English!? (see https://stackoverflow.com/a/17903086)
locale.setlocale(locale.LC_ALL, '')

import dateutil.easter

if len(sys.argv) == 2:
    year = int(sys.argv[1])
    year_to = year + 9
else:
    print("Usage: " + sys.argv[0] + " <year>", file=sys.stderr)
    sys.exit(1)

file_name_base = "calendar_" + str(year) + "_daily"
file_name_html = file_name_base + ".html"
print("Writing file " + file_name_html, file=sys.stderr)
f = open(file_name_html, "w")

f.write("""<html>
<head><title>Daily tasks for year """ + str(year) + """</title>
<style>

body {
  font-family: "sans-serif";
}

td.month-cell {
  width: 3.8%;
  border: 0px;
}

td.empty-cell, td.day-cell, td.saturday-cell, td.sunday-cell, td.holiday-cell {
  width: 2.6%;
  height: 2em;
}

td.empty-cell {
  border: 0px;
}

td.day-cell, td.saturday-cell, td.sunday-cell, td.holiday-cell {
  border: 1px solid black;
  text-align: left;
  vertical-align: top;
}

td.saturday-cell, td.sunday-cell, td.holiday-cell {
   background-color: #c0c0c0;
}

div.day-digit, div.saturday-digit, div.sunday-digit, div.holiday-digit {
  font-size: 0.5em;
}

div.holiday-digit {
  color: red;
}

div.sunday-digit {
  color: red;
  font-weight: bold;
}

</style>
</head>
""")
f.write("<body>")

f.write('<p style="text-align: center; font-size: 1.5em">'+ str(year) + '</p>')

f.write('<p><table style="border-spacing: 0; border-collapse: collapse; width: 100%;">')

easter_monday = dateutil.easter.easter(year) + datetime.timedelta(days=1)

[locale_lang, locale_encoding] = locale.getlocale()
if locale_lang != None and len(locale_lang.split("_")) > 1:
  locale_country = locale_lang.split("_")[1]
  holidays = holidays.utils.country_holidays(country=locale_country)
  if holidays == None:
      print("No holidays for country " + locale_country + " found - not showing holidays", file=sys.stderr)
else:      
  print("Locale does not represent a coutnry, not showing holidays", file=sys.stderr)

for month in range(1, 13):
    f.write("<tr>")

    shift, days_in_month = calendar.monthrange(year, month)

    f.write('<td class="month-cell" style="text-align: right; " colspan="' + str(shift+1) + '">' + calendar.month_abbr[month] + '</td>')

    # max 31 days + max 6 cells padding
    for day_cell in range(1, days_in_month+1):
            day = day_cell

            weekday = calendar.weekday(year, month, day)
            if holidays != None and datetime.date(year, month, day) in holidays:
                daytype = 'holiday'
            else:
                if weekday == 5:
                    daytype = 'saturday'
                elif weekday == 6:
                    daytype = 'sunday'
                else:
                    daytype = 'day'

            f.write('<td class="'+daytype+'-cell">')
            f.write('<div class="'+daytype+'-digit">' + str(day) + '</span>')
            f.write("</td>")

    f.write("</tr>")

f.write("</table></p>")

f.write("</body>")
f.write("</html>")

f.close()

file_name_pdf = file_name_base + ".pdf"
print("Generating PDF " + file_name_pdf + " with wkhtmltopdf", file=sys.stderr) 
try:
  subprocess.run(["wkhtmltopdf", "-O", "Landscape", file_name_html, file_name_pdf])
except FileNotFoundError:
  print("ERROR: Could not find wkhtmltopdf - not generating PDF output. Plese install it to generate PDF output.", file=sys.stderr)
  sys.exit(1)