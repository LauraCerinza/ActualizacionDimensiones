from conexion import conectar_origen, conectar_dw


def actualizar_productos():
    origen = conectar_origen()
    dw = conectar_dw()

    cursor_origen = origen.cursor(dictionary=True)
    cursor_dw = dw.cursor(dictionary=True)

    cursor_origen.execute("""
        SELECT id_producto, nombre, categoria, precio
        FROM producto
    """)

    productos = cursor_origen.fetchall()

    for producto in productos:
        cursor_dw.execute("""
            SELECT id_producto
            FROM dim_producto
            WHERE id_producto = %s
        """, (producto["id_producto"],))

        existe = cursor_dw.fetchone()

        if existe:
            cursor_dw.execute("""
                UPDATE dim_producto
                SET nombre = %s,
                    categoria = %s,
                    precio = %s
                WHERE id_producto = %s
            """, (
                producto["nombre"],
                producto["categoria"],
                producto["precio"],
                producto["id_producto"]
            ))
        else:
            cursor_dw.execute("""
                INSERT INTO dim_producto
                (id_producto, nombre, categoria, precio)
                VALUES (%s, %s, %s, %s)
            """, (
                producto["id_producto"],
                producto["nombre"],
                producto["categoria"],
                producto["precio"]
            ))

    dw.commit()

    cursor_origen.close()
    cursor_dw.close()
    origen.close()
    dw.close()


if __name__ == "__main__":
    actualizar_productos()
    print("Dimensión producto actualizada.")
