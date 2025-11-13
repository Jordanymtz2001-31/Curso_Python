from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CitaViewSet, ListarPacientes, ListarMedicos, GuardarPaciente, GuardarMedico, DetallePacienteMedico

router = DefaultRouter()
router.register('citas', CitaViewSet)

urlpatterns = router.urls

# Creamos las rutas personalizadas para los metodos de microservicios
urlpatterns += [
    path('pacientes/', ListarPacientes.as_view(), name='listar_pacientes'),
    path('medicos/', ListarMedicos.as_view(), name='listar_medicos'),
    path('pacientes/guardar/', GuardarPaciente.as_view(), name='guardar_paciente'),
    path('medicos/guardar/', GuardarMedico.as_view(), name='guardar_medico'),
    path('detalle/<int:id_cita>/', DetallePacienteMedico.as_view(), name='detalle_paciente_medico'),
]

