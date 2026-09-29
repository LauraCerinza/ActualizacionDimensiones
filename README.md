# Pipeline Data Warehouse - Modelo Estrella

- Cliente
- Tienda
- Producto

## Estructura

- `conexion.py`: contiene las conexiones a la base operacional y al Data Warehouse.
- `cliente.py`: actualiza `dim_cliente`.
- `tienda.py`: actualiza `dim_tienda`.
- `producto.py`: actualiza `dim_producto`.
- `main.py`: ejecuta las tres actualizaciones.
- `requirements.txt`: dependencia necesaria.

## Antes de ejecutar

1. Tener Python instalado.
2. Tener MySQL instalado y ejecutándose.
3. Cambiar en `conexion.py`:
   - host
   - user
   - password
   - database
4. Verificar que los nombres y columnas de las tablas coincidan con los utilizados en los archivos Python.

## Instalación


pip install -r requirements.txt

## Ejecución

```bash
python main.py
```

También se puede ejecutar cada dimensión por separado:

```bash
python cliente.py
python tienda.py
python producto.py
```

## Lógica del pipeline

Para cada dimensión:

1. Se conecta a la base operacional.
2. Extrae los registros con `SELECT`.
3. Busca cada registro en el Data Warehouse.
4. Si existe, realiza `UPDATE`.
5. Si no existe, realiza `INSERT`.
6. Ejecuta `commit()` para guardar los cambios.

> IMPORTANTE: Las tablas y columnas incluidas son un ejemplo. Deben ajustarse al esquema real del proyecto.
