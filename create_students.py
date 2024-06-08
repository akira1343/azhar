import json, random, django, os, sys
from faker import Faker
fake = Faker('ru_RU')
num_records = 100
path = '/Users/bykov/work/azhar'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE']='main.settings'
django.setup()

from app.models import Student, Qualification

with open('./students.txt', 'r') as f:
    data = f.read()

    students = []
    q = Qualification.objects.all()

    for i in json.loads(data):
        students.append(Student(
           "name": fake.first_name(),
        "surname": fake.last_name(),
        "middle_name": fake.middle_name(),
        "birthday": fake.date_of_birth(minimum_age=16, maximum_age=18).isoformat(),  # Возраст 16-18 лет (2006-2008 год рождения)
        "phone": fake.phone_number(),
        "iin": random.randint(100000000000, 999999999999),  # Генерация ИИН в формате 12-значного числа
        "nationality": random.choice(["Казахстанец", "Узбек", "Кыргыз", "Туркмен", "Таджик"]),
        "parents": random.choice(["Казахстан", "Узбекистан", "Кыргызстан", "Туркменистан", "Таджикистан"]),
        "education_lang": random.choice([1, 2]),  # 1 - русский, 2 - казахский
        "residence_address": fake.city(),
        "residential_address": fake.address(),
        "avg_certificate": random.randint(50, 100),
        "avg_subject": random.randint(1, 5),
        "pay": random.randint(50, 100),
        "education_type": random.randint(1, 5),
        "status": random.randint(1, 5),
        "qualification": random.randint(1, 5),
        "id": str(fake.uuid4()) 
        ))

    Student.objects.bulk_create(students)
    records = [generate_record() for _ in range(num_records)]

# Преобразование данных в JSON
json_data = json.dumps(records, ensure_ascii=False, indent=4)

# Сохранение данных в файл
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json_data)
