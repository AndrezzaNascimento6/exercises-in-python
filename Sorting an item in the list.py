import random
student1 = input('First student name : ')
student2 = input('Second student name : ')
student3 = input('Third student name : ')
student4 = input('Name of fourth student: ')
answer = student1, student2, student3, student4
answer1 = random.choice(answer)
print('The name of the chosen student is: {}'.format(answer1))