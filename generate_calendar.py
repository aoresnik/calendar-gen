import datetime
import calendar
import dateutil.easter

f = open("calendar.html", "w")

year = 2020

f.write("""<html>
<head><title>Koledar """ + str(year) + """</title>
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

months = ['jan', 'feb', 'mar', 'apr', 'maj', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec']

easter_monday = dateutil.easter.easter(year) + datetime.timedelta(days=1)

# Slovenian
holidays = [
    # [day, month]
    [1, 1], [2, 1], [8, 2], [27, 4], [1, 5], [2, 5], [25, 6], [15, 8], [31, 10], [1, 11], [25, 12], [26, 12],
    # easter monday (varies every year)
    [easter_monday.day, easter_monday.month]
]

for month in range(1, 13):
    f.write("<tr>")

    shift, days_in_month = calendar.monthrange(year, month)

    f.write('<td class="month-cell" style="text-align: right; " colspan="' + str(shift+1) + '">' + months[month-1] + '</td>')

    # max 31 days + max 6 cells padding
    for day_cell in range(1, days_in_month+1):
            day = day_cell

            weekday = calendar.weekday(year, month, day)
            if [day, month] in holidays:
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
