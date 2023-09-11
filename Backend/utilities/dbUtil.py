import pymysql

connection = pymysql.connect(host="localhost", user="root", password="XXXXXXX", database="Employee")


class DbConnection:

    @staticmethod
    def executeQuery(query):
        con = pymysql.connect(host="localhost",
                              user="root",
                              password="Vasu@9341",
                              database="Employee")
        try:
            cursor = con.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            print("You're connected to database")
            print("************* Query Result *************")
            print(data)
        except pymysql.Error as e:
            print("Error while connecting to MySQL:", e)
        finally:
            cursor.close()
            con.close()
            print("MySQL connection is closed")
