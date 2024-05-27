import  mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username = "root",
    password = "satyamrana",
    database = "TestPython"
)

mycursor = mydb.cursor()

# mycursor.execute("insert into Student (Name) values ('Om')")
mycursor.execute(f"insert into Student (Name) values ('{input("Enter The Name: ")}')")
mydb.commit()

mycursor.execute("select * from student")

for  i,j in mycursor:
    print(i,j)



