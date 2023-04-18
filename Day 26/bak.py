import pandas
import random

# new_list = [new_item for item in list]

# numbers = [1,2,3]
# new_list = []
# for n in list:
#     add_1 = n + 1
#
# new_list.append(add_1)
#
# new_list = [n + 1 for n in numbers]

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared_numbers = [num * num for num in numbers]
#
# print(squared_numbers)

# result = [num for num in numbers if num % 2 == 0]
#
# print(result)

# with open("file1.txt", mode="r") as file:
#     file_1 = file.read()
#     file_1_list = file_1.split("\n")
#
# with open("file2.txt", mode="r") as file:
#     file_2 = file.read()
#     file_2_list = file_2.split("\n")
#
# print(file_1_list)
# print(file_2_list)
#
# result = [int(num) for num in file_1_list if num in file_2_list]
# print(result)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# student_scores = {name:random.randint(1,100) for name in names}
#
# passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
#
# print(passed_students)
#
# failed_students = {student:score for (student, score) in student_scores.items() if score < 60}
#
# print(failed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# result = {word:len(word) for word in sentence.split(" ")}
#
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
#
# weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
#
# print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)

print(student_df)