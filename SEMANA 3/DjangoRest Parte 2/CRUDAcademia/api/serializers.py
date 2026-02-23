from rest_framework import serializers
from .models import Curso, Estudiante


class CursoSerializer(serializers.ModelSerializer):
    estudiantes_actuales = serializers.SerializerMethodField()
    
    class Meta:
        model = Curso
        fields = '__all__'
    
    def get_estudiantes_actuales(self, obj):
        return obj.estudiantes.count() 
    
# serializers.py
class EstudianteSerializer(serializers.ModelSerializer):
    cursos = serializers.SlugRelatedField(
        queryset=Curso.objects.filter(activo=True),
        slug_field='nombre',  # "Python" → Curso object
        many=True
    )

    def validate_cursos(self, cursos):
        for curso in cursos:
            alumnos_actuales = curso.estudiantes.count()  
            
            if alumnos_actuales >= curso.cupo_maximo:
                raise serializers.ValidationError(
                    f"El curso '{curso.nombre}' lleno ({alumnos_actuales}/{curso.cupo_maximo})"
                )
        return cursos
    
    #Guarda Alumno + sus Cursos + validaciones
    def create(self, validated_data):
        # Extrae los cursos del JSON
        cursos_data = validated_data.pop('cursos')  # [{"id": 1}, {"id": 2}]
    
        # Crea el Alumno SIN cursos
        alumno = Estudiante.objects.create(**validated_data)  # Solo nombre, email, promedio
    
        #AGREGA cada curso al alumno (¡ESTO es la magia!)
        for curso in cursos_data:
            alumno.cursos.add(curso)  # Crea la relación ManyToMany
    
        return alumno  # Devuelve el alumno COMPLETO
    
    class Meta:
        model = Estudiante
        fields = '__all__'

