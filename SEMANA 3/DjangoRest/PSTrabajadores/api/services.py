from django.db import connection #Esta libreria gestiona la comunicacion con la bd y es parte del ORM de django.

def ejecutar_respaldo():
    # Un cursor es como un puntero que nos permite ejecutar comandos SQL y recuperar informacion de la base de datos. 
    with connection.cursor() as cursor:
        # with es un context Manager que garantiza que el manejor correcto de los recursos. 
        # callproc es un metodo que ejecuta procedimientos almacenados.
        cursor.callproc('PR_RESPALDO_TRABAJADORES')