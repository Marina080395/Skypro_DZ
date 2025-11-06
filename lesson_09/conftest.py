import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base, Subject

# Конфигурация базы данных
DB_URL = "postgresql://postgres:postMarina@localhost:5432/mydatabase"


@pytest.fixture(scope="module")
def engine():
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()


@pytest.fixture(autouse=True)
def cleanup_db(session):
    """Автоматически очищает базу после каждого теста"""
    yield
    # Удаляем все данные в правильном порядке
    # (сначала дочерние, потом родительские таблицы)
    session.execute(text("DELETE FROM group_student"))
    session.execute(text("DELETE FROM student"))
    session.execute(text("DELETE FROM users"))
    session.execute(text("DELETE FROM subject"))
    session.commit()


@pytest.fixture
def test_subject(session):
    subject = session.query(Subject).filter_by(subject_id=1).first()
    if not subject:
        subject = Subject(subject_id=1, subject_title="Математика")
        session.add(subject)
        session.commit()
    return subject
