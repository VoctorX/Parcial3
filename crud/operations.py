from crud.database import conexion

def crear(contact_id, name, phone, image_path):
    cursor= conexion.cursor()
    query= "INSERT INTO contactos (id, name, phone, image_path) VALUES (?,?,?,?)"
    cursor.execute(query, (contact_id, name, phone, image_path))
    conexion.commit()


def leer():
    cursor= conexion.cursor()
    query= "SELECT id, name, phone, image_path from contactos"
    cursor.execute(query)
    return cursor.fetchall()

def actualizar(contact_id, name=None, phone=None, image_path=None):
    cursor = conexion.cursor()
    query_parts = []
    params = []

    # Construir la consulta dinámicamente
    if name:
        query_parts.append("name = ?")
        params.append(name)
    if phone:
        query_parts.append("phone = ?")
        params.append(phone)
    if image_path:
        query_parts.append("image_path = ?")
        params.append(image_path)
    
    # Si el usuario no introdujo nada, no hacemos nada
    if not query_parts:
        return True

    query = f"UPDATE contactos SET {', '.join(query_parts)} WHERE id = ?"
    params.append(contact_id)
    
    cursor.execute(query, tuple(params))
    conexion.commit()
    return cursor.rowcount > 0

def eliminar(contact_id):
    cursor= conexion.cursor()
    query= "DELETE FROM contactos WHERE id = ?"
    cursor.execute(query, (contact_id,))
    conexion.commit()
    return cursor.rowcount > 0
