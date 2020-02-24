# -*- coding: utf-8 -*-
from mysql.connector import connect

conexao = connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='admin123!@#'
)

print(conexao)
