from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
       conexion = None
       try:
        conexion = Conexion.obtener_Conexion()
        cursor = conexion.cursor()
        cursor.execute(cls.SELECCIONAR)
        registros = cursor.fetchall()
        #Mapeo de clase-tabla cliente
        clientes = []
        for registro in registros:
           cliente = Cliente(registro[0],registro[1],
                             registro[2],registro[3])
           clientes.append(cliente)
        return clientes
       except Exception as e:
          print(f'Ocurrio un error al seleccionar clientes {e}')
       finally:
          if conexion is not None:
             cursor.close()
             Conexion.liberar_Conexion(conexion)
    
    @classmethod
    def insertar(cls, cliente):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_Conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount  # ✅ Devuelve el número de filas insertadas correctamente
        except Exception as e:
            print(f'Ocurrió un error al insertar el cliente: {e}')
            return 0  # ✅ Retorna 0 en caso de error en lugar de None
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.liberar_Conexion(conexion)
    
    @classmethod
    def actualizar(cls,cliente):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_Conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, 
                        cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR,valores)
            conexion.commit()
            return cursor.rowcount  # ✅ Devuelve el número de filas insertadas correctamente
        except Exception as e:
            print(f'Ocurrió un error al insertar el cliente: {e}')
            return 0  # ✅ Retorna 0 en caso de error en lugar de None
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.liberar_Conexion(conexion)
    
    @classmethod
    def eliminar(cls,cliente):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_Conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR,valores)
            conexion.commit()
            return cursor.rowcount  # ✅ Devuelve el número de filas insertadas correctamente
        except Exception as e:
            print(f'Ocurrió un error al insertar el cliente: {e}')
            return 0  # ✅ Retorna 0 en caso de error en lugar de None
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.liberar_Conexion(conexion)

