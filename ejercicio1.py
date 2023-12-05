class Biblioteca:
    def __init__(self):
        self.pila_libros = []

    def prestarlibros(self, libro):
        self.pila_libros.append(libro)
        print(f"Libro '{libro}' prestado con éxito.")

    def devolverlibros(self):
        if self.pila_libros:
            libro_devuelto = self.pila_libros.pop()
            print(f"Libro '{libro_devuelto}' devuelto correctamente.")
        else:
            print("No hay libros prestados en este momento.")

    def mostrarestados(self):
        if self.pila_libros:
            print("Libros prestados actualmente:")
            for libro in reversed(self.pila_libros):
                print(f"- {libro}")
        else:
            print("No hay libros prestados en este momento.")

biblioteca = Biblioteca()

biblioteca.prestarlibros("Cien años de soledad")
biblioteca.mostrarestados()
biblioteca.prestarlibros("Don Quijote de la Mancha")
biblioteca.mostrarestados()
biblioteca.devolverlibros()
biblioteca.mostrarestados()