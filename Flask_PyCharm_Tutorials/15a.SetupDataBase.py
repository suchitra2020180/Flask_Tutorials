from Flask_withSQL_Database import db, Table, app


#Create all the tables model==> db table
with app.app_context():
    db.create_all()

    sam=Table('Sammy',3)
    frank=Table('Frankie',4)


    #Output is None,none
    print(sam.id)
    print(frank.id)
    ###Saving multiple enteries to the table
    db.session.add_all([sam,frank])

    db.session.commit()

    print(sam.id)
    print(frank.id)