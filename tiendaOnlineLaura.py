import re

class TiendaOnline:
    
    def __init__(self,ventas_totales = float(0)): # definimos los atributos de la clase
    # ponemos un valor por defecto de tipo float de ventas totales que es 0, tambien podriamos poner directamente 0.0
        self.ventas_totales = ventas_totales
        self.inventario = [] # Es una lista vacia en la que iremos añadiendo diccionarios con los datos de cada producto
        self.clientes = {} # Es un diccionario vacio sobre el que iremos añadiendo diccionarios con los datos de los clientes
        self.compras_clientes = {} #Es un diccionario vacio, sobre el que iremos añadiendo lista de diccionarios (carritos)
    # a partir de aqui creamos los metodos asociados a la clase
    
    def agregar_producto(self,nombre,precio,cantidad):
        
        existe = False 
        for elemento in self.inventario: # lo primero es iterar el inventario para tratar de buscar el producto
        
            if nombre in elemento.values(): # si el elemento existe actualizamos la cantidad de dicho producto
                existe = True # si se encuentra el elemento existe pasa a ser True, por lo que el segundo condicional no se ejecuta
                print('elemento ya en inventario, modifico cantidad')
                cantidad = cantidad + elemento['cantidad']
                elemento ['cantidad'] = cantidad
                print(f"El inventario actualizado es => {self.inventario}") # imprimimos un mensaje donde se da informacion del inventario actual
                
        if existe == False: # esto solo se acciona si despues de itera toda la lista no se encuentra el producto
            # si despues de iterar TODO el inventario el elemento no se encuentra entonces añadimos un nuevo diccionario con el producto nuevo
            print('Este producto no esta en nuestro inventario, lo añadimos')
            self.inventario.extend([{'nombre': nombre, 'precio': precio,'cantidad': cantidad}])
            print(f"El inventario actualizado es => {self.inventario}") # imprimimos un mensaje donde se da informacion del inventario actual
        
    def ver_inventario(self):
        for elemento in self.inventario: # iteramos la lista que contiene los diccionarios con cada producto
            for key, value in elemento.items(): # iteramos cada diccionario dentro de la lista
                print(key.capitalize(), ":", value) 
                # Imprimimos las keys en mayusculas seguidas de : y su valor ("Nombre": nombre producto, "Precio" : numero, "Cantidad:numero"        
            print('................\n')
    def buscar_producto(self,nombre):
        existe = False 
        for elemento in self.inventario: # iteramos la lista del inventario
            if nombre in elemento.values(): # si el nombre se encuentra en los valores del diccionario (concretamente el par que va con "Nombre")
                existe = True
                for key,value in elemento.items(): # iteramos el diccionario que contiene el producto
                    print(key.capitalize(), ":", value) # Imprimimos los datos del producto en cuestión
        if existe == False:
            print("Producto no encontrado")
                     
    def actualizar_stock (self,nombre,cantidad): 
        existe = False    # Ponemos una condicion existe, que va a ser False, a no ser que encontremos el elemento, caso en el que se transformara en True
        for elemento in self.inventario: # Iteramos el inventario
            if nombre in elemento.values(): # Si encontramos el producto cambiamos existe a True, y se ejecuta este condicional, actualizando la cantidad
                existe = True
                cantidad = elemento["cantidad"] + cantidad
                elemento["cantidad"] = cantidad
                print(f"Producto ya está en inventario, actualizamos su stock, el stock de este producto actualizado es {elemento}")
        if  existe == False:  
            print("El producto no se encuentra en nuestro inventario") # si el producto no se encuentra, se imprime mensaje comunicandolo 

    def eliminar_producto (self,nombre): 
        existe = False    
        for elemento in self.inventario: # Iteramos todo el inventario, si encuentra el elemento cambia la condicion a True y elimina el elemento
            if nombre in elemento.values():
                existe = True
                self.inventario.remove(elemento)
                print(f"Elemento {nombre} correctamente eliminado, el inventario actualizado es {self.inventario}") 
                # Imprimimos mensaje mostrando el producto eliminado y el inventario actual. 
                
        if  existe == False:  
            #si despues de iterar todo el inventario no encuentra el elemento, la condicion existe seguirá siendo False y se ejecuta este condicional
            print("El producto no se encuentra en nuestro inventario") # Imprimimos mensaje comunicando que no está el producto. 
                    
    def calcular_valor_inventario(self):
        suma = 0 # generamos una variable neutra suma que será la que iremos incrementando en cada iteración
        for producto in self.inventario: #iteramos inventario
            valor_producto = producto["cantidad"] * producto["precio"] # creamos variable valor_producto: que es precio * la cantidad
            print(f'{producto["nombre"]} valor total: {valor_producto} euros' ) # Imprimo el valor asociado a cada producto
            suma += valor_producto 
            # en cada vuelta del bucle sumamos el valor de cada producto con el producto siguiente, y así sucesivamente hasta que termine el bucle
        print(f"El valor de nuestro inventario actual es {suma} euros") # Imprimimos mensaje mostrando el valor total
    
    def realizar_compra(self):
        
        carrito = {} # generamos una lista vacia para poder ir metiendo los productos que seleccione el cliente
        coste= 0 # genero una variable neutra para ir guardando el coste total
        while True: # genero un bucle while para que el cliente pueda ir realizando las compras que quiera
            existe_inventario = False
            # le muestro al cliente el inventario para que nos diga qué quiere
            # genero una variable seleccion_producto que tomara como valor el input que meta el cliente
            seleccion_producto = input("Dime que productos quieres comprar de los que figuran en el inventario \n(cuando no quieras añadir más productos al carrito escribe fin): ")    
            print(f"Has seleccionado : {seleccion_producto}")
            if seleccion_producto.lower() == "fin": # genero una condicion que rompe el bucle, para cuando el cliente decida parar de comprar
                break
            
            precio_producto_actual = 0
            for elemento in self.inventario: # itero nuestro inventario
                if seleccion_producto.lower() in elemento.values(): # si el producto está en el inventario se ejecuta este if
                    existe_inventario = True
                    cantidad_producto = int(input(f"Dime cuantas unidades quieres de {seleccion_producto}: ")) 
                    # genero una varible cantidad_producto que toma el valor transformado a un integer para que nos diga la cantidad
                    print(f"Has seleccionado {cantidad_producto} unidades")
                    if cantidad_producto > elemento['cantidad']: 
                        # verificamos que disponemos cantidad suficiente en el inventario, si no la tenemos imprimimos mensaje
                        print("lo siento, no tenemos stock suficiente")
                        break 
                    elemento['cantidad'] = elemento['cantidad'] - cantidad_producto
                    coste_actual = cantidad_producto * elemento['precio']
                    coste += coste_actual
                    precio_producto_actual = elemento['precio']
                    print('coste actual del producto: ', coste_actual)
                    print('coste acumulado: ', coste)

            if seleccion_producto in carrito:
                print('ya existe elproducto en el carrito')
                carrito[seleccion_producto]["cantidad"] += cantidad_producto
                #print('Despues - ', producto)
            else:
                carrito.update({seleccion_producto:{"cantidad": cantidad_producto, "precio": precio_producto_actual}})
                    
            # {'producto': 'Camisa', 'cantidad': 3, 'coste': 60}, {'producto': 'blusa', 'cantidad': 3, 'coste': 15}
            if existe_inventario == False:
                print("lo siento, producto no encontrado, intentalo de nuevo")        
        
        print(f"[FIN DE LA COMPRA]\n------------------------")
        print(f"Tu carrito actual es {carrito}")
        print(f"El coste total de tu compra asciende a {coste} euros")  
        return [coste,carrito]         
    
    def procesar_pago(self,coste):
        try:
            importe_pagado = float (input("El importe que has pagado es: "))
            if coste > importe_pagado:
                deficit = coste - importe_pagado
                print(f"Importe insuficiente, queda pendiente de pago {deficit}")

            else:
                cambio = importe_pagado - coste
                print(f"Pago realizado correctamente, tu cambio es {cambio} euros")

        except:
            print("Para procesar el pago es necesario que introduzcas numeros, no letras")    
    

    def agregar_clientes(self, nombre, email):
            
        patron = r"[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.\w+"
        # genero un patrón usando expresiones regulares para verificar que el mail tenga el formato correcto
        if re.match(patron,email) != None: # si comparando el patrón con el email si hay coincidencias actualizamos diccionario con el cliente nuevo y su mail
            self.clientes.update({nombre: {}}) # primero añado el diccionario nombre a self.clientes que contiene un diccionario vacio
            self.clientes[nombre].update({"e-mail":email}) # añado el par clave valor "email" : mail a ese diccionario vacio
            
        else: # si re.match(patron,email) == None es que el mail con cumple con el patrón definido y imprimimos mensaje
            print("Lo siento, el email introducido tiene un formato incorrecto")
        
        print(self.clientes)  # imprimo el diccionario self.clientes     
  
    
    def ver_clientes(self):
        for cliente,mail in self.clientes.items(): # itero el diccionario donde clave es cliente y valor mail
            print(f"NOMBRE CLIENTE => {cliente}, EMAIL => {mail}")
    

    def registrar_compra (self,nombre, carrito):
        print(' Carrito q registrar: ' , carrito)
        #Comprobar si el cliente esta en el diccionario
        if nombre in self.compras_clientes.keys():
            print('Cliente existe en nuestro registro de compras')
            for item, value in carrito:
                print('item----', item)
                if item in self.compras_clientes[nombre].keys():
                    print('Cliente ya habia comprado previamente '+ item)
                    print('cantidad anterior: '+ str(self.compras_clientes[nombre][item]['cantidad']))
                    self.compras_clientes[nombre][item]['cantidad'] += carrito[item]['cantidad']
                    print('cantidad nueva: '+ str(self.compras_clientes[nombre][item]['cantidad']))

                else:
                    print('Cliente no habia comprado el nuevo item '+ item)


            # Se añade nuevo valor en el diccionario con la clave : nombre del cliente, y valor una lista añadiendo el carrito  
        else: 
            print('Cliente no existe en nuestro registro de compras')
            self.compras_clientes.update({nombre: (carrito)})
            print(self.compras_clientes)

                    
    def ver_compras_cliente (self,nombre,historial_compra):
        cliente_existe = False
        for cliente in self.clientes.keys():   
            if nombre in cliente:
                cliente_existe = True
                print(f"Las compras realizadas por este cliente son {historial_compra}")
                 
        
        if cliente_existe == False:
            print("cliente no encontrado")

    def ver_compras_totales (self):
        beneficio_venta = 0
        print(self.clientes)
        for key,value in self.clientes.items():
            for key2, value in self.clientes[key]:
                print(value)
        print(beneficio_venta)
    
    # {'Laura Romero': {'e-mail': 'lromerovet@gmail.com', 'compra': {'camisa': {'cantidad': 2, 'precio': 20}}}, 'Elena Perez': {'e-mail': 'elena1489_68sklhj@hotmail.com'}
            

tienda = TiendaOnline()

print(' 1. Agregar productos \n')
tienda.agregar_producto('camiseta', 15, 50)
tienda.agregar_producto('pantalon', 25, 100)
print(' 2. Ver inventario: \n')
tienda.ver_inventario()

print(' 3. Buscar producto existente: \n')
tienda.buscar_producto('pantalon')
print(' 3.1. Buscar producto no existente: \n')
tienda.buscar_producto('blusa')

print('4. Actualizar stock: \n' )
tienda.ver_inventario()
tienda.actualizar_stock('pantalon', 50)
tienda.ver_inventario()

print('5. Eliminar producto: \n')
tienda.agregar_producto('calcetines', 5, 200)
tienda.buscar_producto('calcetines')
tienda.eliminar_producto('calcetines')
tienda.ver_inventario()


print('6. Calcular inventario: \n')
tienda.calcular_valor_inventario()


print('----- 7. Realizar compra numero 1: ------ \nInventario: \n')
tienda.ver_inventario()
print('-- 7.1 Empieza la compra 1: \n')
costeCompra1, carrito1 = tienda.realizar_compra()

print('----- 7. Realizar compra numero 2: ------ \nInventario: \n')
tienda.ver_inventario()
print('-- 7.1 Empieza la compra 2: \n')
costeCompra2, carrito2 = tienda.realizar_compra()


print('\n8. Procesar pago con el coste de compra numero 1 - anterior ' + str(costeCompra1) + ': ')
tienda.procesar_pago(costeCompra1)


print('9. Agregar clientes: \n')
tienda.agregar_clientes('Fatima', 'fatima@test.com')
tienda.agregar_clientes('Laura', 'laura@test.com')


print('10. Ver clientes: \n')
tienda.ver_clientes()

print('11. Registrar compra: \n')
print('Vamos a regitrar la primera y segunda compra a cliente: Fatima')
tienda.registrar_compra('Fatima', carrito1)
tienda.registrar_compra('Fatima', carrito2)

