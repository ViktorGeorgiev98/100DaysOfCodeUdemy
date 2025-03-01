# with normal file method
# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#

# with csv method
# import csv
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))


# Pandas library => same result, but easier and quicker with better formatting
import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])