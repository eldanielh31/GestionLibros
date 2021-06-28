from Personas import Person
from Libros import Books

menu_string = " a) Ver lista de personas\n b) Buscar persona\n c) Ver ficha de persona\n d) Ver lista de libros\n e) Buscar libro\n f) Ver ficha de técnica de libro\n g) Prestar libro\n h) Devolver libro\n i) Ver préstamode libros"

def main():
    #print(menu_string)
    Person.full_list('estudiantes.xlsx')

    Books.full_list('libros.xlsx')

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

def option_d():
    print(Books.to_String())

def option_e(name, gender, autor):
    book = Books.get_by_name_gener_autor(name, gender, autor)

    if(book != None):
        print("Id: " + str(book[0]) + " || Nombre: " + book[1]+ " || Genero: " + book[2]+ " || Autor: " + book[3] + "\n")
    else:
        print("El libro buscado no está disponible en la base de datos. \n")

def option_f(code):
    book = Books.get_by_code(code)

    if (book != None):
        print("Id: " + str(book[0]) + " || Nombre: " + book[1] + " || Genero: " + book[2] + " || Autor: " + book[
            3] + "\n")
    else:
        print("El libro buscado no está disponible en la base de datos. \n")



if(__name__ == "__main__"):
    main()