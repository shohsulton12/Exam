# Shohsulton Muhamedjonov
# n42


# 1-masala


import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="123",
        host="localhost",
        port="5432",
        database="n42"
    )

    cursor = connection.cursor()

create_table_query = '''
        CREATE TABLE IF NOT EXISTS product (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price  VARCHAR NOT NULL,
            color VARCHAR(50),
            image VARCHAR(255)
        )
    '''
