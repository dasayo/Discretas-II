from hash_table import Hash_table

class gestor_placas:
    def __init__(self):
        self.placas = Hash_table(7)
    
    def insertar_placa(self, placa: str, modelo: str):
        """Función que inserta en placas usando la clase HashTable."""
        self.placas.insert(placa, modelo)

    def buscar_placa(self, placa: str):
       """Función que busca una placa de auto en la tabla hash."""
       return self.placas.search(placa)
    
    def borrar_placa(self, placa: str):
        """Función que borra una placa de auto de la tabla hash."""
        return self.placas.delete(placa)

    def __str__(self):
        return str(self.placas)

def main():
    gestor = gestor_placas()

    print("Insertando placas...")
    gestor.insertar_placa("PLA008", "Toyota")
    gestor.insertar_placa("PLA001", "Ford")

    print("Buscando placas...")
    print(gestor.buscar_placa("PLA008"))
    print(gestor.buscar_placa("PLA001"))

    print("Borrando placas...")
    gestor.borrar_placa("PLA008")

    print("Buscando placas...")
    print(gestor.buscar_placa("PLA008"))
    print(gestor.buscar_placa("PLA001"))

if __name__ == "__main__":
    main()