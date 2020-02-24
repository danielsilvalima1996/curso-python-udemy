from mysql.connector import connect

conexao = connect(
    host="127.0.0.1",
    user="root",
    password="admin123!@#"
)

cursor = conexao.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS agenda')
