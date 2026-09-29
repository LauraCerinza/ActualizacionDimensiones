from conexion import conectar_origen, conectar_dw


def actualizar_tiendas():
    origen = conectar_origen()
    dw = conectar_dw()

    cursor_origen = origen.cursor(dictionary=True)
    cursor_dw = dw.cursor(dictionary=True)

    cursor_origen.execute("""
        SELECT id_tienda, nombre, ciudad, direccion
        FROM tienda
    """)

    tiendas = cursor_origen.fetchall()

    for tienda in tiendas:
        cursor_dw.execute("""
            SELECT id_tienda
            FROM dim_tienda
            WHERE id_tienda = %s
        """, (tienda["id_tienda"],))

        existe = cursor_dw.fetchone()

        if existe:
            cursor_dw.execute("""
                UPDATE dim_tienda
                SET nombre = %s,
                    ciudad = %s,
                    direccion = %s
                WHERE id_tienda = %s
            """, (
                tienda["nombre"],
                tienda["ciudad"],
                tienda["direccion"],
                tienda["id_tienda"]
            ))
        else:
            cursor_dw.execute("""
                INSERT INTO dim_tienda
                (id_tienda, nombre, ciudad, direccion)
                VALUES (%s, %s, %s, %s)
            """, (
                tienda["id_tienda"],
                tienda["nombre"],
                tienda["ciudad"],
                tienda["direccion"]
            ))

    dw.commit()

    cursor_origen.close()
    cursor_dw.close()
    origen.close()
    dw.close()


if __name__ == "__main__":
    actualizar_tiendas()
    print("Dimensión tienda actualizada.")
