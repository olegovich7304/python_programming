#coding:utf-8
groupmates = [
{
"name": u"Иван",
"group": "БСТ-2251",
"age": 23,
"marks": [4, 3, 5, 5, 4]
},
{
"name": u"Артем",
"group": "БСТ-2253",
"age": 22,
"marks": [3, 2, 3, 4, 3]
},
{
"name": u"Дмитрий",
"group": "БСТ-2251",
"age": 21,
"marks": [3, 5, 4, 3, 5]
},
{
"name": u"Светлана",
"group": "БСТ-2253",
"age": 20,
"marks": [5, 5, 5, 4, 5]
},
]

def print_students(students):
    print(u"Имя студента".ljust(15), \
    u"Группа".ljust(8), \
    u"Возраст".ljust(8), \
    u"Оценки".ljust(20))
    for student in students:
        print( \
        student["name"].ljust(15), \
        student["group"].ljust(8), \
        str(student["age"]).ljust(8), \
        str(student["marks"]).ljust(20))
    print("\n")

print_students(groupmates)
