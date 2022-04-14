# You are going to write a program that calculates the average student height from a List of heights.

# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

# e.g.

# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

# There are a total of 7 heights in student_heights

# 1146 ÷ 7 = 163.71428571428572

# Average height rounded to the nearest whole number = 164



student_heights = input("Input a list of students heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])



total_height = 0
for add in student_heights:
    total_height += add
print(total_height)

total_student = 0

for count in student_heights:
    total_student += 1
print(total_student)

average = round(total_height/total_student)
print(average)
