import matplotlib.pyplot as plt
students=["san","rags","roh","nith","niv","pos","ragh"]
scores=[98,98,97,94,98,97,95]
plt.bar(students,scores,color='skyblue')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.title('Student Exam Scores')
plt.show()


