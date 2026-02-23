from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Estudiante, Curso

@receiver(m2m_changed, sender=Estudiante.cursos.through)
def gestionar_cupo_curso(sender, instance, action, pk_set, **kwargs):
    """
    Se ejecuta CUANDO:
    - +1 estudiante se inscribe (action='post_add')
    - -1 estudiante se elimina (action='pre_remove')
    """
    if action == 'post_add':  # Nuevo estudiante inscrito
        for curso in instance.cursos.all():
            if curso.estudiantes.count() >= curso.cupo_maximo:
                curso.activo = False
                curso.save(update_fields=['activo'])
                print(f"✅ Curso '{curso.nombre}' DESACTIVADO - lleno")
    
    elif action == 'pre_remove':  # Estudiante se elimina
        # Reactiva si hay cupo disponible
        for curso in instance.cursos.all():
            if curso.estudiantes.count() < curso.cupo_maximo:
                curso.activo = True
                curso.save(update_fields=['activo'])
                print(f"✅ Curso '{curso.nombre}' REACTIVADO - hay cupo")
