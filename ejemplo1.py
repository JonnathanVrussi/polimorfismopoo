#Creaciòn de la superclase "Animal
class Animal:
  # Definir el mètodo "sonido"
  def sonido(self):
    pass

# Creaciòn de la subclase 1 , junto con su mètodo y atributo 
class Perro(Animal):
  # Se asigna el mismo mètodo de la superclase "Animal"
  def sonido(self):
    return "Guau"

# Creaciòn de la subclase 2 , junto con su mètodo y atributo 
class Gato(Animal):
  # Se asigna el mismo mètodo de la superclase "Animal"
  def sonido(self):
    return "Miau"

# Creaciòn de la funciòn " Hacer sonido " 
hacer_sonido(animal:Animal):
   print(animal.sonido())

#Creacion de los objetos 
perro=Perro()
gato=Gato()

# Salida de los objetos 
hacer_sonido(perro)
hacer_sonido(gato)
