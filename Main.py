

#working with database - sqlite

import sqlite3

#connector to database : global

db = sqlite3.connect("pyslitedb")

#function to create table
def createTable():

    db.row_factory = sqlite3.Row
    #creating the table
    db.execute("create table if not exists Admin(ID integer primary key autoincrement , Name text , Age int , Sex text , Address text)")
    db.commit()

#function for adding records
def addRecords(Name,Age,Sex,Address):
    db.row_factory = sqlite3.Row
    # creating the table
    db.execute("insert into Admin(Name,Age,Sex,Address) values(?,?,?,?)", (Name, Age, Sex, Address))
    print("Record has been added successfuly! ")
    # commit/add data to the database
    db.commit()

#function for deleting records
def deleteRecords(ID):
    db.row_factory = sqlite3.Row
    # creating the table
    db.execute("delete from Admin where ID = {}".format(ID))
    print("Record has been deleted successfully! ")
    db.commit()

#function for updating records
def updateRecords(ID,Age):
    db.row_factory = sqlite3.Row
    # creating the table
    db.execute("update Admin set Age=? where ID=?", (Age,ID))
    print("Record has been Updated successfuly! ")
    # commit/add data to the database
    db.commit()


#funciton to list admins in the database
def listAdmins():
    #selectadmins from database
    cursor = db.execute("select * from Admin")
    #loop all admins for display
    for row in cursor:
        print("ID : {} , Name : {} , Age {} : ,Sex : {} , Address : {} ".format(row["ID"],row["Name"],row["Age"],row["Sex"],row["Address"]))






def main():

    #loop the application to always run
    while 1:
        # call create table function
        createTable()
        indexOperation = int(input("\n\tSELECT AN OPERATION "
                                   "\n\n\t 1.Add Record."
                                   " \n\t 2.List Admins."
                                   "\n\t 3.Delete Admin "
                                   "\n\t 4. Update Age"
                                   " \n\t 0.Exit."))


        if(indexOperation == 0):
            break;
        # capture selection of input
        # call funciton addRecords if selction == 1
        elif (indexOperation == 1):
            Name = input("\n\tEnter Name : ")
            Age = int(input("\n\tEnter age : "))
            Sex = input("\n\tEnter Sex (Male/Female/None) : ")
            Address = input("\n\tEnter Your Address : ")
            addRecords(Name, Age, Sex, Address)
        elif (indexOperation == 2):
            # call function listAdmins if selection == 2
            listAdmins()
        elif (indexOperation == 3):
            print("Delete User from Database: ")
            ID = int(input("Enter the ID of user u need to delete: "))
            deleteRecords(ID)
        elif(indexOperation == 4):
            ID = input("Enter Admins ID : ")
            Age = int(input("Enter new Age :"))
            updateRecords(ID, Age)









if __name__ == '__main__':main()

