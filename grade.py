student_people = input('Enter how many students: ')
student_people = int(student_people)
y = int(student_people)
x = []

while student_people > 0:
    student_grade = input('Enter student grade: ')
    student_grade = int(student_grade)
    x.append(student_grade)
    student_people -= 1

def student_data(num):

    fail = 0
    if num == 1:
        return sum(x)
    elif num == 2:
        return max(x)
    else:
        for i in x:
            if i < 60:
                fail += 1
        return fail

print('student grade average: {0}\nstudent grade max: {1}\n'
      'student grade fail: {2}'.format(student_data(1), student_data(2), student_data(3)))