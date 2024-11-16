from pizza_main import Pizzas,Ingredientes,cesta_cliente
from ingredientes import *
class Pizza(Pizzas):
    pass
"""PIZZAS"""
marinara = Pizza("Marinara",7,[tomate,ajo,oregano,anchoas],1)
margherita = Pizza("Margherita",7.5,[tomate,muzzarella],1)
cotto = Pizza("Cotto",8.5,[tomate,muzzarella,jamon_cocido],1)
diavola = Pizza("Diavola",8.5,[tomate,muzzarella,chorizo_picante],1)
cotto_e_funghi = Pizza("Cotto e funghi",9,[tomate,muzzarella,jamon_cocido,champiñones],1)
funghi_e_carciofi = Pizza("Funghi e carciofi",9,[tomate,muzzarella,champiñones,alcachofas],1)
siciliana = Pizza("Siciliana",9,[tomate,muzzarella,anchoas,aceitunas_negras,alcaparras,oregano],1)
pollo = Pizza("Pollo",9.5,[muzzarella,pollo_asado,patatas_al_horno,salsa_barbacoa],1)
quattro_formaggi = Pizza("Quattro formaggi",9.5,[tomate,muzzarella,emmental,grana_padano,gorgonzola],1)
speck_e_gorgonzola = Pizza("Speck e gorgonzola",9.5,[tomate,muzzarella,speck,gorgonzola],1)
speck_e_provola = Pizza("Speck e provola",9.5,[tomate,muzzarella,speck,provola],1)
tonno_e_cipolla = Pizza("Tonno e cipolla",9.5,[tomate,muzzarella,atun,cebolla],1)
vegetariana = Pizza("Vegetariana",9.5,[tomate,muzzarella,berenjena,calcabacin,pimiento],1)
amatriciana = Pizza("Amatriciana",10.5,[tomate,muzzarella,guanciale,pecorino_romano],1)
capricciosa = Pizza("Capricciosa",10.5,[tomate,muzzarella,jamon_cocido,champiñones,alcachofas,aceitunas],1)
carbonara = Pizza("Carbonara",10.5,[muzzarella,guanciale,huevo,pecorino_romano,pimienta_negra],1)
ortolana = Pizza("Ortolana",10.5,[muzzarella,berenjena,calcabacin,pimiento,patatas_al_horno,grana_padano],1)
parmigiana = Pizza("Parmigiana",10.5,[tomate,muzzarella,berenjena,grana_padano,jamon_cocido,albahaca],1)
patatosa = Pizza("Patatosa",10.5,[muzzarella,panceta,champiñones,patatas_al_horno,grana_padano],1)
rustica = Pizza("Rustica",10.5,[tomate,muzzarella,chorizo_picante,gorgonzola,cebolla_morada],1)
salame = Pizza("Salame",10.5,[muzzarella,salame,patatas_al_horno,provola,rucula],1)
zingara = Pizza("Zingara",10.5,[tomate,muzzarella,pimiento,panceta,aceitunas],1)
calabrese = Pizza("Calabrese",11,[tomate,muzzarella,berenjena,nduja,tomate_cherry_semi_seco,grana_padano],1)
cruda_e_bufala = Pizza("Cruda e bufala",11,[tomate,muzzarella_bufala,jamon_serrano],1)
fresca = Pizza("Fresca",11,[muzzarella,salmon,aguacate,cebolla_morada,lima],1)
golosa = Pizza("Golosa",11,[tomate,muzzarella,chorizo_picante,jamon_cocido,emmental],1)
paesana = Pizza("Paesana",11,[muzzarella_bufala,panceta,rucula,tomate_cherry,grana_padano],1)
pazza = Pizza("Pazza",11,[tomate,muzzarella,chorizo_picante,atun,cebolla_morada,gorgonzola],1)


