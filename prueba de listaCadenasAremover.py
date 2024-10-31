class Nodo:
    def __init__(self, valor, sig = None):
        self.valor = valor
        self.sig = sig

def pedir(mensaje):
    return (input(f"{mensaje} "))

def imprimir_lista(q):
    while q is not None:
        print(f"| {q.valor} | | ->", end=" ")
        q = q.sig
    print("None")

def crear_nodo(d):
    return Nodo(d)

def Remover_de_list_A_a (k):
     while k is not None:
      q=k
     k = [ A.a ]
     del k[ A.a ]
     q.remove[ A.a ]
     q=k.sig
     if(k.valor[0]=="A-a"):
       print("None")

def insertar_al_final():
    l = None  # Cabeza de la lista
    u = None  # Último nodo de la lista
    resp = 1

    
    while resp == 1:
        d = pedir("De el dato a insertar:")
        
        if l is None:
            # Si la lista está vacía, creamos el primer nodo
            l = crear_nodo(d)
            u = l  # El primer nodo también es el último
        else:
            # Si la lista ya tiene nodos, agregamos el nuevo nodo al final
            p = crear_nodo(d)
            u.sig = p  # El último nodo ahora apunta al nuevo nodo
            u = p  # Actualizamos el último nodo
        
        resp = pedir("Hay más datos 1 para seguir 0 para detener:")
    return l


def main():
    l = insertar_al_final()
    imprimir_lista(l)
    Remover_de_list_A_a(2)


main()
