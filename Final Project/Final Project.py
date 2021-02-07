class Company:
  def __init__(self, name, age, language,):
    self.name = name
    self.age = age
    self. language = language
  def print_name(self):
      print(self.name + " ")
  def print_age(self):
      print(self.name + " is " + self.age + " years old.")
  def print_language(self):
      print(self.name + " can speak " + self.language + ".")

class Employee(Company):
  pass

class Company_Manager(Company):
  pass

employee1 = Employee("Cristina", "25", "English and Italian")
employee1.print_language()

employee2 = Employee("Nergis", "23", "English and Turkish")
employee2.print_language()

employee3 = Employee("Ted", "27", "English and Chinese")
employee3.print_language()

employee4 = Employee("Barney", "26", "English and French")
employee4.print_language()

company_manager = Company_Manager("Robin", "29", "English and Japanese")
company_manager.print_language() 



