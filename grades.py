def gradingStudents(grades):
    # Write your code here
    for i in range(0,len(grades)) :
        if grades[i]>37 and (5-(grades[i]%5))<=3:
            grades[i] +=(5-(grades[i]%5))
    return grades

grades = [73,67,38,33]
res = gradingStudents(grades)
print(res)