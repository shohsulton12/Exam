# Shohsulton Muhamedjonov
# N42
# EXAM
# 09.05.2024


# 1-masala


import psycopg2, threading
from psycopg2 import Error


def connect():
    try:
        conn = psycopg2.connect(
            dbname="n42",
            user="postgres",
            password="123",
            host="localhost",
            port="5432"
        )
        return conn
    except Error as e:
        print("Error in sign in to sql", e)
        return None


def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists Product (
            id serial primary key,
            name varchar(255)   not null,
            price   int not null,
            color varchar(255) ,
            image varchar(255)  
        )
    """)
    conn.commit()
    print("Produc table created successfully")
    cur.close()
    conn.close()


# 2-masala


def insert(name, price, color, image):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
                insert into Product (name, price,color,image) 
                values (%s,%s,%s,%s)
            """, (name, price, color, image))
    conn.commit()
    print("Datas inserted successfully")
    cur.close()
    conn.close()


def select(product_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from Product where id = %s", (product_id,))
    row = cur.fetchone()
    if row:
        print("ID", product_id, ":", row)
    else:
        print("ID", product_id, "NOT FOUND")
    cur.close()
    conn.close()


def update(product_id, name, price):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
            update Product
            set name = %s, price = %s
            where id = %s
        """, (name, price, product_id))
    conn.commit()
    print("Updated product successfully")
    cur.close()
    conn.close()


def delete(product_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("delete from Product where id = %s", (product_id,))
    conn.commit()
    print("Delete data successfully")
    cur.close()
    conn.close()


connect()

create_table()

insert(name="<Phone>", price=100, color="<black>", image="<lnlnvf>")
insert(name="<Book>", price=499, color="<red>", image="<mdlvmefl>")
insert(name="<Pen>", price=133, color="<blue>", image="<sdnaldc>")

select(product_id=1)

update(product_id=1, name="<Soat>", price=300)

delete(product_id=3)


# 3-masala


class Alphabet:
    def __init__(self):
        self.letters = [chr(i) for i in range(97, 123)]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.letters):
            letter = self.letters[self.index]
            self.index += 1
            return letter
        else:
            raise StopIteration


alphabet = Alphabet()
for letter in alphabet:
    print(letter)


# 4-masala


def print_numbers():
    for i in range(1, 5):
        print("Thread number:", i)


def print_letters():
    for lettere in ['a', 'b', 'c', 'd', 'e']:
        print("Thread letter:", lettere)


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


# 5-masala

class Product:
    def __init__(self, name, price, color, image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Color:", self.color)
        print("Image:", self.image)


product = Product("Lap top", 1500, "White", "ndccbk")
product.save()

# 6-masala


dbconnect = {
    'host': 'localhost',
    'database': 'n42',
    'user': 'postgres',
    'password': '123',
    'port': 5432,
    'options': '-c search_path=dbo,public'
}


class DbConnect:
    def __init__(self, db_params):
        self.dbconnect = db_params

    def __enter__(self):
        self.conn = psycopg2.connect(**self.dbconnect)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()


# 7-masala


# https://github.com/shohsulton12/Exam
