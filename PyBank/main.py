import os
import csv
import pathlib
import statistics

budget_path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'Resources','budget_data.csv')
with open(budget_path) as path_copy:
    reader = csv.reader(path_copy, delimiter = ",")
    header = next(path_copy)

    months = 0
    total_profit = 0

    profit_list = []
    months_list = []

    for row in reader:
        months += 1
        total_profit += int(row[1])

        profit_list.append(int(row[1]))
        months_list.append(str(row[0]))


change_in_profit = []
largest_inc = 0
largest_dec = 0

largest_inc_month = ""
largest_dec_month = ""

x=0
while x < months:
    if x > 0:
        monthly_change = (profit_list[x] - profit_list[x-1])

        if monthly_change > largest_inc:
                largest_inc = monthly_change
                largest_inc_month = months_list[x]

        if monthly_change < largest_dec:
                largest_dec = monthly_change
                largest_dec_month = months_list[x]

        change_in_profit.append(monthly_change)

    x += 1

avg_change = round(statistics.mean(change_in_profit),2)

output_path = os.path.join(pathlib.Path(__file__).parent.resolve(), 'analysis','analysis.txt')

output_line_1 = "Total Months:" + str(months)
output_line_2 = "Total: $" + str(total_profit)
output_line_3 = "Average Change" + str(avg_change)
output_line_4 = "Greatest Increase in Profits: " + str(largest_inc_month) + " ($" + str(largest_inc) + ")"
output_line_5 = "Greates Decrease in Profits: " + str(largest_dec_month) + " ($" + str(largest_dec) + ")"

total_output = ["Financial Analysis", "---------------------------- ", output_line_1, output_line_2, output_line_3, output_line_4, output_line_5]

with open(output_path, 'w') as output_copy:

    for line in total_output:
        output_copy.write(line)
        output_copy.write("\n")

for line in total_output:
    print(line)
