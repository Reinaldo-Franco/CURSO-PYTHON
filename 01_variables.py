# VARIABLES
my_variable = "my string variable"
print(my_variable)

variable_string = "Reinaldo"
variable_int = 42
variable_float = 3.14
variable_bool = True

print(variable_string, variable_int, variable_float, variable_bool)
print("--------------------------")
print(variable_int)
print(type(variable_int))
int_to_string = str(variable_int)
print(int_to_string)
print(type(int_to_string))
print("--------------------------")
# CONCATENACION DE VARIABLES
print("Mi nombre es " + variable_string)
print("Mi nombre es " + variable_string + " y tengo " + str(variable_int) + "años")
# FUNCIONES O PALABRAS RESERVADAS
print("Reinaldo tiene:" + str(len(variable_string)) + " letras")
# DEFINIR VARIABLES EN UNA SOLA LINEA
name, surname, age, country = "Reinaldo", "Gomez", 42, "Argentina"
print(name, surname, age, country)
print("--------------------------")
print("Me llamo:", name, surname, ". Mi edad es:", age, "y vivo en:", country)
print("--------------------------")
# INPUT
nombre = input("ingrese su nombre:")
print("Hola", nombre)
