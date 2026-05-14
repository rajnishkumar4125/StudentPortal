from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    # Only run this for the 'students' app
    if sender.name == 'students':
        roles = ['Admin', 'Teacher', 'Student', 'Parents']
        for role in roles:
            Group.objects.get_or_create(name=role)