from cliente import actualizar_clientes
from tienda import actualizar_tiendas
from producto import actualizar_productos


def ejecutar_pipeline():
    print("====================================")
    print(" INICIANDO PIPELINE DATA WAREHOUSE ")
    print("====================================")

    print("\n[1/3] Actualizando clientes...")
    actualizar_clientes()
    print("Clientes actualizados.")

    print("\n[2/3] Actualizando tiendas...")
    actualizar_tiendas()
    print("Tiendas actualizadas.")

    print("\n[3/3] Actualizando productos...")
    actualizar_productos()
    print("Productos actualizados.")

    print("\n====================================")
    print(" PIPELINE FINALIZADO CORRECTAMENTE ")
    print("====================================")


if __name__ == "__main__":
    ejecutar_pipeline()
