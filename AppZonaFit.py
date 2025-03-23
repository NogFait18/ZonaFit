from clientedao import ClienteDAO
from cliente import Cliente
import os

def borrar_terminal():
    # Borrar la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    print('Menu'.center(50,'-'))
    print('''
        1)Listar clientes
        2)Agregar cliente
        3)Actualizar cliente
        4)Eliminar clientes
        5)Salir
        ''')
    try: 
        opcion = int(input('Ingrese  una opcion (1-5): '))
        borrar_terminal()
        if opcion == 1:
            print(f'Listado de clientes'.center(50,'-'))
            clientes = ClienteDAO.seleccionar()
            for cliente in clientes:
                print(cliente)

        elif opcion == 2:
            print(f'Agregar clientes'.center(50,'-'))
            nombre_var = input('Ingrese su nombre: ')
            apellido_var = input('Ingrese su apellido: ')
            mebresia_var = input('Ingrese su membresia: ')
            cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=mebresia_var)
            cliente_insertados = ClienteDAO.insertar(cliente)
            print(f'cliente insertados: {cliente_insertados}')


        elif opcion == 3:
            print(f'Actualizar cliente'.center(50,'-'))
            id_cliente_var = int(input('Escribre el id_usuario a modificar: '))
            nombre_var = input('Ingrese su nombre: ')
            apellido_var = input('Ingrese su apellido: ')
            mebresia_var = input('Ingrese su membresia: ')
            cliente = Cliente(id=id_cliente_var,nombre=nombre_var, apellido=apellido_var, membresia=mebresia_var)
            cliente_actualizados = ClienteDAO.actualizar(cliente)
            print(f'cliente actualizados: {cliente_actualizados}')


        elif opcion == 4:
            print(f'Eliminar cliente'.center(50,'-'))
            id_cliente_var = int(input('Escribre el id_usuario a eliminar: '))
            cliente = Cliente(id=id_cliente_var)
            cliente_eliminados = ClienteDAO.eliminar(cliente)
            print(f'cliente eliminados: {cliente_eliminados}')

            
        elif opcion == 5:

            print('Salimos de la aplicación!')
            break
        else:
            print('Esa opcion no existe, vuelve a intentarlo')
    except Exception as e:
        print(f'Ocurrio un error: {e}')
