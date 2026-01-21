import time

class Dragon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.etapas = ["Huevo", "Bebé", "Joven", "Guardián", "Sabio"]
        self.etapa_actual = 0
        
        # Habilidades (0 a 100)
        self.habilidades = {
            "Fuego del Lenguaje": 0,    # Francés
            "Sabiduría Antigua": 0,     # General
            "Corazón del Dragón": 0,    # Emocional (Journal)
            "Disciplina": 0             # Constancia
        }

    def verificar_evolucion(self):
        promedio = sum(self.habilidades.values()) / len(self.habilidades)
        if promedio > (self.etapa_actual + 1) * 20 and self.etapa_actual < 4:
            self.etapa_actual += 1
            print(f"¡INCREÍBLE! Tu dragón ha evolucionado a: {self.etapas[self.etapa_actual]}")

    def mostrar_stats(self):
        print(f"\n--- ESTADO DE {self.nombre.upper()} ---")
        print(f"Etapa: {self.etapas[self.etapa_actual]}")
        for hab, val in self.habilidades.items():
            print(f"{hab}: {'🔥' * (val // 10)} ({val}/100)")

class AppEducativa:
    def __init__(self, usuario, dragon):
        self.usuario = usuario
        self.dragon = dragon

    def realizar_journal(self):
        print("\n--- EL LIBRO DEL DRAGÓN ---")
        input("¿Cómo te has sentido hoy aprendiendo? ")
        input("Escribe una frase en francés sobre ti: ")
        print("Tu dragón siente tu honestidad. +10 en Corazón del Dragón.")
        self.dragon.habilidades["Corazón del Dragón"] += 10
        self.dragon.verificar_evolucion()

    def mision_frances(self, aciertos):
        puntos = aciertos * 5
        print(f"\nMisión cumplida. Has ganado {puntos} puntos de Fuego del Lenguaje.")
        self.dragon.habilidades["Fuego del Lenguaje"] += puntos
        self.dragon.verificar_evolucion()

# --- SIMULACIÓN DE USO ---
mi_dragon = Dragon("Ignis")
app = AppEducativa("Estudiante 1", mi_dragon)

print("Bienvenido a tu Reino Medieval.")
app.realizar_journal()
app.mision_frances(4) # El usuario acierta 4 ejercicios
mi_dragon.mostrar_stats()
