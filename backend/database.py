from sqlmodel import SQLModel, Field, create_engine, Session

# Define a Question-Answer model
class QA(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    question: str
    answer: str

# Create the SQLite database
engine = create_engine("sqlite:///qa_history.db")
SQLModel.metadata.create_all(engine)

# Helper function to log data
def log_to_db(question, answer):
    with Session(engine) as session:
        qa = QA(question=question, answer=answer)
        session.add(qa)
        session.commit()

# Helper function to fetch history
def fetch_history():
    with Session(engine) as session:
        return session.query(QA).all()
