# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code
# def make_pie(index):
#     try:
#         fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         fruit = fruits[index]
#         print(fruit + " pie")
#
# make_pie(4)
# make_pie(2)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        pass
print(total_likes)

#repl.it/@appbrewery/day-30-2-solution