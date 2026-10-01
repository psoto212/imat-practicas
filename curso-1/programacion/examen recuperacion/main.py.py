class Producto:
    def init(self, cod_producto:int, nombre_producto:str,unidades:int,precio_compra:float,precio_venta:float): 
        self.cod_producto = cod_producto
        self.nombre_producto = nombre_producto
        self.unidades = unidades
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.salir = self.salir_programa()
        
    def fichero(fichero = 'productos.txt'):
        with open(fichero,'r', encoding = "UTF-8") as file:
            for i in file:
                lista_productos = file.readline().replace('\n','')
                lista_productos = list(lista_productos.split(';'))
                dict_product = {lista_productos[1] ,lista_productos[3]}
                
                print(lista_productos)  

    def errores(producto, lista_productos):
        erorres = 0
        lista_error = []
        for k in lista_productos:
            if len(producto) != len(lista_productos[k]):
                errores +=1
                if producto[2].isalpha() or producto[3].isalpha() or producto[4].isalpha():
                    erorres += 1
        return erorres
    
    
    def codigo_novalido(exception, lista_productos):
        codigo = False
        if codigo != lista_productos[0]:
            return codigo



    def elegir_producto(cod_producto, lista_productos, codigo_novalido):
        try: #utilizamos la excepcion para ver si el producto solicitado esta en nuestro fichero
            if cod_producto == lista_productos[0]: #si lo está lo asociamos a la columna primera del fichero que son los codigos de cada producto y a partir de eso sacamos toda la linea del mismo producto
                for t in range(1,len(lista_productos[0])):
                    for j in range(len(lista_productos)):
                        producto = lista_productos[t][j]
            return producto
        except codigo_novalido() as e: # si el producto no esta a partir de la funcion excepcion creada anteriormente de codigo no valido le decimos al usuario que su codigo no es valido y que intente otro
            print(int("codigo no valido introduzca otro codigo")) #no está acabado no me acuerdo de la funcion para que una excepcion no cerrase el bucle definitivamente
    


    def unidades_pedidas(cod_producto,unidades, elegir_producto, lista_productos):
        while elegir_producto():
            for unidades in lista_productos[2]:
                unidades_totales = lista_productos[2] - unidades
                if unidades_totales < 0:
                    print(f"no tenemos {unidades} unidades pero le daremos {lista_productos[2]} y pediremos{-unidades_totales} ")
                    with open('pedidos.txt','w', encoding = "UTF-8") as pedidos:
                        pedidos.writeline("codigo : unidades a pedir")
                        pedidos.write(f"{cod_producto} : {unidades_totales}")
        

    def salir_programa():
        n = 0
        resto = 0
        mas_productos = input("¿desea comprar otro producto?")
        mas_productos.lower()
        for j in range(len(mas_productos)):
            if mas_productos[j] == 'n':
                n += 1
            else:
                resto +=1
            if n>resto:
                print("muchas gracias por su compra")
            else:
                with open('productos.txt','r') as file:
                    print(file.readlines())
    


def __main__(nombre_producto):
    print(f"errores encontrados {errores()}")
    print("-----------------------------")
    print("Productos")
    print("-----------------------------")
    





        

            
                