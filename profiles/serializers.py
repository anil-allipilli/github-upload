
from .models import *
from rest_framework import serializers
from subjects.serializers import GradeSerializer, SectionSerializer, SubjectSerializer
from accounts.serializers import MyUserSerializer


class DriverSerializer(serializers.ModelSerializer):  

    class Meta:
        model = Driver
        fields = ('id', 'name', 'profile_pic',  'date_of_birth','previous_work_experience', 'driving_licence',  'proof_of_address', 'address', 'phone_number_1', 'phone_number_2')

class BusSerializer(serializers.ModelSerializer):   
    
    bus_driver = DriverSerializer()
    class Meta:
        model = Bus
        fields = ('id', 'bus_identification', 'bus_driver')


class PhysicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Physician
        fields = ('id', 'name', 'profile_pic', 'previous_work_experience',  'proof_of_address', 'address', 'phone_number_1', 'phone_number_2')

class WorkingStaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkingStaff
        fields = ('id', 'name', 'profile_pic',  'job_description','previous_work_experience',  'proof_of_address', 'address', 'phone_number_1', 'phone_number_2')

class ManagementStaffSerializer(serializers.ModelSerializer):
    name = MyUserSerializer()
    class Meta:
        model = ManagementStaff
        fields = ('id', 'name', 'profile_pic',  'job_description','previous_work_experience',  'proof_of_address', 'address', 'phone_number_1', 'phone_number_2')


class StudentSerializer(serializers.ModelSerializer):
    student         = MyUserSerializer()
    student_grade   = GradeSerializer()
    student_section = SectionSerializer()
    transport       = BusSerializer()

    class Meta:
        model = Scholar
        fields = ('id', 'student', 'student_grade', 'student_section', 'profile_pic', 'date_of_birth', 'transport', 'address', 'phone_number_1', 'phone_number_2')

class TeacherSerializer(serializers.ModelSerializer):
    teacher             = MyUserSerializer()
    teacher_subjects    = SubjectSerializer(many=True)

    class Meta:
        model = SchoolTeacher
        fields = ('id', 'teacher', 'profile_pic', 'date_of_birth', 'teacher_subjects', 'resume', 'address', 'phone_number_1', 'phone_number_2')

class GaurdianSerializer(serializers.ModelSerializer):
    
    parent             = MyUserSerializer()
    children           = StudentSerializer(many=True)
    class Meta:
        model = Gaurdian
        fields = ('id', 'parent', 'children', 'profile_pic', 'date_of_birth', 'address', 'phone_number_1', 'phone_number_2')

class StudentPerformanceProfileSerializer(serializers.ModelSerializer):
    
    student_name             = StudentSerializer()
    
    class Meta:
        model = StudentPerformanceProfile
        fields = ('id', 'student_name')




class StudentMedicalInformationProfileSerializer(serializers.ModelSerializer):

    student_name                = StudentSerializer()
    assigned_physician          = PhysicianSerializer()   

    class Meta:
        model = StudentMedicalInformationProfile
        fields = ('id', 'student_name', 'assigned_physician', 'medical_form')

class StudentTaskProfileSerializer(serializers.ModelSerializer):
    """model to maintain all student related activities"""

    student_name = StudentSerializer()
    class Meta:
        model = StudentTaskProfile
        fields = ('id', 'student_name')

class MedicalAssistanceSerializer(serializers.ModelSerializer):

    medical_profile             = StudentMedicalInformationProfileSerializer()
    assisted_physician          = PhysicianSerializer()
    
    class Meta:
        model = MedicalAssistance
        fields = ('id', 'medical_profile', 'assisted_physician')

class TeacherTaskProfileSerializer(serializers.ModelSerializer):
    
    teacher_name                = TeacherSerializer()
    class Meta:
        model = TeacherTaskProfile
        fields = ('id', 'teacher_name')

class ParentTaskProfileSerializer(serializers.ModelSerializer):
    
    parent                = GaurdianSerializer()
    class Meta:
        model = ParentTaskProfile
        fields = ('id', 'parent')