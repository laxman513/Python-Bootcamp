import numpy as np

marks = np.array([45, 78, 92, 35, 88, 60])

print("All Marks:", marks)

pass_marks = marks[marks >= 45]

print("Pass marks:", pass_marks)

high_marks = marks[marks >= 80]

print("High marks:", high_marks)