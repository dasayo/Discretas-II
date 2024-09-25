import random

class MultiplicationHashTable:
    def __init__(self, size, A=None):
        self.size = size
        self.A = A if A else random.uniform(0, 1)  # Elegir A entre 0 y 1 si no se proporciona
        self.table = [None] * size  # Inicializa la tabla hash

    def hash_function(self, key):
        """Método de la multiplicación: (k * A) mod 1 * m"""
        fractional_part = (key * self.A) % 1  # Extrae la parte fraccionaria (decimales)
        return int(fractional_part * self.size)  # Multiplica por el tamaño de la tabla y toma el entero

    def insert(self, key):
        hash_index = self.hash_function(key)
        if self.table[hash_index] is None:
            self.table[hash_index] = key
        else:
            print(f"Colisión en índice {hash_index} al insertar {key}")

    def display(self):
        for i, val in enumerate(self.table):
            if val is not None:
                print(f"Índice {i}: {val}")
            else:
                print(f"Índice {i}: Vacío")

# Ejemplo de uso:
if __name__ == "__main__":
    size = 10  # Tamaño de la tabla hash
    keys = [19, 27, 36, 10, 64, 73, 20, 25, 30]

    # Se puede elegir un valor específico para A, o dejar que se elija aleatoriamente
    A = 0.6180339887  # Constante recomendada (1 - raíz cuadrada de 5) / 2
    hash_table = MultiplicationHashTable(size, A)
    
    # Insertar claves en la tabla hash
    for key in keys:
        hash_table.insert(key)

    # Mostrar tabla hash
    hash_table.display()
