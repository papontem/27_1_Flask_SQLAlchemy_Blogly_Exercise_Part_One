"""Seed file to make sample data for blogly db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add Users
# TODO: NEED TO figure out why imgs from unsplash are not loading 
whiskey  = User( first_name='Whiskey'    ,last_name='Tango'    ,img_url='https://unsplash.com/photos/TSkUCyCuVH4' )
bowser   = User( first_name='Bowser Jr.' ,last_name='Koopa'    ,img_url='https://unsplash.com/photos/X-0FisCRIaA' )
spike    = User( first_name='Spike'      ,last_name='Chain'    ,img_url='https://unsplash.com/photos/zqhe4qjVTJI' )

# Add new objects to session, so they'll persist
db.session.add_all([whiskey,bowser,spike])

# Commit--otherwise, this never gets saved!
db.session.commit()