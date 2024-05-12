#From Flask_withSQL_Database.py file import database(db) and class (Table)
from Flask_withSQL_Database import db, Table, app


with app.app_context():
    ##### CRUD  Operations

    ##1. Create
    #Create new entries into the table
    my_info=Table('Rani',5)
    #Adding single entry to the database table
    db.session.add(my_info)
    #Save the entry by commiting
    db.session.commit()


    ####2. Read
    #To retrieve all the enteries in the table:
    all_info=Table.query.all()
    print(all_info)

    #Select by Id
    # To retrieve enteries by id
    #entry_one=Table.query.get(1)    #Deprived commands
    entry_one = db.session.get(Table,1)
    print(entry_one.name)

    #Filters
    #To retreive or filter by column name
    table_frankie=Table.query.filter_by(name='Frankie')
    print(table_frankie.all())

    #O/p: Frankie is 4 years old


    ##  3. UPDATE
    ##Changing the age of Sam to 10 years from 3years old
    #First_person=Table.query.get(1)
    First_person=db.session.get(Table,1)
    First_person.age=10
    db.session.add(First_person)
    db.session.commit()


    ##  4.DELETE
    sec_person=Table.query.get(2)
    db.session.delete(sec_person)
    db.session.commit()

    Full_TableData=Table.query.all()
    print(Full_TableData)