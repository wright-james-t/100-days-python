# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
# # print(temp_list)
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# # print(data[data.day == "Monday"])
# #
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
#
# # print(monday.condition)
#
# ftemps = data.assign(Celsius = lambda x: (9/5)*x['temp']+32)
#
# # print(ftemps)
#
# monday_temp_c = monday.temp.iloc[0]
# # monday_temp_c = int(monday.temp)
# monday_temp_f = monday_temp_c * 9/5 + 32
#
# print(monday_temp_f)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

count = len(data[data["condition"] == "Sunny"])

print(count)