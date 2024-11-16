from pizza_main import Pizzas
from ingredientes import pollo_asado,provola,espinacas,rodajas_tomate,mayonesa,muzzarella_bufala,jamon_cocido,salsa_trufa
class Ripiena(Pizzas):
    pass
"""RIPIENA"""
ripiena_di_pollo = Ripiena("Ripiena di pollo",7.5,[pollo_asado,provola,espinacas,rodajas_tomate,mayonesa],2)
ripiena_tartufata = Ripiena("Ripiena tartufata",7.5,[muzzarella_bufala,jamon_cocido,salsa_trufa],2)

