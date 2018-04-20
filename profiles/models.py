# from django.db import models
# from accounts.models import MyUser as User
# # from grades.models import Grade, Section, Subject
# from django.db.models.signals import post_save
# from django.dispatch import receiver



# class Driver(models.Model):
#     name                        = models.CharField(max_length=1024)
#     profile_pic                 = models.ImageField(upload_to="profile_pic/", default = 'pic_folder/None/no-img.jpg')
#     date_of_birth               = models.DateField(null=True)
#     previous_work_experience    = models.TextField(null=True)
#     driving_licence             = models.FileField(null=True)
#     address                     = models.TextField(max_length=2048, null=True)
#     proof_of_address            = models.FileField(upload_to="proofs/", null=True)
#     phone_number_1              = models.CharField(max_length=12, null=True)
#     phone_number_2              = models.CharField(max_length=12, null=True)

#     def __str__(self):
#         return self.name

# class Bus(models.Model):
#     bus_identification          = models.CharField(max_length=12)
#     bus_driver                  = models.ForeignKey(Driver)

# class Physician(models.Model):
#     name                        = models.CharField(max_length=1024)
#     profile_pic                 = models.ImageField(upload_to="profile_pic/", default = 'pic_folder/None/no-img.jpg')
#     previous_work_experience    = models.TextField(null=True)
#     physician_licence           = models.FileField(null=True)
#     address                     = models.TextField(max_length=2048, null=True)
#     proof_of_address            = models.FileField(upload_to="proofs/", null=True)
#     phone_number_1              = models.CharField(max_length=12, null=True)
#     phone_number_2              = models.CharField(max_length=12, null=True)
#     def __str__(self):
#         return self.name
    
# class WorkingStaff(models.Model):
#     name                        = models.CharField(max_length=1024)
#     profile_pic                 = models.ImageField(upload_to="profile_pic/", default = 'pic_folder/None/no-img.jpg')
#     previous_work_experience    = models.TextField(null=True)
#     job_description             = models.TextField(null=True)
#     address                     = models.TextField(max_length=2048, null=True)
#     proof_of_address            = models.FileField(upload_to="proofs/", null=True)
#     phone_number_1              = models.CharField(max_length=12, null=True)
#     phone_number_2              = models.CharField(max_length=12, null=True)
#     def __str__(self):
#         return self.name

# class ManagementStaff(models.Model):
#     name                        = models.OneToOneField(User, limit_choices_to={'is_staff': True})
#     profile_pic                 = models.ImageField(upload_to="profile_pic/", default = 'pic_folder/None/no-img.jpg')
#     previous_work_experience    = models.TextField(null=True)
#     job_description             = models.TextField(null=True)
#     address                     = models.TextField(max_length=2048, null=True)
#     proof_of_address            = models.FileField(upload_to="proofs/", null=True)
#     phone_number_1              = models.CharField(max_length=12, null=True)
#     phone_number_2              = models.CharField(max_length=12, null=True)
#     def __str__(self):
#         return self.name.username




# class Scholar(models.Model):

#     student                     = models.OneToOneField(User, limit_choices_to={'is_student': True})
#     student_grade               = models.ForeignKey(Grade, null=True)
#     student_section             = models.ForeignKey(Section, null=True)
#     profile_pic                 = models.ImageField(upload_to="profile_pic/", default = 'pic_folder/None/no-img.jpg')
#     date_of_birth               = models.DateField(null=True)
#     transport                   = models.ForeignKey(Bus, null=True)
#     address                     = models.TextField(max_length=2048, null=True)
#     phone_number_1              = models.CharField(max_length=12, null=True)
#     phone_number_2              = models.CharField(max_length=12, null=True)
 
#     def __str__(self):
#         return self.student.username

# class SchoolTeacher(models.Model):
    
#     teacher                     = models.OneToOneField(User, limit_choices_to={'is_teacher': True})
#     profile_pic                 = models.ImageField(upload_to="profile_pic/", default = 'pic_folder/None/no-img.jpg')
#     date_of_birth               = models.DateField(null=True)
#     teacher_subjects            = models.ManyToManyField(Subject)
#     resume                      = models.FileField(upload_to="resumes/", null=True)
#     address                     = models.TextField(max_length=2048, null=True)
#     proof_of_address            = models.FileField(upload_to="proofs/", null=True)
#     phone_number_1              = models.CharField(max_length=12, null=True)
#     phone_number_2              = models.CharField(max_length=12, null=True)

#     def __str__(self):
#         return self.teacher.username

# class Gaurdian(models.Model):
    
#     parent                      = models.OneToOneField(User, limit_choices_to={'is_parent': True})
#     profile_pic                 = models.ImageField(upload_to="profile_pic/", default = 'pic_folder/None/no-img.jpg')
#     children                    = models.ManyToManyField(Scholar)
#     date_of_birth               = models.DateField(null=True)
#     address                     = models.TextField(max_length=2048, null=True)
#     proof_of_address            = models.FileField(upload_to="proofs/", null=True)
#     phone_number_1              = models.CharField(max_length=12, null=True)
#     phone_number_2              = models.CharField(max_length=12, null=True)

#     def __str__(self):
#         return self.parent.username

# class StudentPerformanceProfile(models.Model):
    
#     student_name                = models.OneToOneField(Scholar)


# class StudentMedicalInformationProfile(models.Model):

#     student_name                = models.OneToOneField(Scholar)
#     assigned_physician          = models.ForeignKey(Physician)
#     medical_form                = models.FileField(upload_to="medical_forms/")

# class StudentTaskProfile(models.Model):
#     """model to maintain all student related activities"""

#     student_name = models.OneToOneField(Scholar)

# class MedicalAssistance(models.Model):

#     medical_profile             = models.ForeignKey(StudentMedicalInformationProfile)
#     assisted_physician          = models.ForeignKey(Physician)
#     description_of_assistance   = models.TextField(max_length=3072)

# class TeacherTaskProfile(models.Model):
    
#     teacher_name                = models.OneToOneField(SchoolTeacher)

# class ParentTaskProfile(models.Model):
    
#     parent_name                = models.OneToOneField(Gaurdian)

# @receiver(post_save, sender=Scholar)
# def ensure_account_exists(sender, **kwargs):
#     if kwargs.get('created', False):
#         StudentMedicalInformationProfile.objects.get_or_create(student_name=kwargs.get('instance'))        
#         StudentPerformanceProfile.objects.get_or_create(student_name=kwargs.get('instance'))
#         StudentTaskProfile.objects.get_or_create(student_name=kwargs.get('instance'))

# @receiver(post_save, sender=SchoolTeacher)
# def ensure_account_exists(sender, **kwargs):
#     if kwargs.get('created', False):
#         TeacherTaskProfile.objects.get_or_create(teacher_name=kwargs.get('instance'))        
        
# @receiver(post_save, sender=Gaurdian)
# def ensure_account_exists(sender, **kwargs):
#     if kwargs.get('created', False):
#         ParentTaskProfile.objects.get_or_create(parent_name=kwargs.get('instance'))        
        