class TiendaOnline:
    def __init__(self,ventas_totales = 0.0): 
        self.ventas_totales = ventas_totales
        #[{'nombre': 'Camisa', 'precio': 20, 'cantidad': 40}, {'nombre': 'Pantalón', 'precio': 30, 'cantidad': 30}]
        self.inventario = [] 
    def mostrar_inventario(self):
        print('Inventario: ', self.inventario)

    def agregar_producto(self,nombre,precio,cantidad):
       
        if len(self.inventario) == 0:
            print('inventario vacio, añado un nuevo diccionario')
            self.inventario.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})

        else:
            print('inventario con datos, añado/modifico elemento en el inventario ')
            for elemento in self.inventario:
                if nombre in elemento.values():
                    print('elemento ya en inventario, modifico cantidad')
                    elemento['cantidad'] += cantidad
                else:
                    print('elemento no en inventario, añado nuevo diccionario')
                    self.inventario.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})


ropa = TiendaOnline() # creo un objeto de mi tienda online, que es de la categoria ropa
ropa.agregar_producto('Pantalon', 5, 30)
ropa.agregar_producto('Camisa', 33, 4)
ropa.agregar_producto('Camisa', 33, 4)
ropa.agregar_producto('Pantalon', 33, 4)


print(ropa.mostrar_inventario())
