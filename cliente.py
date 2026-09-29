from conexion import conectar_origen, conectar_dw


def actualizar_clientes():
    origen = conectar_origen()
    dw = conectar_dw()

    cursor_origen = origen.cursor(dictionary=True)
    cursor_dw = dw.cursor(dictionary=True)

    cursor_origen.execute("""
        SELECT id_cliente, nombre, apellido, ciudad, telefono, correo
        FROM cliente
    """)

    clientes = cursor_origen.fetchall()

    for cliente in clientes:
        cursor_dw.execute("""
            SELECT id_cliente
            FROM dim_cliente
            WHERE id_cliente = %s
        """, (cliente["id_cliente"],))

        existe = cursor_dw.fetchone()

        if existe:
            cursor_dw.execute("""
                UPDATE dim_cliente
                SET nombre = %s,
                    apellido = %s,
                    ciudad = %s,
                    telefono = %s,
                    correo = %s
                WHERE id_cliente = %s
            """, (
                cliente["nombre"],
                cliente["apellido"],
                cliente["ciudad"],
                cliente["telefono"],
                cliente["correo"],
                cliente["id_cliente"]
            ))
        else:
            cursor_dw.execute("""
                INSERT INTO dim_cliente
                (id_cliente, nombre, apellido, ciudad, telefono, correo)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                cliente["id_cliente"],
                cliente["nombre"],
                cliente["apellido"],
                cliente["ciudad"],
                cliente["telefono"],
                cliente["correo"]
            ))

    dw.commit()

    cursor_origen.close()
    cursor_dw.close()
    origen.close()
    dw.close()


if __name__ == "__main__":
    actualizar_clientes()
    print("Dimensión cliente actualizada.")
