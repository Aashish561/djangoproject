import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_system.settings')
import django
django.setup()

from faker import Faker
from students.models import DepartmentAdmin, Student

fake = Faker()

def create_data():
    # Create department admins
    departments = ['BIT', 'BCS', 'BCA', 'CSIT', 'BHM']
    for dept in departments:
        username = f"{dept.lower()}_admin"
        DepartmentAdmin.objects.create_user(
            username=username,
            password=f"{dept}@12345",
            department=dept,
            is_staff=True
        )
    
    # Create 20 students
    for i in range(1, 21):
        dept = departments[i % 5]
        admin = DepartmentAdmin.objects.get(username=f"{dept.lower()}_admin")
        Student.objects.create(
            student_id=f"STU{1000+i}",
            name=fake.name(),
            department=dept,
            address=fake.address(),
            email=fake.email(),
            phone=fake.phone_number(),
            created_by=admin
        )

if __name__ == '__main__':
    create_data()