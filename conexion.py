import mysql.connector


def conectar_origen():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="base_operacional"
    )


def conectar_dw():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="datawarehouse"
    )
