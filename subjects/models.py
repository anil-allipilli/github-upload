from django.db import models





class Grade(models.Model):
    grade               = models.CharField(max_length=8)  

    def __str__(self):
        return self.grade

class Subject(models.Model):
    subject_grade       = models.ForeignKey(Grade, related_name='subjects', on_delete=models.CASCADE) 
    subject             = models.CharField(max_length=20)    
    is_language         = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    def __unicode__(self):
        return self.subject



class Section(models.Model):

    section_grade       = models.ForeignKey(Grade, related_name='sections', on_delete=models.CASCADE)
    section             = models.CharField(max_length=2)

    def __str__(self):
        return str(self.grade) + " " + str(self.section_grade)
