#Create a 2d array to store the marks of 3 subjects of 5 students. and perform:
# 1. Find the max marks
# 2. Find the min marks
# 3. Find the avg marks
# 4. find the students id (0 to 5) who score max marks in sub(1)
# 5. find max marks subject wise
# 6. Find avg marks student wise

# Create a 2D array to store marks of 3 subjects of 5 students

marks = [[88,78,94],
         [68,47,73],
         [96,87,93],
         [72,43,78],
         [89,92,83]
         ]

# 1. Find the max marks
print("Maximum marks:", max(max(row) for row in marks))

# 2. Find the min marks
print("Minimum marks:", min(min(row) for row in marks))

# 3. Find the average marks
total = sum(sum(row) for row in marks)
avg = total / (5 * 3)
print("Average marks:", avg)

# 4. Find student IDs who score max marks in subject 1
max_sub1 = max(row[0] for row in marks)
students = [i for i in range(5) if marks[i][0] == max_sub1]
print("Student IDs with max marks in subject 1:", students)

# 5. Find max marks subject wise
max_subject = [max(marks[i][j] for i in range(5)) for j in range(3)]
print("Maximum marks subject wise:", max_subject)

# 6. Find average marks student wise
avg_student = [sum(row) / 3 for row in marks]
print("Average marks student wise:", avg_student)