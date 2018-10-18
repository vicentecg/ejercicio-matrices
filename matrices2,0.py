
def menu():
    pass
    while(True):
        print("Menu:")
        print("a.- sumar matrices")
        print("b.- resta de matrices")
        print("c.- multip. matrices")
        print("d.- calcular determinante")
        print("e.- salir")
        opcion = input("ingrese opcion:")
        if(opcion == "a"):
            suma()
menu()

def suma():
    pass
    print("Matriz de 2x2")
    print("Primera matriz:")
    fila_a_col_a = float(input("fila 1 columna 1: "))
    fila_a_col_b = float(input("fila 1 columna 2: "))
    fila_b_col_a = float(input("fila 2 columna 1: "))
    fila_b_col_b = float(input("fila 2 columna 2: "))
    print("Segunda matriz:")
    fila_c_col_c = float(input("fila 1 columna 1: "))
    fila_c_col_d = float(input("fila 1 columna 2: "))
    fila_d_col_c = float(input("fila 2 columna 1: "))
    fila_d_col_d = float(input("fila 2 columna 2: "))


    resp_fila_a_col_a = fila_a_col_a + fila_c_col_c
    resp_fila_a_col_b = fila_a_col_b + fila_c_col_d
    resp_fila_b_col_a = fila_b_col_a + fila_d_col_c
    resp_fila_b_col_b = fila_b_col_b + fila_d_col_d

