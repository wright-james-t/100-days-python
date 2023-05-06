student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

#--example end--#

totalHeight = 0
heightCount = 0

for num in student_heights:
    totalHeight += num
    heightCount += 1
averageHeight = totalHeight / heightCount

print("The average height is", int(averageHeight))