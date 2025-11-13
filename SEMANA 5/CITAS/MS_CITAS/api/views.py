import requests
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Cita
from .serializer import CitaSerializer
from rest_framework.views import APIView

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

    # Creamos metodo personalizado de microservicios de pacientes y medicos
    # Aqui la direccion de metodo despues de citas/ es el nombre del metodo
class ListarPacientes(APIView):
    def get(self, request):
        # Llamada al microservicio de pacientes con la url correspondiente
        url = 'http://localhost:8001/pacientes/'

        # Realizamos la solicitud GET al microservicio de pacientes
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json() # Obtener los datos en formato JSON
            return Response(data) # Devolver la respuesta con los datos obtenidos
        else:
            return Response({"error": "No se pudo obtener la lista de pacientes"}, status=response.status_code)
        
class ListarMedicos(APIView):
    def get(self, request):
        # Llamada al microservicio de medicos con la url correspondiente
        url = 'http://localhost:8002/medicos/'

        # Realizamos la solicitud GET al microservicio de medicos
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json() # Obtener los datos en formato JSON
            return Response(data) # Devolver la respuesta con los datos obtenidos
        else:
            return Response({"error": "No se pudo obtener la lista de medicos"}, status=response.status_code)
        
class GuardarPaciente(APIView):
    def post(self, request):
        # Llamada al microservicio de pacientes con la url correspondiente
        url = 'http://localhost:8001/pacientes/'

        # Realizamos la solicitud POST al microservicio de pacientes
        response = requests.post(url, json=request.data)

        if response.status_code == 201:
            data = response.json() # Obtener los datos en formato JSON
            return Response(data) # Devolver la respuesta con los datos obtenidos
        else:
            return Response({"error": "No se pudo guardar el paciente"}, status=response.status_code)
        

class GuardarMedico(APIView):
    def post(self, request):
        # Llamada al microservicio de medicos con la url correspondiente
        url = 'http://localhost:8002/medicos/'

        # Realizamos la solicitud POST al microservicio de medicos
        response = requests.post(url, json=request.data)

        if response.status_code == 201:
            data = response.json() # Obtener los datos en formato JSON
            return Response(data) # Devolver la respuesta con los datos obtenidos
        else:
            return Response({"error": "No se pudo guardar el medico"}, status=response.status_code)
        
    # Metodo de ambos servicios con su id que consulte un solo registro junto que las citas
class DetallePacienteMedico(APIView):
    def get(self, request, id_cita):

    # Buscamos la cita por su id si existe o no
        try: 
            cita = Cita.objects.get(id_cita=id_cita)

            # Llamada al microservicio de pacientes con la url correspondiente
            url_paciente = f'http://localhost:8001/pacientes/{cita.id_cita}/'
            url_medico = f'http://localhost:8002/medicos/{cita.id_cita}/'

            # Realizamos la solicitud GET al microservicio de pacientes
            response_paciente = requests.get(url_paciente)
            response_medico = requests.get(url_medico)

            # Verificamos si ambas solicitudes fueron exitosas
            if response_paciente.status_code == 200 and response_medico.status_code == 200:
                data_paciente = response_paciente.json() # Obtener los datos en formato JSON
                data_medico = response_medico.json() # Obtener los datos en formato JSON

                # Devolver la respuesta con los datos obtenidos  junto con los datos de la cita
                return Response({
                    "cita": {
                        "id": cita.id_cita,
                        "motivo": cita.motivo,
                        "fecha_hora": cita.fecha_hora
                    },
                    "paciente": data_paciente,
                    "medico": data_medico,
                
                }) # Devolver la respuesta con los datos obtenidos
            else:
                return Response({"error": "No se pudo obtener el detalle del paciente o medico"}, status=400)
        except Cita.DoesNotExist:
            return Response({"error": "La cita no existe"}, status=404)