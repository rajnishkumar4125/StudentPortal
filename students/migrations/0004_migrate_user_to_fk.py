# Generated manually - comprehensive migration from CharField to ForeignKey

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.contrib.auth.models import User


def migrate_user_field(apps, schema_editor):
    """
    Migrate user field from CharField to ForeignKey.
    1. Create User objects from student names
    2. Update student.user_id to reference the user IDs
    """
    Student = apps.get_model('students', 'Student')
    
    # Get all students with usernames
    students = Student.objects.all()
    
    for student in students:
        if student.user and isinstance(student.user, str) and student.user.strip():
            username = student.user
            # Create or get the user
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'first_name': username,
                    'email': f'{username.lower()}@example.com'
                }
            )


def reverse_migrate(apps, schema_editor):
    """Cannot safely reverse this migration"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_profile_pic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # Step 1: Create User objects from string usernames
        migrations.RunPython(migrate_user_field, reverse_migrate),
        
        # Step 2: Add temporary user_id field that will link to User
        migrations.AddField(
            model_name='student',
            name='user_id_temp',
            field=models.IntegerField(null=True, blank=True),
        ),
        
        # Step 3: Raw SQL to update user_id_temp based on username matching
        migrations.RunSQL(
            sql="""
            UPDATE students_student 
            SET user_id_temp = (
                SELECT id FROM auth_user WHERE auth_user.username = students_student.user
            )
            WHERE students_student.user IS NOT NULL;
            """,
            reverse_sql="""
            UPDATE students_student SET user_id_temp = NULL;
            """
        ),
        
        # Step 4: Remove old user CharField
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        
        # Step 5: Rename and convert user_id_temp to proper ForeignKey
        migrations.RenameField(
            model_name='student',
            old_name='user_id_temp',
            new_name='user',
        ),
        
        # Step 6: Alter field to be a ForeignKey
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
