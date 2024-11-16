import re
"""INVENTARIO"""
cesta_cliente=[]
pedido = 1
"""HORNOS"""
horno_danielle = []
horno_walter = []
"""CLASE MADRE PIZZA"""
class Pizzas(): 
    def __init__(self,nombre,precio,ingredientes,tamaño):
        self.nombre = nombre
        self.precio = precio
        self.ingredientes = [ingredientes]
        self.tamaño = tamaño
    def añadir_quitar_ingredientes(self,ingrediente1,ingrediente2,cantidad):
        descartes= {}
        extras={}
        if isinstance(ingrediente1, list):
            for ingrediente in ingrediente1:
                descartes.update({ingrediente.nombre: ingrediente.precio})
        else:
            descartes.update({ingrediente1.nombre:ingrediente1.precio})
        if isinstance(ingrediente2,list):
            for ingrediente in ingrediente2:
                extras.update({ingrediente.nombre: ingrediente.precio})
            suma = sum(extras.values())
            precio_final = (self.precio + suma) * cantidad
            cesta_cliente.append(f"{cantidad} {self.nombre}: Sin{list(descartes.keys())} Extra>>> {list(extras.keys())} €{precio_final}")   
        else:
            extras.update({ingrediente2.nombre:ingrediente2.precio})
            suma = sum(extras.values())
            precio_final = (self.precio + suma) * cantidad
            cesta_cliente.append(f"{cantidad} {self.nombre}: Sin{list(descartes.keys())} Extra>>> {list(extras.keys())} €{precio_final}")
    def quitar_ingrediente(self,ingrediente,cantidad):
        descartes = {}
        if isinstance(ingrediente, list):
            for ingrediente in ingrediente:
                descartes.update({ingrediente.nombre: ingrediente.precio})
            cesta_cliente.append(f"{cantidad} {self.nombre}: Sin>>> {list(descartes.keys())} €{self.precio*cantidad}")
        else:
            descartes.update({ingrediente.nombre:ingrediente.precio})
            cesta_cliente.append(f"{cantidad} {self.nombre}: Sin>>>{list(descartes.keys())} €{self.precio*cantidad}")
    def añadir_ingrediente(self,ingrediente,cantidad):
        extras = {}
        if isinstance(ingrediente, list):
            for ingrediente in ingrediente:
                extras.update({ingrediente.nombre: ingrediente.precio})
            suma = sum(extras.values())
            precio_final = (self.precio + suma) * cantidad
            item = (f"{cantidad} {self.nombre}: Extra>>> {list(extras.keys())} €{precio_final}",)
        else:
            extras.update({ingrediente.nombre:ingrediente.precio})
            suma = sum(extras.values())
            precio_final = (self.precio + suma) * cantidad
            cesta_cliente.append(f"{cantidad} {self.nombre}: Extra>>> {list(extras.keys())} €{precio_final}")
    def añadir_cesta(self,cantidad):
        precio_final= self.precio * cantidad
        cesta_cliente.append(f"{cantidad} {self.nombre} €{precio_final}")
    def eliminar_cesta(self):
        for item in cesta_cliente:
            if self.nombre in item:
                cesta_cliente.remove(item)
                print(f"Se eliminó: {item}")
                break
"""CLASE MADRE BEBIDA"""
class Bebidas():
    def __init__ (self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    def añadir_cesta(self,cantidad):
        precio_final= self.precio * cantidad
        cesta_cliente.append(f"{cantidad} {self.nombre} €{precio_final}")
    def eliminar_cesta(self):
        for item in cesta_cliente:
            if self.nombre in item:
                cesta_cliente.remove(item)
                print(f"Se eliminó: {item}")
"""CLASE MADRE INGREDIENTES"""
class Ingredientes():
    def __init__ (self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
"""FUNCION COBRAR"""
def cobrar():
    total = 0  
    for item in cesta_cliente:
        match = re.search(r"€([0-9]*\.?[0-9]+)", item)
        if match:
            precio = float(match.group(1)) 
            total += precio
    print(f"Total a pagar: €{total}")
    



