# with normal file method
# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#
from traceback import print_tb

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
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(type(data))
# will print pandas data frame
# print(type(data["temp"]))
# now it will print a series
# data_dict = data.to_dict()
# will transform it into a dictionary
# print(data_dict)

# temp_list = data["temp"].to_list()

# print(temp_list)
# becomes a list as well
# average temp
# average_temp = int(sum(temp_list) / len(temp_list))
# print(f"Average temperature is {average_temp}")
# average temp using pandas, works the same way with 1 line
# print(data["temp"].mean())
# print max temperature
# print(data["temp"].max())

# get data in columns
# same result both ways
# print(data["condition"])
# print(data.condition)

# get data in rows
# data[data["day"] == "Monday"]
# print(data[data.day == "Monday"])
# print row of data with the highest temperatur
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])
# monday temp as F
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)


# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# convert to csv, will create a new file in the current folder
# data.to_csv("new_data.csv")

