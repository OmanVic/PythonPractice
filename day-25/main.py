# with open("weather-data.csv") as file:
#     content = file.read()
# data = content.splitlines()
# # print(data)
#
# import csv
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperature.append(temp)
#     print(temperature)
import pandas
import pandas as pd
data = pd.read_csv("weather-data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# #print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)

# Calculating average temperature

# ave_temp = sum(temp_list)/len(temp_list)
# print(ave_temp)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)
#
# # print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# # print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp)
#
#
# # Create a dateframe from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

central_park = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = central_park.Primary_Fur_Color
num_black = (fur_color == "Black").sum()
num_cinnamon = (fur_color == "Cinnamon").sum()
num_gray = (fur_color == "Gray").sum()
print(num_gray)

file_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [num_gray, num_cinnamon, num_black],
}
file = pandas.DataFrame(file_dict)
file.to_csv("squirrel_count.csv")