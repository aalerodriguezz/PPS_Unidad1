class UI:
    def __init__(self):
        self.nombre_autor = "Alejandro Rodriguez"

    def cabecera(self, titulo):
        """Imprime el título de la tarea y el autor"""
        print("\n" + "=" * 40)
        print(f" {titulo}")
        print(f" Realizado por: {self.nombre_autor}")
        print("=" * 40 + "\n")

    def mensaje_exito(self, texto):
        print(f" -> [OK] {texto}")

    def mensaje_error(self, texto):
        print(f" -> [ERROR] {texto}")