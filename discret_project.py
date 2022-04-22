def lineaSup(largo):
    linea = "   ╔"
    for i in range(1, largo-1):
        linea += "═"
    linea += "╗"
    print(linea)


def lineaMed(largo):
    linea = "   ╠"
    for i in range(1, largo-1):
        linea += "═"
    linea += "╣"
    print(linea)


def lineaInf(largo):
    linea = "   ╚"
    for i in range(1, largo-1):
        linea += "═"
    linea += "╝" + "\n"
    print(linea)


def lineaBlanco(largo):
    linea = "   ║"
    for i in range(1, largo-1):
        linea += " "
    linea += "║"
    print(linea)


def lineaDato(d, largo):
    linea = ""
    linea += "   ║ "
    linea += d
    blancos = largo - len(d)
    for i in range(1, blancos-2):
        linea += " "
    linea += "║"
    print(linea)


def menuPrincipal():
    lineaSup(60)
    lineaBlanco(60)
    lineaDato("                 Operaciones con Conjuntos", 60)
    lineaBlanco(60)
    lineaMed(60)
    lineaBlanco(60)
    lineaDato("01. Operar dos Conjuntos", 60)
    lineaDato("02. Operar tres Conjuntos", 60)
    lineaDato("03. Salir", 60)
    lineaBlanco(60)
    lineaInf(60)


while True:
    menuPrincipal()
    while True:
        try:
            opc = int(input("Opción -> "))
            break
        except ValueError:
            print("Valor incorrecto!")
    print()

    if opc == 1:
        A = set()
        B = set()
        print("\t\t.:Introduce los datos solicitados:.")
        print()
        while True:
            try:
                cant_A = int(input("Cantidad de datos del conjunto A: "))
                break
            except ValueError:
                print("Valor incorrecto!")
        print()
        print("Digite los datos numéricos enteros")
        print()
        for a in range(cant_A):
            while True:
                try:
                    dato = int(input("-> "))
                    A.add(dato)
                    break
                except ValueError:
                    print("Valor incorrecto!")
        print()
        while True:
            try:
                cant_B = int(input("Cantidad de datos del conjunto B: "))
                break
            except ValueError:
                print("Valor incorrecto!")
        print()
        print("Digite los datos")
        print()
        for b in range(cant_B):
            while True:
                try:
                    dato = int(input("-> "))
                    B.add(dato)
                    break
                except ValueError:
                    print("Valor incorrecto!")
        print()

        union = A.union(B)
        interseccion = A.intersection(B)
        dif_A_B = A.difference(B)
        dif_B_A = B.difference(A)
        dif_simetrica = A.symmetric_difference(B)
        sub_A = A.issubset(B)
        sub_B = B.issubset(A)

        print("\t\t.:Resultados:.")
        print(f"""\nConjunto A: {A}
Conjunto B: {B}
\nUnión: {union}
Intersección: {interseccion}
Diferencia A - B: {dif_A_B}
Diferencia B - A: {dif_B_A}
Diferencia simétrica: {dif_simetrica}
A es subconjunto B: {sub_A}
B es subconjunto A: {sub_B}
""")

    if opc == 2:
        A = set()
        B = set()
        C = set()
        print("\t\t.:Introduce los datos solicitados:.")
        print()
        while True:
            try:
                cant_A = int(input("Cantidad de datos del conjunto A: "))
                break
            except ValueError:
                print("Valor incorrecto!")
        print("Digite los datos")
        print()
        for a in range(cant_A):
            while True:
                try:
                    dato = int(input("-> "))
                    A.add(dato)
                    break
                except ValueError:
                    print("Valor incorrecto!")
        print()
        while True:
            try:
                cant_B = int(input("Cantidad de datos del conjunto B: "))
                break
            except ValueError:
                print("Valor incorrecto!")
        print("Digite los datos")
        print()
        for b in range(cant_B):
            while True:
                try:
                    dato = int(input("-> "))
                    B.add(dato)
                    break
                except ValueError:
                    print("Valor incorrecto!")
        print()

        while True:
            try:
                cant_C = int(input("Cantidad de datos del conjunto C: "))
                break
            except ValueError:
                print("Valor incorrecto!")
        print("Digite los datos")
        print()
        for c in range(cant_C):
            while True:
                try:
                    dato = int(input("-> "))
                    C.add(dato)
                    break
                except ValueError:
                    print("Valor incorrecto!")
        print()
        union = A.union(B, C)
        interseccion = A.intersection(B, C)
        dif_A_B = A.difference(B)
        dif_A_C = A.difference(C)
        dif_B_A = B.difference(A)
        dif_B_C = B.difference(C)
        dif_C_A = C.difference(A)
        dif_C_B = C.difference(B)
        dif_simetrica_A_B = A.symmetric_difference(B)
        dif_simetrica_A_C = A.symmetric_difference(C)
        dif_simetrica_B_C = B.symmetric_difference(C)
        dif_simetrica_all = A ^ B ^ C
        sub_A_B = A.issubset(B)
        sub_A_C = A.issubset(C)
        sub_B_A = B.issubset(A)
        sub_B_C = B.issubset(C)
        sub_C_A = C.issubset(A)
        sub_C_B = C.issubset(B)
        print("\t\t.:Resultados:.")
        print(f"""\nConjunto A: {A}
Conjunto B: {B}
Conjunto C: {C}
\nUnión: {union}
Intersección: {interseccion}
Diferencia A - B: {dif_A_B}
Diferencia A - C: {dif_A_C}
Diferencia B - A: {dif_B_A}
Diferencia B - C: {dif_B_C}
Diferencia C - A: {dif_C_A}
Diferencia C - B: {dif_C_B}
Diferencia simétrica A y B: {dif_simetrica_A_B}
Diferencia simétrica A y C: {dif_simetrica_A_C}
Diferencia simétrica B y C: {dif_simetrica_B_C}
Diferencia simétrica A, B y C: {dif_simetrica_all}
A es subconjunto B: {sub_A_B}
A es subconjunto de C: {sub_A_C}
B es subconjunto A: {sub_B_A}
B es subconjunto de C: {sub_B_C}
C es subconjunto de A: {sub_C_A}
C es subconjunto de B: {sub_C_B}
""")
    if opc == 3:
        print("\t.:Gracias por utilizar el programa!:.")
        break
