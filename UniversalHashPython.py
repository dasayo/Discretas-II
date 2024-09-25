import random
from sympy import nextprime

class UniversalHashTable:
    def __init__(self, size):
        self.size = size
        self.prime = self.nextprime(self.size)  # Elige un primo mayor al tamaño
        self.a = random.randint(1, self.prime - 1)  # 1 <= a < prime
        self.b = random.randint(0, self.prime - 1)  # 0 <= b < prime
        self.table = [None] * size

    def hash_function(self, key):
        # Función hash universal: ((a * key + b) % prime) % size
        return ((self.a * key + self.b) % self.prime) % self.size

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
    size = 10000  # Tamaño de la tabla
    keys = [19, 27, 36, 10, 64, 73, 20, 25, 30,5287,7259,5590]

    hash_table = UniversalHashTable(size)
    
    # Insertar claves en la tabla hash
    for key in keys:
        hash_table.insert(key)

    # Mostrar tabla hash
    hash_table.display()
