import datetime
import mysql.connector
import random

mydb = mysql.connector.connect(host="localhost", user="root", password="amitv9493")
cursor = mydb.cursor()
cursor.execute("use de_practice")

years = [2024, 2023, 2025]
for i in range(50):
    random_date = datetime.date(
        random.choice(years), random.randint(1, 12), random.randint(1, 28)
    )
    random_amount = random.randint(1000, 5000)
    cursor.execute(
        """insert into shop_sales_data (sale_date, amount) values (%s,%s)""",
        (
            random_date,
            random_amount,
        ),
    )
mydb.commit()
