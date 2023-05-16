from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from pg_credentials import SQLALCHEMY_DATABASE_URL


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = Session(autocommit=False, autoflush=False, bind=engine)

metadata = MetaData()
metadata.reflect(engine, only=[
    'Apartments', 'Buildings', 'CheckinJournal', 'Employers',
    'FinancialJournal', 'Jobs', 'Participants', 'ParticipantStatusLogs',
    'Pubs', 'Restaurants', 'Schools', 'SocialNetwork', 'TravelJournal'
])
Base = automap_base(metadata=metadata)
Base.prepare()

Apartments = Base.classes.Apartments
Buildings = Base.classes.Buildings
Employers = Base.classes.Employers
Jobs = Base.classes.Jobs
Participants = Base.classes.Participants
Pubs = Base.classes.Pubs
Restaurants = Base.classes.Restaurants
Schools = Base.classes.Schools
SocialNetwork = Base.classes.SocialNetwork

ParticipantStatusLogs = Base.classes.ParticipantStatusLogs
FinancialJournal = Base.classes.FinancialJournal
CheckinJournal = Base.classes.CheckinJournal
TravelJournal = Base.classes.TravelJournal