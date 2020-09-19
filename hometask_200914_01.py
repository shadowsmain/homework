student_marks = []
while True:
       mark = input('введите оценку студента:\n')
       if mark:                           # '' == False, () == False, [] == False
           student_marks.append(int(mark))
           if int(mark) > 5:
                print('incorrect number')
       else:
         break

print('ввод завершен')
print(student_marks)