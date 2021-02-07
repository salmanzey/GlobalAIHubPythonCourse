class Animals:
  def __init__(self, name, age, species):
    self.name = name
    self.age = age
    self.species = species
  def print_name(self):
    print(self.name + " ")
  def print_age(self):
    print(self.name + " is " + self.age + " years old.")
  def print_species(self):
    print(self.name + " is a " + self.species + ".")  

class Dogs(Animals):
  def __init__(self, name, age, species, colour, likes):
    super().__init__(name, age, species)
    self.colour = colour
    self.likes = likes
  def print_colour(self):
    print(self.name + "'s colour is " + self.colour + " colour.")
  def print_likes(self):
    print(self.name + " likes to " + self.likes +".")  

class Cats(Animals):
  def __init__(self, name, age, species, colour, likes):
    super().__init__(name, age, species)
    self.colour = colour
    self.likes = likes
  def print_colour(self):
    print(self.name + "'s colour is " + self.colour + " colour.")
  def print_likes(self):
    print(self.name + " likes to " + self.likes +".")  

dog = Dogs("Duman", "3", "dog", "black", "playing")   
cat = Cats("Lila", "2", "cat", "white", "sleep")

dog.print_name()
dog.print_age()
dog.print_species()
dog.print_colour()
dog.print_likes()

cat.print_name()
cat.print_age()
cat.print_species()
cat.print_colour()
cat.print_likes()
