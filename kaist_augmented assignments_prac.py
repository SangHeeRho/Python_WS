total=0
NumStudents=0
grades=[90, 76, 71, 87, 83, 90, 57, 79, 82, 94]
for i in grades:
    total+=i
    NumStudents+=1
average=total/NumStudents
print(f'Class average is {average}')
print(f'Average is {total/NumStudents:.2f}')
