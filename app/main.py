from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal, engine, Apartments, Buildings, CheckinJournal, Employers, FinancialJournal, \
    Jobs, Participants, ParticipantStatusLogs, Pubs, Restaurants, Schools, SocialNetwork, TravelJournal

app = FastAPI(title="VAST 2022 data access", openapi_prefix='/')

# Configure CORS rules for external access
origins = [
    'http://localhost:8080'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=['*']
)


@app.get("/")
async def root():
    return {"message": "This is an API to access data for VAST Challenge 2022"}


@app.get("/Apartments")
async def aparments_all():
    db_apartments = SessionLocal.query(Apartments).all()
    return db_apartments


@app.get("/Buildings")
async def buildings_all():
    db_buildings = SessionLocal.query(Buildings).all()
    return db_buildings


@app.get("/Employers")
async def employers_all():
    db_employers = SessionLocal.query(Employers).all()
    return db_employers


@app.get("/Jobs")
async def jobs_all():
    db_jobs = SessionLocal.query(Jobs).all()
    return db_jobs


@app.get("/Participants")
async def participants_all():
    db_participants = SessionLocal.query(Participants).all()
    return db_participants


@app.get("/Pubs")
async def pubs_all():
    db_pubs = SessionLocal.query(Pubs).all()
    return db_pubs


@app.get("/Restaurants")
async def restaurants_all():
    db_restaurants = SessionLocal.query(Restaurants).all()
    return db_restaurants


@app.get("/Schools")
async def schools_all():
    db_schools = SessionLocal.query(Schools).all ()
    return db_schools


def query_logs_by_participant_id(sa_class, participantId, limit=1000, offset=0):
    return SessionLocal.query(sa_class) \
        .filter_by(participantId=participantId).limit(limit).offset(offset).all()


@app.get("/ParticipantStatusLogs")
async def participant_status_logs_all(participantId: int, limit: int = 1000, offset: int = 0):
    db_participant_status_logs = query_logs_by_participant_id(ParticipantStatusLogs, participantId, limit, offset)
    return db_participant_status_logs


@app.get("/CheckinJournal")
async def checkin_journal_all(participantId: int, limit: int = 1000, offset: int = 0):
    db_checkin_journal = query_logs_by_participant_id(CheckinJournal, participantId, limit, offset)
    return db_checkin_journal


@app.get("/FinancialJournal")
async def financial_journal_all(participantId: int, limit: int = 1000, offset: int = 0):
    db_financial_journal = query_logs_by_participant_id(FinancialJournal, participantId, limit, offset)
    return db_financial_journal


@app.get("/TravelJournal")
async def travel_journal_all(participantId: int, limit: int = 1000, offset: int = 0):
    db_travel_journal = query_logs_by_participant_id(TravelJournal, participantId, limit, offset)
    return db_travel_journal
