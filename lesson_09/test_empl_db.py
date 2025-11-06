from empl import Company
from EmplTable import EmplTable
import pytest

api = Company("http://5.101.50.27:8000")
db = EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

def setup_module(module):
    db.create_table()
    db.delete_all_employees()  # Очищаем таблицу сотрудников перед тестами

def teardown_module(module):
    db.dispose()  # Используем метод dispose()

def test_create_and_get_employee():
    name = "SkyPro"
    descr = "testing"
    company = api.create_company(name, descr)
    new_company_id = company["id"]

    len_before = len(db.get_employees())

    db.insert_employee("Sakina", "Nagieva", "+123456789", new_company_id)

    len_after = len(db.get_employees())

    assert len_after - len_before == 1

    employee_list = api.get_list_employee(new_company_id)
    assert any(employee["firstName"] == "Sakina" and employee["lastName"] == "Nagieva" for employee in employee_list)

def test_update_employee():
    employees = db.get_employees()
    assert len(employees) > 0

    employee_id = employees[0]["id"]
    db.update_employee(employee_id, "Jane", "Doe", "Middle", "+987654321", "jane.doe@example.com", "http://example.com")

    updated_employee = db.get_employee_by_id(employee_id)  # Получаем обновленного сотрудника напрямую
    assert updated_employee["first_name"] == "Jane"
    assert updated_employee["last_name"] == "Doe"
    assert updated_employee["middle_name"] == "Middle"
    assert updated_employee["phone"] == "+987654321"
    assert updated_employee["email"] == "jane.doe@example.com"
    assert updated_employee["avatar_url"] == "http://example.com"

def test_delete_all_employees():
    employees = db.get_employees()

    for employee in employees:
        employee_id = employee["id"]
        db.delete_employee(employee_id)

    employees_after_deletion = db.get_employees()
    assert len(employees_after_deletion) == 0
