import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Gestor de Biblioteca V3 implementando Grafos, Nodos y Árboles

#  CLASE LIBRO
class Libro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo.lower()
        self.autor = autor
        self.disponible = True
        self.espera = deque()

        # MP - Mantenimiento Preventivo:
        # Se normaliza título a minúsculas para evitar errores en búsquedas futuras.
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.isbn} - {self.titulo.capitalize()} - ({self.autor}) ({estado})"



#  CLASE USUARIO
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

        # ME - Evolutivo (HU05):
        # En una próxima versión se podría integrar historial de préstamos.
    def __str__(self):
        return self.nombre

#  NODOS Y ÁRBOLES DE LIBROS
class NodoLibro:
    def __init__(self, libro):
        self.libro = libro
        self.izquierda = None
        self.derecha = None

class ArbolLibros:
    def __init__(self):
        self.raiz = None

    def insertar(self, libro):
        # ME - Evolutivo:
        # ÁRBOL BINARIO permite ordenar libros por título.
        self.raiz = self._insertar_rec(self.raiz, libro)

    def _insertar_rec(self, nodo, libro):
        if nodo is None:
            return NodoLibro(libro)
        if libro.titulo < nodo.libro.titulo:
            nodo.izquierda = self._insertar_rec(nodo.izquierda, libro)
        else:
            nodo.derecha = self._insertar_rec(nodo.derecha, libro)
        return nodo

    def buscar(self, titulo):
        # ME - Evolutivo (HU01): búsqueda por título.
        return self._buscar_rec(self.raiz, titulo.lower())

    def _buscar_rec(self, nodo, titulo):
        if nodo is None:
            return None
        if titulo == nodo.libro.titulo:
            return nodo.libro
        elif titulo < nodo.libro.titulo:
            return self._buscar_rec(nodo.izquierda, titulo)
        else:
            return self._buscar_rec(nodo.derecha, titulo)

    def mostrar_inorden(self):
        # ME - Evolutivo (HU03): mostrar libros disponibles.
        self._inorden_rec(self.raiz)

    def _inorden_rec(self, nodo):
        if nodo:
            self._inorden_rec(nodo.izquierda)
            print(nodo.libro)
            self._inorden_rec(nodo.derecha)

#  NODOS Y ÁRBOLES DE USUARIOS
class NodoUsuario:
    def __init__(self, usuario):
        self.usuario = usuario
        self.izquierda = None
        self.derecha = None

class ArbolUsuarios:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre):
        # ME - Evolutivo (HU02): registrar usuarios.
        usuario = Usuario(nombre)
        self.raiz = self._insertar_rec(self.raiz, usuario)

    def _insertar_rec(self, nodo, usuario):
        if nodo is None:
            return NodoUsuario(usuario)
        if usuario.nombre.lower() < nodo.usuario.nombre.lower():
            nodo.izquierda = self._insertar_rec(nodo.izquierda, usuario)
        else:
            nodo.derecha = self._insertar_rec(nodo.derecha, usuario)
        return nodo

    def buscar(self, nombre):
        # MC - Correctivo:
        # Se agregó .lower() para evitar errores con mayúsculas.
        return self._buscar_rec(self.raiz, nombre.lower())

    def _buscar_rec(self, nodo, nombre):
        if nodo is None:
            return None
        if nombre == nodo.usuario.nombre.lower():
            return nodo.usuario
        elif nombre < nodo.usuario.nombre.lower():
            return self._buscar_rec(nodo.izquierda, nombre)
        else:
            return self._buscar_rec(nodo.derecha, nombre)

    def mostrar_usuarios(self):
        print("\nUsuarios registrados:")
        self._mostrar_rec(self.raiz)

    def _mostrar_rec(self, nodo):
        if nodo:
            self._mostrar_rec(nodo.izquierda)
            print(nodo.usuario)
            self._mostrar_rec(nodo.derecha)

#  BIBLIOTECA
class Biblioteca:
    def __init__(self):
        self.devoluciones_recientes = []

    def agregar_devolucion(self, libro):
        # ME - Evolutivo:
        # Nuevas funcionalidades de devolución.
        self.devoluciones_recientes.append(libro)

    def mostrar_devoluciones(self):
        if not self.devoluciones_recientes:
            print("No hay devoluciones recientes.\n")
        else:
            print("Devoluciones recientes:")
            for libro in self.devoluciones_recientes:
                print(libro)

    def agregar_a_espera(self, libro, usuario):
        # ME - Evolutivo (HU04): lista de espera.
        libro.espera.append(usuario)
        print(f"Usuario '{usuario.nombre}' agregado a la lista de espera para el libro '{libro.titulo.capitalize()}'.\n")

    def mostrar_espera(self, libro):
        # ME - Evolutivo (HU05)
        if not libro.espera:
            print(f"No hay usuarios en espera para el libro '{libro.titulo.capitalize()}'.\n")
        else:
            print(f"Usuarios en espera para el libro '{libro.titulo.capitalize()}':")
            for usuario in libro.espera:
                print(usuario)

#  FUNCIONES
def agregar_libro(arbol_libros):
    isbn = input("Ingrese el ID del libro: ")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el nombre del autor: ")

    # MP - Preventivo:
    # Validación mínima para evitar registros defectuosos.
    if not isbn or not titulo:
        print("Datos insuficientes. No se agregó el libro.\n")
        return

    libro = Libro(isbn, titulo, autor)
    arbol_libros.insertar(libro)
    print(f"El Libro '{titulo}' se ha agregado correctamente.\n")

def agregar_usuario(arbol_usuarios):
    nombre = input("Ingrese el nombre del usuario: ")

    # MP - Preventivo:
    if not nombre:
        print("Nombre inválido.\n")
        return

    arbol_usuarios.insertar(nombre)
    print(f"Usuario '{nombre}' registrado con éxito.\n")

def prestar_libro(arbol_libros, arbol_usuarios, biblioteca):
    nombre = input("Ingrese el nombre del usuario: ")
    usuario = arbol_usuarios.buscar(nombre)

    if usuario is None:
        print("Usuario no encontrado.\n")
        return

    titulo = input("Ingrese el título del libro a prestar: ").lower()
    libro = arbol_libros.buscar(titulo)

    if libro:
        if libro.disponible:
            libro.disponible = False
            print(f"El libro '{libro.titulo.capitalize()}' ha sido prestado a {usuario.nombre}.\n")
        else:
            # ME - Evolutivo (HU04): sistema de espera
            print(f"El libro '{libro.titulo.capitalize()}' está prestado. Se agregará a la lista de espera.\n")
            biblioteca.agregar_a_espera(libro, usuario)
    else:
        print("Libro no encontrado.\n")

def devolver_libro(arbol_libros, arbol_usuarios, biblioteca):
    nombre = input("Ingrese el nombre del usuario: ")
    usuario = arbol_usuarios.buscar(nombre)

    if usuario is None:
        print("Usuario no encontrado.\n")
        return

    titulo = input("Ingrese el título del libro a devolver: ").lower()
    libro = arbol_libros.buscar(titulo)

    if libro:
        if not libro.disponible:
            libro.disponible = True
            print(f"El libro '{libro.titulo.capitalize()}' se ha devuelto.\n")
            biblioteca.agregar_devolucion(libro)

            # ME - Evolutivo (HU04):
            # entrega automática al siguiente en espera
            if libro.espera:
                siguiente_usuario = libro.espera.popleft()
                libro.disponible = False
                print(f"El libro '{libro.titulo.capitalize()}' ha sido prestado a {siguiente_usuario.nombre} desde la lista de espera.\n")
        else:
            print(f"El libro '{libro.titulo.capitalize()}' ya estaba disponible.\n")
    else:
        print("Libro no encontrado.\n")

def mostrar_espera(arbol_libros, biblioteca):
    titulo = input("Ingrese el título del libro: ").lower()
    libro = arbol_libros.buscar(titulo)

    if libro:
        biblioteca.mostrar_espera(libro)
    else:
        print("Libro no encontrado.\n")

#  GRAFO DE USUARIOS
class GrafoUsuarios:
    def __init__(self):
        self.G = nx.Graph()

    def agregar_usuario(self, nombre):
        # ME - Evolutivo:
        self.G.add_node(nombre)

    def agregar_relacion(self, usuario1, usuario2):
        # MC - Correctivo:
        # Se añade manejo de errores en caso de usuarios no existentes.
        if usuario1 in self.G and usuario2 in self.G:
            self.G.add_edge(usuario1, usuario2)
        else:
            print("Uno o ambos usuarios no existen en el grafo.")

    def mostrar_grafo(self):
        # MA - Adaptativo:
        # Se ajusta al entorno gráfico mediante networkx.
        pos = nx.spring_layout(self.G)
        nx.draw_networkx_nodes(self.G, pos, node_color='lightgreen', node_size=800)
        nx.draw_networkx_edges(self.G, pos)
        nx.draw_networkx_labels(self.G, pos, font_weight='bold')
        plt.title('Relaciones entre Usuarios')
        plt.axis('off')
        plt.show()

    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(inicio)
        print(inicio, end=' ')
        for vecino in self.G[inicio]:
            if vecino not in visitados:
                self.dfs(vecino, visitados)

    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        while cola:
            nodo = cola.popleft()
            if nodo not in visitados:
                print(nodo, end=' ')
                visitados.add(nodo)
                cola.extend([vecino for vecino in self.G[nodo] if vecino not in visitados])

#  SISTEMA BIBLIOTECA - MENÚ
def sistema_biblioteca_unificado():
    arbol_libros = ArbolLibros()
    arbol_usuarios = ArbolUsuarios()
    biblioteca = Biblioteca()
    grafo_usuarios = GrafoUsuarios()

    # MP - Preventivo: Datos precargados para pruebas controladas.
    arbol_libros.insertar(Libro("123", "Cien años de soledad", "Gabriel García Márquez"))
    arbol_libros.insertar(Libro("456", "Satanás", "Mario Mendoza"))
    arbol_libros.insertar(Libro("789", "El principito", "Antoine de Saint-Exupéry"))
    arbol_libros.insertar(Libro("987", "El Coronel no tiene quien le escriba", "Gabriel García Márquez"))

    # Usuarios pre-cargados
    usuarios_pre = ["Eduardo", "Alejandro", "Andres", "Esneider"]
    for nombre in usuarios_pre:
        arbol_usuarios.insertar(nombre)
        grafo_usuarios.agregar_usuario(nombre)

    # Interfaz principal
    while True:
        print("\nOpciones:")
        print("1. Agregar un Libro")
        print("2. Agregar un Usuari@")
        print("3. Ver Libros disponibles")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Ver Libros devueltos recientemente")
        print("7. Ver lista de espera de un libro")
        print("8. Ver usuari@s registrad@s")
        print("9. Mostrar grafo de relaciones entre usuarios")
        print("10. Agregar relación entre usuarios")
        print("11. Recorrido DFS en grafo de usuarios")
        print("12. Recorrido BFS en grafo de usuarios")
        print("13. Salir del sistema")

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            agregar_libro(arbol_libros)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del usuario: ")
            arbol_usuarios.insertar(nombre)
            grafo_usuarios.agregar_usuario(nombre)
            print(f"Usuario '{nombre}' registrado con éxito.\n")
        elif opcion == "3":
            print("\nListado de libros:")
            arbol_libros.mostrar_inorden()
        elif opcion == "4":
            prestar_libro(arbol_libros, arbol_usuarios, biblioteca)
        elif opcion == "5":
            devolver_libro(arbol_libros, arbol_usuarios, biblioteca)
        elif opcion == "6":
            biblioteca.mostrar_devoluciones()
        elif opcion == "7":
            mostrar_espera(arbol_libros, biblioteca)
        elif opcion == "8":
            arbol_usuarios.mostrar_usuarios()
        elif opcion == "9":
            grafo_usuarios.mostrar_grafo()
        elif opcion == "10":
            u1 = input("Nombre del primer usuario: ")
            u2 = input("Nombre del segundo usuario: ")
            grafo_usuarios.agregar_relacion(u1, u2)
        elif opcion == "11":
            inicio = input("Ingrese usuario de inicio para DFS: ")
            if inicio in grafo_usuarios.G:
                print("Recorrido DFS:")
                grafo_usuarios.dfs(inicio)
                print()
            else:
                print("Usuario no encontrado en el grafo.")
        elif opcion == "12":
            inicio = input("Ingrese usuario de inicio para BFS: ")
            if inicio in grafo_usuarios.G:
                print("Recorrido BFS:")
                grafo_usuarios.bfs(inicio)
                print()
            else:
                print("Usuario no encontrado en el grafo.")
        elif opcion == "13":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

        repetir = input("¿Desea realizar otra operación? (S/N): ").strip().lower()
        if repetir != 's':
            print("Saliendo del sistema...")
            break

#  EJECUCIÓN
if __name__ == "__main__":
    sistema_biblioteca_unificado()
