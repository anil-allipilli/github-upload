from .models import Grade, Subject, Section
from rest_framework import serializers


class GradeSerializer(serializers.HyperlinkedModelSerializer):

    subjects = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='api:subject-detail',
        lookup_field='pk')

    class Meta:
        model = Grade
        fields = ['grade', 'subjects']


class SubjectSerializer(serializers.HyperlinkedModelSerializer):  

    subject_grade = serializers.HyperlinkedIdentityField(        
        read_only=True,
        view_name='api:grade-detail',
        lookup_field='pk')

    subject = serializers.HyperlinkedIdentityField(        
        read_only=True,
        view_name='api:subject-detail',
        lookup_field='pk')

    class Meta:
        model = Subject
        fields = ('subject_grade', 'subject', 'is_language')

class SectionSerializer(serializers.ModelSerializer):   
    section_grade = serializers.HyperlinkedIdentityField(
        
        read_only=True,
        view_name='api:grade-detail',
        lookup_field='pk')

    class Meta:
        model = Section
        fields = ('section_grade', 'section')