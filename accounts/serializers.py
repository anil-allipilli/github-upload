from rest_framework import serializers
from .models import MyUser

class MyUserSerializer(serializers.ModelSerializer):  

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_student', 'is_teacher', 'is_parent', 'is_physician')