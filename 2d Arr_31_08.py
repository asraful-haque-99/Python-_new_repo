#Add 10 marks for all students who score <50 in subject 1(2nd column).
#Find out no of students(count) who score > 80 in sub2 (3rd column).
#Find out the min marks of student 2.
#Find out the max marks of student 4.

marks = [[88,78,94],
         [68,47,73],
         [96,87,93],
         [72,43,78],
         [89,92,83]]

# 1. Add 10 marks for all students who score < 50 in subject 1 (2nd column)
for i in range(5):
    if marks[i][1] < 50:
        marks[i][1] += 10

print("Updated marks:", marks)

# 2. Find number of students who score > 80 in subject 2 (3rd column)
count = 0
for i in range(5):
    if marks[i][2] > 80:
        count += 1

print("Number of students:", count)

# 3. Find minimum marks of student 2
print("Minimum marks of student 2:", min(marks[2]))

# 4. Find maximum marks of student 4
print("Maximum marks of student 4:", max(marks[4]))