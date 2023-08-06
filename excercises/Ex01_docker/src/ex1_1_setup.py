from datetime import datetime
from prettytable import PrettyTable
import csv
import sys

now = datetime.now()
print(f"Countdown from : {now.strftime('%Y-%m-%d %H:%M:%S')}")

rows = []

if len(sys.argv) < 2:
    print("Feed me more arguments")
    exit

datafilename = sys.argv[1]
logfilename = sys.argv[2]

with open(datafilename) as file:
    data = csv.reader(file)

    for row in data:
        label = row[0]
        event_date = row[1]

        try:
            end_date = datetime.strptime(event_date, "%Y-%m-%d %H:%M")
        except ValueError:
            end_date = datetime.strptime(event_date, "%Y-%m-%d")

        year_diff = max(end_date.year - now.year, 0)
        month_diff = max(end_date.month - now.month, 0)
        day_diff = max(end_date.day - now.day, 0)
        hour_diff = abs(end_date.hour - now.hour)
        minute_diff = abs(end_date.minute - now.minute)
        second_diff = abs(end_date.second - now.second)

        out = [label, year_diff, month_diff, day_diff, hour_diff, minute_diff, second_diff]
        rows.append(out)

x = PrettyTable()
x.field_names = ["Event", "Y", "M", "D", "H", "Min", "S"]

x.add_rows(rows)
print(x)

if logfilename:
    with open(logfilename, "a") as file:
        file.write(x.get_string())