from django.db import connection

def ejecutar_proc_postres(id_postre, tipo, precio, evento):
    with connection.cursor() as cursor:
        cursor.callproc('PR_I_U_D_POSTRES', [id_postre, tipo, precio, evento])
        # fetchall() es un metodo que recupera una lista de tuplas con los resultados de una consulta SQL.
        result = cursor.fetchall()
        # Si result tiene informacion almacenamos la primera fila y columna en la vairable mensaje y si no el mensaje 'Sin mensaje de salida.'
        # result[0] Primera fila
        # result [0][0] Primera columna de la primera fila
        mensaje = result[0][0] if result else 'Sin mensaje de salida.'
        
    return mensaje #Retornamos