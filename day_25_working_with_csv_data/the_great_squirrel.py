import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_fur_color_count = len(data[data["Primary Fur Color"] == "Gray"])
# print(grey_fur_color_count)

red_fur_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(red_fur_color_count)

black_fur_color_count = len(data[data["Primary Fur Color"] == "Black"])
# print(black_fur_color_count)

new_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_fur_color_count, red_fur_color_count, black_fur_color_count]
}

df = pandas.DataFrame(new_data)
df.to_csv("squirrel_count.csv")
