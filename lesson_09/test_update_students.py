from sqlalchemy import func
from models import User, Student, Subject


def test_update_student(session):
    # Сначала создаем предмет (Subject), если его нет
    subject = session.query(
        Subject).filter_by(subject_id=1).first()
    if not subject:
        subject = Subject(subject_id=1,
                          subject_title="Математика")
        session.add(subject)
        session.commit()

    # Получаем максимальное значение user_id из базы данных
    max_user_id = session.query(
        func.max(User.user_id)).scalar()

    # Если max_user_id равно None (база данных пуста),
    # устанавливаем начальное значение 1
    next_user_id = max_user_id + 1 if max_user_id else 1

    # Создаем пользователя и добавляем его в базу данных
    user = User(
        user_id=next_user_id,
        user_email="test@example.com",
        subject_id=subject.subject_id
    )
    session.add(user)
    session.commit()

    # Создаем студента и добавляем его в базу данных
    student = Student(
        user_id=user.user_id,
        level="beginner",
        education_form="online",
        subject_id=subject.subject_id
    )
    session.add(student)
    session.commit()

    # Обновляем уровень студента
    student_to_update = session.query(Student).filter_by(
        user_id=user.user_id
    ).first()
    student_to_update.level = "intermediate"
    session.commit()

    # Проверяем, что студент был успешно обновлен
    updated_student = session.query(Student).filter_by(
        user_id=user.user_id
    ).first()
    assert updated_student is not None
    assert updated_student.level == "intermediate"
    assert updated_student.education_form == "online"
    assert updated_student.subject_id == subject.subject_id

    # Удаляем студента и пользователя после завершения теста
    session.delete(student_to_update)
    session.delete(user)
    session.commit()
