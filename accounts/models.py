from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import post_save
from django.dispatch import receiver


class MyUserManager(UserManager):


    def create_student(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_student', True)
        extra_fields.setdefault('is_teacher', False)
        extra_fields.setdefault('is_parent', False)
        extra_fields.setdefault('is_physician', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_teacher(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_student', False)
        extra_fields.setdefault('is_teacher', True)
        extra_fields.setdefault('is_parent', False)
        extra_fields.setdefault('is_physician', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)
    
    def create_parent(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_student', False)
        extra_fields.setdefault('is_teacher', False)
        extra_fields.setdefault('is_parent', True)
        extra_fields.setdefault('is_physician', False)
        extra_fields.setdefault('is_staff', False)        
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_physician(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_student', False)
        extra_fields.setdefault('is_teacher', False)
        extra_fields.setdefault('is_parent', False)
        extra_fields.setdefault('is_physician', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)




class MyUser(AbstractUser):

    is_student = models.BooleanField(
        _('student'),
        default=True,
        help_text=_('Designates whether the user is a student'),
    )
    is_teacher = models.BooleanField(
        _('teacher status'),
        default=False,
        help_text=_('Designates whether the user is a teacher.'),
    )
    is_parent = models.BooleanField(
        _('parent status'),
        default=False,
        help_text=_('Designates whether the user is a parent.'),
    )
    is_physician = models.BooleanField(
        _('physician status'),
        default=False,
        help_text=_('Designates whether the user is a physician.'),
    )
    

    




    objects = MyUserManager()

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username




# from profiles.models import Scholar, SchoolTeacher, Gaurdian, Physician, ManagementStaff

# @receiver(post_save, sender=MyUser)
# def ensure_account_exists(sender, **kwargs):
#     if kwargs.get('created', False):
#         print(kwargs)
#         if kwargs.get('instance').is_student:
#             Scholar.objects.get_or_create(student=kwargs.get('instance'))
#         if kwargs.get('instance').is_teacher:
#             SchoolTeacher.objects.get_or_create(teacher=kwargs.get('instance'))
#         if kwargs.get('instance').is_parent:
#             Gaurdian.objects.get_or_create(parent=kwargs.get('instance'))
#         if kwargs.get('instance').is_physician:
#             Physician.objects.get_or_create(name=kwargs.get('instance'))
#         if kwargs.get('instance').is_staff:
#             ManagementStaff.objects.get_or_create(name=kwargs.get('instance'))