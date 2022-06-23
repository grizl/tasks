n = int(input('Write number of students: '))
data = {}

# data = {'John': ['math', 'physics', 'astronomy'], 'Jane': ['physics', 'astronomy', 'chemistry'], 'Jonathan' : ['math', 'programming', 'physics']}

for i in range(1, n+1):
    name = input(f'Name of {i} student: ')
    if name not in data:
        subs = input(f'Subjects of {i} student: ').split()
        data.update({name : subs})
    else:
        print(f'Name {name} is already in the list.')
        print(f'Please, try to change the name')
        name = input(f'Enter altered name of {i} student: ')
        subs = input(f'Subjects of {i} student: ').split()
        data.update({name : subs})

def show_all():
    names = sorted(data, reverse=True)
    for i in names:
        print(f'{i} : {data[i]}')

show_all()

def student_for_sub(student):
    if student in data:
        print(data[student])
    else:
        print('There are no students with this name')

s = list(data.keys())
student_for_sub(s[0])
student_for_sub(s[1])

def sub_for_students(sub):
    students = []
    for key, value in data.items():
        if sub in value:
            students.append(key)
    if len(students):
        print(students)
    else:
        print('There are no matching students')

sub_for_students('math')
sub_for_students('astronomy')
sub_for_students('biology')