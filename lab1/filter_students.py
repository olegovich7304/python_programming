#coding:utf-8
groupmates = [
    {
        "name": "Александр",
        "surname": "Миронов",
        "exams": ["АиС", "СУБД", "МиСПИСиТ"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Виктория",
        "surname": "Соколова",
        "exams": ["АиС", "СУБД", "МиСПИСиТ"],
        "marks": [3, 4, 5]
    },
    {
        "name": "Даниил",
        "surname": "Орлов",
        "exams": ["АиС", "СУБД", "МиСПИСиТ"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Мария",
        "surname": "Ковалёва",
        "exams": ["АиС", "СУБД", "МиСПИСиТ"],
        "marks": [3, 4, 3]
    },
    {
        "name": "Кирилл",
        "surname": "Лебедев",
        "exams": ["АиС", "СУБД", "МиСПИСиТ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Алина",
        "surname": "Воронцова",
        "exams": ["АиС", "СУБД", "МиСПИСиТ"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Максим",
        "surname": "Тихонов",
        "exams": ["АиС", "СУБД", "МиСПИСиТ"],
        "marks": [5, 5, 5]
    }
]
def filter_students(students, middle):
    print("Имя".ljust(15), "Фамилия".ljust(15), "Экзамены".ljust(30), "Оценки".ljust(20), "Средний балл")
    for student in students:
        total = 0
        for mark in student["marks"]:
            total = total + mark
        average = total / len(student["marks"])
        if round(average, 2) > middle:
            print(
                student["name"].ljust(15),
                student["surname"].ljust(15),
                str(student["exams"]).ljust(30),
                str(student["marks"]).ljust(20),
                round(average, 2)
            )
mid = float(input("Введите минимальный средний балл: "))
filter_students(groupmates, mid)
