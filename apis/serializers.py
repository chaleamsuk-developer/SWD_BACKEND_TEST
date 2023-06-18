# serializers.py
from rest_framework import serializers
from apis.models import SchoolStructure,StudentSubjectsScore,Subjects,Personnel,Classes,Schools

class SchoolStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolStructure
        fields = '__all__' 
        
class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('title')
        
class StudentSubjectsScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubjectsScore
        fields = ('student','subjects','credit','score')

class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = ('title')

class ClassesSerializer(serializers.ModelSerializer):
    schools_set = SchoolsSerializer(many=True, read_only=True)
    class Meta:
        model = Classes
        fields = ('class_order', 'schools_set')

class PersonnelSerializer(serializers.ModelSerializer):
    classes_set = ClassesSerializer(many=True, read_only=True)
    class Meta:
        model = Personnel
        fields = ('first_name','last_name','personnel_type','classes_set')