import mysql.connector

print("Csatlakozás az adatbázishoz...")

try:
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password=""
    )
    cursor = db.cursor()

    print("Sikeres csatlakozás.")
    print("Adatbázis és tábla létrehozása...")

    cursor.execute("CREATE DATABASE IF NOT EXISTS memorygamedb")
    cursor.execute("USE memorygamedb")

    create_table_sql = """
        CREATE TABLE IF NOT EXISTS highscore (
            id INT(11) NOT NULL auto_increment,
            name VARCHAR(20) NOT NULL,
            time TIME NOT NULL,
            PRIMARY KEY (id)
        );
        
    """

    cursor.execute(create_table_sql)

    print("Sikeresen létrejött az adatbázis és a tábla!")

except mysql.connector.Error as err:
    if err.errno == 2003:
        print("Nem lehetett csatlakozni az adatbázishoz! Nézd meg, hogy biztosan fut-e!")
    else:
        print("Valami hiba történt: {}".format(err))
