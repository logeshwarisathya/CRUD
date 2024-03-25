import sqlite3
con=sqlite3.connect('users.db')

def insertdata(name,age,city):
    qry="insert into users (NAME,AGE,CITY) values (?,?,?);"
    con.execute(qry,(name,age,city))
    con.commit()
    print("user details added")

def updatedata(name,age,city,id):
    qry="update users set NAME=?,AGE=?,CITY=? where id=?;"
    con.execute(qry,(name,age,city,id))
    con.commit()
    print("user details updated")

def deletedata(id):
    qry="delete from users where id=?;"
    con.execute(qry,(id))
    con.commit()
    print("user details deleted")

def SelectData():
    qry="select * from users"
    result=con.execute(qry)
    for row in result:
        print(row)

print(""" 
1.Insert
2.Update
3.Delete
4.Select
""")

ch=1
while ch==1:
    c=int(input("select your choice :"))
    if (c==1):
        print("add new record")
        name=input("enter name:")
        city=input("enter city:")
        age=input("enter age:")
        insertdata(name,age,city)
    elif (c==2):
        print("edit A record")
        id=input("enter ID:")
        name=input("enter name:")
        city=input("enter city:")
        age=input("enter age:")
        updatedata(name, age, city, id)
    elif (c==3):
        print("Delete A record")
        id = input("enter ID:")
        deletedata(id)

    elif (c==4):
        print("print all record")
        SelectData()
    else:
        print("invalid selection")
    
print("Thank You")
