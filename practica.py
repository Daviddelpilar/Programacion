class Aplicacion: #creo una clase llamada Aplicacion 
    print('Bienvenido a nuestra aplicacion') #hago un print dando la bienvenida al cliente al entrar en la aplicacion 
    print('Por favor rellene los siguientes datos: ') #hago otro print para pedir al cliente que rellene lo siguiente

class Tienda(Aplicacion): #Creo otra clase, haciendo una herencia dentro de la clase padre Aplicacion
    def __init__(self) -> None: #uso el def __init para poder asignar variables
        self.nombre_apellidos=input('Introduzca su nombre y apellidos: ')
        self.telefono=input('Introduzca su numero de telefono: ')
        self.correo=input('Introduzca su correo: ')
        self.contraseña=input('Introduzca la contraseña: ')
        self.dni=input('Introduzca su DNI: ')
        self.direccion=input('Introduzca su dirreccion: ')
        self.codigo_postal=input('Introduza su codigo postal: ')
#Estas secunencias de self sirven para que el programa le pregunte al cliente una serie de preguntas

    def confirmarRegistro(self): #creo una funcion para poder confirmar el registro del cliente
        print(f'{self.nombre_apellidos} con DNI {self.dni} sus datos se han guardado correctamente')
        #hago un print para poder decirle al cliente que sus datos se han guardado
        print(f'Enhorabuena {self.nombre_apellidos} ha quedado registrado')#hago un print para decirle al cliente que se ha registrado
    
    def comprarProducto(self): #creo una nueva funcion para poder saber la compra del cliente
        print('Eliga el producto que quiera: ')

        productos=['camisa','guantes','zapatillas','pantalones','sombrero'] #creo una lista con los productos que se venden
        listaFinal=[]#creo otra lista para poder almacenar el precio
        while True: 
            digito=input('''
            A. Introduzca el producto
            B. Mostrar el precio total
            C. Terminar compra
            Introduzca''').capitalize() #Aqui mediante unos input le hago una informacion al 
            #cliente sobre la compra que va a realizar. Por ultimo uso el metodo capitalize para 
            #devolver una copia de la cadena con la primera letra en mayusculas

            if digito== 'A':
                print(productos)
                nombre=input('Introduzca el producto que quiere: ') #uso la variable input para preguntar al 
                #cliente sobre el cliente que desea comprar
                if nombre not in productos:
                    print('El producto escogida no lo disponemos')
                    #en caso de que el cliente escoga un producto que no este le saldra un mensaje
                    #de que ese producto no esta disponible

                else:
                    almacen=productos.index(nombre) #asigno la variable almacen para organizar todo
                    precio=precios[almacen]

                    print(f'El precio es {precio}')
                    listaFinal.append(precio) #adjunto el metodo append para adjuntar el precio total

            elif digito=='B':
                precioTotal=sum(listaFinal) #asigno precioTotal a la suma para calcular el total
                print(f'El precio total es {precioTotal}€') #hago un print para que le informe al cliente del precio total

            elif digito=='C':
                precioTotal=sum(listaFinal) #hace que salga el precio total de las compras


                print('Si reisde en España, Francia, Rusia, Inglaterra, el iva se aplicara a la comprar si su pais no esta sera un 23%')

                pais=input('Introduzca su pais: ')

                if pais=='España':
                    print('El IVA es del 21%')
                    precioTotalIva=precioTotal*1.21
                    print(f'El precio total en España es {precioTotalIva}€')
                    #aqui mediante unos metodos calculo el precio total con su correspondiente iva

                elif pais=='Francia':
                    print('El IVA es del 20%')
                    precioTotalIva=precioTotal*1.20
                    print(f'El precio total en Francia es {precioTotalIva}€')
                    
                
                elif pais=='Rusia':
                    print('El IVA es del 18%')
                    precioTotalIva=precioTotal*1.18
                    print(f'El precio total en Rusia es {precioTotalIva}€')
                
                
                elif pais=='Inglaterra0':
                    print('El IVA es del 20%')
                    precioTotalIva=precioTotal*1.20
                    print(f'El precio total en Inglaterra es {precioTotalIva}€')
                    
                else:
                    print('El IVA es del 24%')
                    precioTotalIva=precioTotal*1.24
                    print(f'El precio total en su pais es {precioTotalIva}€')
                    #aqui hago otro metodo para sacar el precio de la compra con un pais que no sale en la lista


                    print(f'Su compra ha sido realizada con exito con un coste de {precioTotalIva}€')
                    #aqui sale un resumen de la compra dando el coste final de la compra

                    print(f'Se ha enviado un importe de la compra a su correo registrado')

                    print(f'El seguimiento de su producto lo podra realizar en el correo {self.correo}')

                    print(f'Gracias por realizar la compra, estimado {self.nombre_apellidos}')

                    break
cliente1=Tienda()#asigno una variable para poder asignar y meterle las funciones 
cliente1.confirmarRegistro()#esta funcion es para poder confirmar el registro
cliente1.comprarProducto()#esta funcion sirve para ejecutar la compra