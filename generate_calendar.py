import datetime
import calendar

f = open("calendar.html", "w")

year = 2020

f.write("<html><head><title>Koledar " + str(year) + "</title></head>");
f.write("<body>")

f.write('<h>'+ str(year) + '</h>')

f.write('<table style="border-spacing: 0; border-collapse: collapse; width="100%;">')

for month in range(1, 12):
    f.write("<tr>")

    shift, days_in_month = calendar.monthrange(year, month)

    # max 31 days + max 6 cells padding
    for day_cell in range(1, 37):
        if day_cell > shift and (day_cell - shift <= days_in_month):
            f.write('<td style="width: 2.70%; border: 1px solid black;">')
            f.write(str(day_cell - shift))
        else:
            f.write('<td style="width: 2.70%; border: 0px;">')
        f.write("</td>")

    f.write("</tr>")
 
f.write("</table>")

f.write("</body>")
f.write("</html>")

