def test_create_project(auth_header):
    project_name = generate_random_string()
    payload = {"name": project_name, "description": "Test project"}
    response = requests.post(BASE_URL + "/projects", json=payload, headers=auth_header)
    assert response.status_code == 201
    project = response.json()
    assert project["name"] == project_name

def test_update_project(auth_header):
    project_id = 8  # Здесь предполагается, что у меня есть проект с данным ID
    payload = {"name": "Updated Project", "description": "Updated Description"}
    response = requests.put(BASE_URL + f"/projects/{project_id}", json=payload, headers=auth_header)
    assert response.status_code == 200
    project = response.json()
    assert project["name"] == "Updated Project"

def test_get_project(auth_header):
    project_id = 8  # Предполагаю, что проект с указанным ID существует
    response = requests.get(BASE_URL + f"/projects/{project_id}", headers=auth_header)
    assert response.status_code == 200
    project = response.json()
    assert isinstance(project, dict)

def test_create_project_missing_fields(auth_header):
    payload = {}  # Отсутствие обязательного поля 'name'
    response = requests.post(BASE_URL + "/projects", json=payload, headers=auth_header)
    assert response.status_code == 400

def test_get_nonexistent_project(auth_header):
    project_id = 1234567890098  # Несуществующий ID
    response = requests.get(BASE_URL + f"/projects/{project_id}", headers=auth_header)
    assert response.status_code == 404
