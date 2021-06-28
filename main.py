from Personas import Person
from Libros import Books

menu_string = " a) Ver lista de personas\n b) Buscar persona\n c) Ver ficha de persona\n d) Ver lista de libros\n e) Buscar libro\n f) Ver ficha de técnica de libro\n g) Prestar libro\n h) Devolver libro\n i) Ver préstamode libros"

def main():
    #print(menu_string)
    Person.full_list('estudiantes.xlsx')
    print(Person.All_Person)

    Books.full_list('libros.xlsx')
    print(Books.All_Books)

def option_a():
    print(Person.to_String())

def option_b(name):
    person = Person.get_by_name(name)
    if(person != None):
        print("Codigo: " + str(person[0]) + " || Nombre: " + person[1] + " || Correo: " + person[2] + "\n")
    else:
        print("La persona no se encuentra en la base de datos.")

def option_c(code):
    person = Person.get_by_code(code)
    if(person != None):
        print("Codigo: " + str(person[0]) + " || Nombre: " + person[1] + " || Correo: " + person[2] + "\n")
    else:
        print("La persona no se encuentra en la base de datos.")


if(__name__ == "__main__"):
    main()