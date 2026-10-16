
# Python Date and Time

from datetime import datetime, date, timedelta

# 1. Get Current Date and Time
current = datetime.now()
print("Current Date and Time:", current)


# 2. Get Current Date
today = date.today()
print("Today's Date:", today)


# 3. Create a Specific Date
my_date = date(2026, 10, 16)
print("Specific Date:", my_date)


# 4. Extract Year, Month and Day
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# 5. Format Date and Time
formatted = current.strftime("%d-%m-%Y")
print("Formatted Date:", formatted)


# 6. Add 7 Days to a Date
next_week = today + timedelta(days=7)
print("After 7 Days:", next_week)


# 7. Calculate Difference Between Dates
date1 = date(2026, 10, 16)
date2 = date(2026, 10, 30)

difference = date2 - date1
print("Difference:", difference.days, "days")


# 8. Convert String into Date
date_string = "16-10-2026"
converted_date = datetime.strptime(
    date_string, "%d-%m-%Y"
).date()

print("Converted Date:", converted_date)
