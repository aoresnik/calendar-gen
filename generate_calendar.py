import datetime
import calendar

f = open("calendar.html", "w")

year = 2020

f.write("""<html>
<head><title>Koledar """ + str(year) + """</title>
<style>

body {
  font-family: "sans-serif";
}

td.month-cell {
  width: 7.5%;
  border: 0px;
}

td.empty-cell, td.day-cell, td.saturday-cell, td.sunday-cell, td.holiday-cell {
  width: 2.5%;
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

div.sunday-digit {
  color: red;
  font-weight: bold;
}

</style>
</head>
""")
f.write("<body>")

f.write('<p style="text-align: center; ">'+ str(year) + '</p>')

f.write('<p><table style="border-spacing: 0; border-collapse: collapse; width: 100%;">')

months = ['jan', 'feb', 'mar', 'apr', 'maj', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'dec']

for month in range(1, 12):
    f.write("<tr>")
    f.write('<td class="month-cell" style="text-align: right; ">' + months[month-1] + '</td>')

    shift, days_in_month = calendar.monthrange(year, month)

    # max 31 days + max 6 cells padding
    for day_cell in range(1, 37):
        if day_cell > shift and (day_cell - shift <= days_in_month):
            day = day_cell - shift

            weekday = calendar.weekday(year, month, day)
            if weekday == 5:
                daytype = 'saturday'
            elif weekday == 6:
                daytype = 'sunday'
            else:
                daytype = 'day'

            f.write('<td class="'+daytype+'-cell">')
            f.write('<div class="'+daytype+'-digit">' + str(day) + '</span>')
        else:
            f.write('<td class="empty-cell">')
        f.write("</td>")

    f.write("</tr>")

f.write("</table></p>")

f.write("</body>")
f.write("</html>")
