# Open the weather_data.csv file
#with open("100 day of code\Day 25 working with csv data and pandas\weather_data.csv") as data_file:
    # Read all the lines from the file
#    data = data_file.readlines()
    # Print the data
#    print(data)


# import csv
# with open("100 day of code\Day 25 working with csv data and pandas\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("100 day of code\Day 25 working with csv data and pandas\weather_data.csv")
# print(data["temp"])

# import pandas
# data = pandas.read_csv("100 day of code\Day 25 working with csv data and pandas\weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
import pandas
data = pandas.read_csv("100 day of code\Day 25 working with csv data and pandas\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231211.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "GRAY"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "CINNAMON"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "BLACK"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
pandas.DataFrame(data_dict).to_csv("100 day of code\Day 25 working with csv data and pandas\squirrel_count.csv")
#data["Primary Fur Color"] = data["Primary Fur Color"].str.upper()