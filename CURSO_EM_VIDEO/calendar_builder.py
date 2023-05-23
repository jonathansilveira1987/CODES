import calendar

text_cal = calendar.TextCalendar(firstweekday=0)

year = int(input('Ano: '))
width = 4
print(text_cal.formatyear(year, width))