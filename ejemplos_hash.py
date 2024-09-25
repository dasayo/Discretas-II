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

class contacto:
    def __init__(self, nombre: str, correo: str, direccion: str, estado: str, 
    historial_llamadas: list):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.estado = estado
        self.historial_llamadas = historial_llamadas

    def __str__(self):
        return f"Nombre: {self.nombre}, Correo: {self.correo},Dirección: {self.direccion}, Estado: {self.estado}, Historial de llamadas: {self.historial_llamadas}"

class gestor_contactos:

    def __init__(self):
        """constructor de la clase gestor_contactos donde tenemos una lista de tablas hash."""
        self.tabla_contactos = {}

    def insertar_contacto(self, numero: str, contacto: contacto):
        """Función que inserta un contacto en la tabla hash."""
        if numero[:3] not in self.tabla_contactos:
            "agreganmos una tabla hash nueva"
            self.tabla_contactos[numero[:3]] = Hash_table()
            self.tabla_contactos[numero[:3]].insert(numero[3:], contacto)
        else:
            self.tabla_contactos[numero[:3]].insert(numero[3:], contacto)
    
    def buscar_contacto(self, numero: str):
        """Función que busca un contacto en la tabla hash."""
        if numero[:3] in self.tabla_contactos:
            return self.tabla_contactos[numero[:3]].search(numero[3:])
        else:
            return None
    
    def __str__(self):
        return str(self.tabla_contactos)


def main():
    gestor = gestor_placas()

    print("Insertando placas...")
    gestor.insertar_placa("PLA008", "Toyota")
    gestor.insertar_placa("PLA001", "Ford")
    
    "valores en la tabla hash"
    print(gestor)

    print("Buscando placas...")
    print(gestor.buscar_placa("PLA008"))
    print(gestor.buscar_placa("PLA001"))

    print("Borrando placas...")
    gestor.borrar_placa("PLA008")

    print("Buscando placas...")
    print(gestor.buscar_placa("PLA008"))
    print(gestor.buscar_placa("PLA001"))

    print("usando gestor_contactos..... \n\n\n")
    gestor_contactos_1 = gestor_contactos()

    contacto1 = contacto("Juan", "juan@email.com", "Calle 1", "Activo",[{"fecha": "2021-01-01", "duracion": "10 min"}])

    gestor_contactos_1.insertar_contacto("3011231278", contacto1)

    print(gestor_contactos_1.buscar_contacto("3011231278"))

if __name__ == "__main__":
    main()