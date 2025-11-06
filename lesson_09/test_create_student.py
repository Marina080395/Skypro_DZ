from sqlalchemy import func
from models import User, Student, Subject


def test_create_student(session):
    # Сначала создаём предмет (subject), если его нет
    subject = session.query(
        Subject).filter_by(subject_id=1).first()
    if not subject:
        subject = Subject(
            subject_id=1, subject_title="Математика")
        session.add(subject)
        session.commit()

    # Получаем максимальное значение user_id из базы данных
    max_user_id = session.query(func.max(User.user_id)).scalar()

    # Если max_user_id равно None (база данных пуста),
    # устанавливаем начальное значение 1
    next_user_id = max_user_id + 1 if max_user_id else 1

    # Создаем пользователя и добавляем его в базу данных
    user = User(
        user_id=next_user_id,
        user_email="test@example.com",
        subject_id=subject.subject_id  # Используем ID существующего предмета
    )
    session.add(user)
    session.commit()

    # Создаем студента и добавляем его в базу данных
    student = Student(
        user_id=user.user_id,
        level="beginner",
        education_form="online",
        subject_id=subject.subject_id  # Используем тот же subject_id
    )
    session.add(student)
    session.commit()

    # Проверяем, что студент был успешно добавлен
    added_student = session.query(Student).filter_by(
        user_id=user.user_id
    ).first()
    assert added_student is not None
    assert added_student.level == "beginner"
    assert added_student.education_form == "online"
    assert added_student.subject_id == subject.subject_id

    # Удаляем студента и пользователя после завершения теста
    session.delete(student)
    session.delete(user)
    session.commit()
