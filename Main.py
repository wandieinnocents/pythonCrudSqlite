

#working with database - sqlite

import sqlite3

#connector to database : global

db = sqlite3.connect("pyslitedb")

#function to create table
def createTable():

    db.row_factory = sqlite3.Row
    #creating the table
    db.execute("create table if not exists Admin(Name text , Age int , Sex text , Address text)")
    db.commit()

def addRecords(Name,Age,Sex,Address):
    db.row_factory = sqlite3.Row
    # creating the table
    db.execute("insert into Admin(Name,Age,Sex,Address) values(?,?,?,?)", (Name, Age, Sex, Address))

    # commit/add data to the database
    db.commit()




def main():

    #call create table function
    createTable()
    indexOperation = int(input("\n\tSELECT AN OPERATION \n\n\t 1 - Add Record - "))
    #capture selection of input
    if(indexOperation == 1):
        Name = input("\n\tEnter Name : ")
        Age =  int(input("\n\tEnter age : "))
        Sex = input("\n\tEnter Sex (Male/Female/None) : ")
        Address = input("\n\tEnter Your Address : ")
        addRecords(Name,Age,Sex,Address)





if __name__ == '__main__':main()

