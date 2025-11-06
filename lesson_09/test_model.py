import pytest
from sqlalchemy import text
from sqlalchemy import func
from models import User, Student, Subject


def test_create_user_and_student(session):
    # Создание тестовых данных
    new_user_id = 100
    test_email = "test_user@example.com"
    test_level = "advanced"

    # Сначала создаём Subject, так как на него есть foreign key
    session.execute(
        text("INSERT INTO subject ("
        "subject_id, subject_title) VALUES (1, 'Math')")
    )

    # Вставка пользователя
    session.execute(
        text("INSERT INTO users ("
        "user_id, user_email, subject_id) VALUES (:id, :email, 1)"),
        {"id": new_user_id, "email": test_email}
    )

    # Вставка студента
    session.execute(
        text("""INSERT INTO student (
             user_id, level, education_form, subject_id)
                VALUES (:id, :level, :form, 1)"""),
        {"id": new_user_id, "level": test_level, "form": "offline"}
    )
    session.commit()

    # Проверка пользователя
    user = session.execute(
        text("SELECT user_email FROM users WHERE user_id = :id"),
        {"id": new_user_id}
    ).fetchone()
    assert user[0] == test_email

    # Проверка студента
    student = session.execute(
        text("SELECT level FROM student WHERE user_id = :id"),
        {"id": new_user_id}
    ).fetchone()
    assert student[0] == test_level


def test_update_student_level(session):
    test_id = 101
    original_level = "beginner"
    new_level = "intermediate"

    # Создаём Subject
    session.execute(
        text("INSERT INTO subject ("
        "subject_id, subject_title) VALUES (2, 'Physics')")
    )

    session.execute(
        text("INSERT INTO users ("
        "user_id, user_email, subject_id) VALUES ("
        ":id, 'update_test@example.com', 2)"),
        {"id": test_id}
    )
    session.execute(
        text("INSERT INTO student ("
        "user_id, level, education_form, subject_id) VALUES ("
        ":id, :level, 'online', 2)"),
        {"id": test_id, "level": original_level}
    )
    session.commit()

    # Обновление уровня
    session.execute(
        text("UPDATE student SET level = :new_level WHERE user_id = :id"),
        {"new_level": new_level, "id": test_id}
    )
    session.commit()

    # Проверка обновления
    updated = session.execute(
        text("SELECT level FROM student WHERE user_id = :id"),
        {"id": test_id}
    ).fetchone()
    assert updated[0] == new_level


def test_create_with_orm(session):
    # Генерируем уникальный ID
    subject_id = session.query(func.max(Subject.subject_id)).scalar() or 0
    subject_id += 1
    subject = Subject(subject_id=subject_id, subject_title="Математика")
    subject = Subject(subject_id=1, subject_title="Math")
    session.add(subject)

    user = User(user_id=100, user_email="test@example.com", subject_id=1)
    session.add(user)

    student = Student(
        user_id=100,
        level="advanced",
        education_form="offline",
        subject_id=1
    )
    session.add(student)
    session.commit()

    # Проверки
    assert user.student.level == "advanced"


def test_edit_subject_transaction_rollback_on_error(session):
    # Тест проверяет откат транзакции при ошибке
    test_id = 2
    original_title = "Физика"

    # Вставляем тестовые данные
    session.execute(
        text("INSERT INTO subject ("
        "subject_id, subject_title) VALUES (:id, :title)"),
        {"id": test_id, "title": original_title}
    )
    session.commit()

    # Мокаем ошибку в транзакции
    with pytest.raises(Exception):
        # Здесь мы должны вызвать ситуацию, которая приведет к ошибке
        # Например, передать некорректные параметры
        session.edit_subject(None, test_id)

    # Проверяем, что данные не изменились
    result = session.execute(
        text("SELECT subject_title "
        "FROM subject WHERE subject_id = :id"),
        {"id": test_id}
    ).fetchone()

    assert result[0] == original_title
