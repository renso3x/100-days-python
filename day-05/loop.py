# student_heights = input("Input a list of student heights ").split()

# total = 0
# len_students = len(student_heights)
# for n in student_heights:
#     total += int(n)

# print(f"Average height {total/student_heights}")

# Max function replication
# Find Highest Score - 78 65 89 86 91 64 89 100
scores = input("Input a list of student scores ").split() 

max_score = scores[0]
for score in scores:
    if int(score) > int(max_score):
        max_score = score

print(f"Max score is {max_score}")