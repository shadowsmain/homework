student_marks = []
while True:
    mark = int(input('ввещдите оценку студента:\n')) < 0
    if mark:
        student_marks.append(mark)
    else:
        break

print('ввод завершен')
print(student_marks)

i = 0
avg_mark = 0
while i < len(student_marks):
    avg_mark += int(student_marks[i])
    i += 1
avg_mark /= len(student_marks)
print('средний балл', avg_mark)