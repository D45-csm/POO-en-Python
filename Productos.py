lista_productos = [] # Lista global para almacenar los usuarios creados

class Producto:
    # Crear una funcion para el CONSTRUCTOR
    def __init__(self, id_producto: int, codigo, nombre: str, precio, disponibilidad:bool, cantidad,categoria:str, marca, descripcion:str):
        self.id_producto= id_producto
        self.codigo = codigo
        self.nombre = nombre      
        self.precio= precio
        self.disponibilidad= disponibilidad
        self.cantidad=cantidad
        self.categoria=categoria
        self.marca= marca
        self.descripcion=descripcion
    # Metodos Base CRUD
    
#CREATE
    def crear_producto(self):
        lista_productos.append(self)
        print(f"✅ Éxito: El producto {self.nombre} ha sido registrado en el sistema.")
    
    #READ
    def buscar_producto(self):
        print(f"ID: {self.id_producto} producto: {self.nombre}")
        
    #UPDATE
    def actualizar_producto(self, disponibilidad: bool):
        self.disponibilidad=disponibilidad

        if self.disponibilidad==True:
            print("✅ Éxito: El producto ha sido actualizado a disponible.")
        else:
            print("✅ Éxito: El producto ha sido actualizado a no disponible.")
        
    #DELETE
    def eliminar_producto(self):
        if self in lista_productos:
            lista_productos.remove(self)
            print(f"✅ Éxito: El producto {self.nombre} ha sido eliminado del sistema.")
        else:
            print(f"⚠️ Advertencia: El producto {self.nombre} no se encuentra en el sistema.")   
    
    #add to car
    def Agregar_carrito(self):
        print("ℹ️ el producto {self.nombre} ha sido agregado exitosamente al carrito")
    #notificate low stock
    def Notificar_bajo_stock(self):
        print("producto bajo de stock⚠️")

class Televisor(Producto):
    def __init__(self, pulgadas, id_producto, codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion):
        super().__init__(id_producto, codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion)
        self.pulgadas=pulgadas

class Licuadora(Producto):
    def __init__(self, id_producto, codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion):
        super().__init__(id_producto, codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion)

class Aspiradora(Producto):
    def __init__(self, id_producto,tamaño_deposito, codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion):
        super().__init__(id_producto, codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion)
        self.tamaño_deposito=tamaño_deposito

class Microondas(Producto):
    def __init__(self, tipo, id_producto, codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion):
        super().__init__(id_producto, codigo, nombre, precio, disponibilidad, cantidad,categoria, marca, descripcion)
        self.tipo=tipo

pro=Producto(1,000, "martillo",23000, False,2, "herramienta", "hamer", "acero inoxidable" )

pro.eliminar_producto()