#! /usr/bin/env python3

import datetime
import calendar
import sys
import calendar
import locale

import holidays

import functions

# Must be set in order to take into account system locale, otherwise defaults to English!? (see https://stackoverflow.com/a/17903086)
locale.setlocale(locale.LC_ALL, '')

import dateutil.easter

N_TASK_CELLS = 10

if len(sys.argv) == 2:
    year = int(sys.argv[1])
    year_to = year + 9
else:
    print("Usage: " + sys.argv[0] + " <year>", file=sys.stderr)
    sys.exit(1)

file_name_base = "calendar_" + str(year) + "_daily_by_month_multiitem"
file_name_html = file_name_base + ".html"
print("Writing file " + file_name_html, file=sys.stderr)
f = open(file_name_html, "w")

f.write("""<html>
<head><title>Daily tasks for year """ + str(year) + """ - by month</title>
<style>

body {
  font-family: "sans-serif";
}

td.month-cell {
  border: 0px;
}

td.empty-cell, td.day-cell, td.saturday-cell, td.sunday-cell, td.holiday-cell {
  height: 1.5em;
}

td.empty-cell {
  border: 0px;
}

td.day-cell, td.saturday-cell, td.sunday-cell, td.holiday-cell, td.legend-cell, td-emtpy-cell {
  border: 1px solid black;
  text-align: center;
  vertical-align: top;
}

td.legend-cell {
  height: 4em;
}

td.checkmark-cell {
}

td.saturday-cell, td.sunday-cell, td.holiday-cell {
   background-color: #c0c0c0;
}

span.day-digit, div.saturday-digit, div.sunday-digit, div.holiday-digit {
  font-size: 1em;
}

span.holiday-digit {
  color: red;
}

span.sunday-digit {
  color: red;
  font-weight: bold;
}

tr {
  line-height: 1.5em;
}

/* based on https://stackoverflow.com/questions/1664049/can-i-force-a-page-break-in-html-printing */
@media print {
  .pagebreak { page-break-after: always; } /* page-break-after works, as well */
}

.title-line {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.title-line-element {
  display: flex;
  align-items: center;
}

</style>
</head>
""")
f.write("<body>")

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
    f.write('<div class="title-line" style="font-size: 1.5em; width: 100%;"><div class="title-line-element" >'+ calendar.month_name[month].encode('ascii', 'xmlcharrefreplace').decode('ascii') + '</div><div class="title-line-element">' + str(year) +'</div></div>')
    f.write('<p><table style="border-spacing: 0; border-collapse: collapse; width: 100%;">')

    f.write("<tr>")
    # I haven't spent enoug time to successfully get CSS to automatically assign minimum space to these columns and leave as much as possible to Notes column
    # So I set the width manually
    f.write('<td class="empty-cell" style="width: 2em;"></td>')
    f.write('<td class="empty-cell" style="width: 3em;"></td>')
    for i in range(N_TASK_CELLS):
        f.write('<td class="legend-cell" style="width: 2.5em;">&nbsp;</td>')
    f.write('<td class="empty-cell" style="text-align: center; vertical-align: bottom; width: max-content;">Notes</td>')
    f.write("</tr>")    

    shift, days_in_month = calendar.monthrange(year, month)

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

            f.write("<tr>")
            f.write('<td class="'+daytype+'-cell" style="width: min-content; text-align: right;">')
            f.write('<span class="'+daytype+'-digit" style="text-align: right;">' + str(day) + '&nbsp;</span>')
            f.write("</td>")
            f.write('<td class="'+daytype+'-cell" style="width: min-content;">')
            f.write('<span class="'+daytype+'-digit">' + calendar.day_abbr[weekday].encode('ascii', 'xmlcharrefreplace').decode('ascii') + '</span>')
            f.write("</td>")
            for i in range(N_TASK_CELLS):
                f.write('<td class="checkmark-cell '+daytype+'-cell">&nbsp;</td>')
            f.write('<td class="'+daytype+'-cell">')
            f.write('<div class="'+daytype+'-digit">&nbsp;</span>')
            f.write("</td>")
            f.write("</tr>")

    f.write("</table></p>")
    f.write('<div class="pagebreak"> </div>')

f.write("</body>")
f.write("</html>")

f.close()

file_name_pdf = file_name_base + ".pdf"
functions.generate_pdf_file(file_name_html, file_name_pdf, orientation="Portrait")
