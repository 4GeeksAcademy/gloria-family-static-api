"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # Iniciamos el contador en 1
        self._next_id = 1
        self._members = []
        # Se crean los miembros por defecto.
        # Se espera que el miembro "Tommy" tenga id 3443, y los otros se agreguen sin id predefinido.
        default_members = [
            {"id": 3443, "first_name": "Tommy", "age": 22, "lucky_numbers": [7]},
            {"first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
            {"first_name": "Jimmy", "age": 5, "lucky_numbers": [1]}
        ]
        for member in default_members:
            self.add_member(member)

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # Se garantiza que se use el apellido de la familia.
        member["last_name"] = self.last_name

        # Si se provee un id, se usa ese id y se ajusta el contador si corresponde.
        if "id" in member:
            # Se asegura que sea un entero.
            if type(member["id"]) != int:
                member["id"] = int(member["id"])
            if member["id"] >= self._next_id:
                self._next_id = member["id"] + 1
        else:
            member["id"] = self._generate_id()
        
        # Se asegura que lucky_numbers sea una lista; si no se envía se usa lista vacía.
        member["lucky_numbers"] = member.get("lucky_numbers", [])
        self._members.append(member)
        return member

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True  # Eliminación exitosa.
        return False  # No se encontró el miembro.

    def get_member(self, id):
        for member in self._members:
            if member["id"] == int(id):
                return member
        return None

    def update_member(self, member):
        # Se recorre la lista y se actualiza el miembro que coincida con el id.
        for i, m in enumerate(self._members):
            if m["id"] == member["id"]:
                member["last_name"] = self.last_name  # Se asegura el apellido de la familia.
                self._members[i] = member
                return member
        return None

    def get_all_members(self):
        return self._members
