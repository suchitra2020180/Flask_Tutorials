#Basic.py
#Run the script only once
#Create enteries into the table
from Flask_Relationships_model import db,Puppy, Owner, Toy,app

with app.app_context():
    #Creating 2 puppy objects:
    rufus=Puppy('Rufus')
    fido=Puppy('Fido')

    #Add Puppies to db
    db.session.add_all([rufus,fido])
    db.session.commit()

    #Check!
    print(Puppy.query.all())

    #Grab Rufus from the database
    #Give me the first puppy whose name is Puppy
    rufus=Puppy.query.filter_by(name='Rufus').first()
    print('Here Rufus has no owner:',rufus)
    #or
    #rufus=Puppy.query.filter_by(name='Rufus').all()[0]
    # Create Owner Object
    #create owner for Rufus
    #obj=Owner(name,id) ==>Here id is Rufus id
    jose=Owner('Jose',rufus.id)

    #Give Rufus some toys
    toy1 = Toy('Chew Toy',rufus.id)
    toy2 = Toy('Ball', rufus.id)

    #Adding the objects to table
    db.session.add_all([jose,toy1,toy2])
    db.session.commit()

    #Grab Rufus after additions
    rufus=Puppy.query.filter_by(name='Rufus').first()
    print(rufus)
    #Now it should show rufus toys also.
    print(rufus.report_toys())





