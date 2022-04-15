student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

for each in student_scores:
    if student_scores[each] >= 91:
        student_grades[each] = "Outstanding"
    elif student_scores[each] >= 81:
        student_grades[each] = "Exceeds Expectations"
    elif student_scores[each] >= 71:
        student_grades[each] = "Acceptable"
    else:
        student_grades[each] = "Fail"

print(student_grades)