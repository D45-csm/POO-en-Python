lista_productos = [] # Lista global para almacenar los usuarios creados
def guardar_datos(objeto):
    lista_productos.append(vars(objeto))
    print("🟢Guardado correctamente")

class Producto:
    # Crear una funcion para el CONSTRUCTOR
    def __init__(self,codigo, nombre: str, precio, disponibilidad:bool, cantidad,categoria:str, marca, descripcion:str):
        self.__codigo = codigo
        self.nombre = nombre   
        self.precio= precio #(publico)
        self._disponibilidad= disponibilidad #(protegido)
        self.__cantidad=cantidad #(privado)
        self.categoria=categoria
        self.marca= marca
        self.descripcion=descripcion

    # get y set para cada atributo---
    # Para codigo 
    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    # Para nombre 
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    # Para precio 
    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    # Para disponibilidad 
    def get_disponibilidad(self):
        return self.disponibilidad

    def set_disponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad

    # Para cantidad 
    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    # Para categoria 
    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

    # Para marca 
    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    # Para descripcion 
    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    # Metodos Base CRUD
    #CREATE
    def __crear_producto(self):
        lista_productos.append(self)
        print(f"✅ Éxito: El producto {self.nombre} ha sido registrado en el sistema.")
    
    #READ
    def buscar_producto(self):
        print(f"Codigo: {self.__codigo} producto: {self.nombre} precio: {self.precio} descripcion: {self.descripcion}")
        
    #UPDATE
    def __actualizar_producto(self, disponibilidad: bool):
        self.disponibilidad=disponibilidad

        if self.disponibilidad:
            print("✅ Éxito: El producto ha sido actualizado a disponible.")
        else:
            print("✅ Éxito: El producto ha sido actualizado a no disponible.")
        
    #DELETE
    def __eliminar_producto(self):
        if self in lista_productos:
            lista_productos.remove(self)
            print(f"✅ Éxito: El producto {self.nombre} ha sido eliminado del sistema.")
        else:
            print(f"⚠️ Advertencia: El producto {self.nombre} no se encuentra en el sistema.")  

    #add to car
    def Agregar_carrito(self):
        print("ℹ️ el producto {self.nombre} ha sido agregado exitosamente al carrito")
    #notificate low stock
    def __Notificar_bajo_stock(self):
        print("producto bajo de stock⚠️")

    #Funciones puente para acceder a los metodos privados y protegidos---
    def ejecutar_crear(self):
        self.__crear_producto()

    def ejecutar_actualizar(self, disponibilidad: bool):
        self.__actualizar_producto(disponibilidad)

    def ejecutar_eliminar(self):
        self.__eliminar_producto()

    def enviar_notificacion_stock(self):
        self.__Notificar_bajo_stock()


class Televisor(Producto):
    def __init__(self, pulgadas, codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion):
        super().__init__( codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion)
        self.pulgadas=pulgadas

class Licuadora(Producto):
    def __init__(self, codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion):
        super().__init__(codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion)

class Aspiradora(Producto):
    def __init__(self,tamaño_deposito, codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion):
        super().__init__(codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion)
        self.tamaño_deposito=tamaño_deposito

class Microondas(Producto):
    def __init__(self, tipo, codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion):
        super().__init__(codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion)
        self.tipo=tipo  

instancia_producto=Producto("0001", "martillo",23000, False,2, "herramienta", "hamer", "acero inoxidable" )
#nombre del objeto= clase(valores)


Producto1=Aspiradora("15 litros","003", "Trineo",500000, True,30, "Limpieza", "Koblenz", "2 metros de largo, 1,4 Metros de hancho")
Producto2=Aspiradora("14 litros","007", "Escoba",360000, False,23, "Limpieza", "Koblenz", "1,5 metros de largo, 0.6 Metros de hancho")

Producto1.buscar_producto()
Producto2.buscar_producto()