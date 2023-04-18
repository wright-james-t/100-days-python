import pandas


# print(data[data.day == "Monday"])

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

data = pandas.read_csv("squirrel.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

squirrel_dict = {
    "color": ["gray", "black", "red"],
    "count": [gray_squirrels, black_squirrels, red_squirrels]
}

count_data = pandas.DataFrame(squirrel_dict)
count_data.to_csv("squirrel_count.csv")