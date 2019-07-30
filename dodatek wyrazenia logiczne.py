presence = 0.85
note = 3    .5
IsExamPassed = False
SemesterIsComplete = (presence >= 0.8 and note >= 3.0) or IsExamPassed
print("Presence =", presence)
print("Grade note:", note)
print("Exam passed:", IsExamPassed)
print("Semester is completed:", SemesterIsComplete)