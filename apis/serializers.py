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

class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = ('title')

class ClassesSerializer(serializers.ModelSerializer):
    school = SchoolsSerializer(many=True, read_only=True)
    class Meta:
        model = Classes
        fields = '__all__' 

class PersonnelSerializer(serializers.ModelSerializer):
    classes = ClassesSerializer(many=True, read_only=True)
    class Meta:
        model = Personnel
        fields = '__all__' 

class StudentSubjectsScoreSerializer(serializers.ModelSerializer):
    personel = PersonnelSerializer(many=True, read_only=True)
    subject = SubjectsSerializer(many=True, read_only=True)
    
    class Meta:
        model = StudentSubjectsScore
        fields = ('student','subjects','credit','score','personel','subject')
