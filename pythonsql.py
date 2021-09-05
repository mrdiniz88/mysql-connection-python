import pyodbc

cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for MySQL};User ID=root;Password=IgorDiniz88.;Server=localhost;Database=PythonSQL;Port=3306;String Types=Unicode')
print('conexão bem sucedida')

cursor = cnxn.cursor()

nome = str(input('Digite seu nome: '))
cpf = int(input('Digite seu cpf: '))

comando = f"""INSERT INTO Pessoas(nome, cpf)
VALUES
	('{nome}', {cpf})"""

cursor.execute(comando)
cursor.commit()