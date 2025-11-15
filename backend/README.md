# Soft

This is a minimal CRM System to help people and small companies tracking them leads.

API Docs: http://127.0.0.1:8000/api/docs/

## Structure

```txt
backend/
├── .devcontainer/
│   └── devcontainer.json
├── app/
│   ├── views/
│   │   ├── core_view.py
│   │   ├── auth_view.py
│   │   └── **_view.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── **_model.py
│   ├── schemas/
│   │   └── **_schema.py
│   ├── services/
│   │   └── **_service.py
│   ├── __init__.py
│   └── blueprints.py
├── migrations/
├── Dockerfile.py
├── .env
├── requirements.txt
└── config.py
```

## Technologies

```txt
Flask==3.1.0
SQLAlchemy==2.0.36
Flask-SQLAlchemy==3.1.1
Flask-Migrate==4.0.7
python-dotenv==1.0.1
mysqlclient==2.2.6
Flask-RESTful==0.3.10
marshmallow-sqlalchemy==1.1.0
flasgger
marshmallow==3.20.1 
flask-marshmallow
flask_smorest
flask-jwt-extended
passlib
flask_cors
pytest
pytest-flask
factory-boy 
faker
```

## How to use

You'll need to have Docker installed in your environment.


## Main commands

1 - If you need start your DB at the first time:<br>
```bash
flask db init
```

<br>

2 - After you add ou make some change:<br>

```bash
flask db migrate -m "your message"
```

<br>

3 - As soon as you run migrate, do it the upgrade: <br>

```bash
flask db upgrade
```
<br>

4 - Create a superadmin if not exists: <br>

```bash
flask create-superadmin
```


---

# How to use Roles and Permissions

This is very simple, you only need to use the decorator `@require_permission("lead:edit", "lead:assign")` if you need more than one permission, just put a list separeted by comma and that's it:

```python
@sales_bp.route("/leads/<int:id>", methods=["PUT"])
@require_permission("lead:edit")
def update_lead(id):
    ...
```

> All permissions are at `app/utils/permissions.py`

---

# TO-DO

Here you'll find a simple list that what I need to-do;

## Backend

[ ] - Module Marketing; <br>
[ ] - Module Customer Success; <br>
[ ] - Finish unit tests; <br>
[ ] - Implement to websockts to handle with pipelines changes; <br>
[ ] - Create a pipeline CI/CD to run tests each push to main branch; <br>

## Frontend

[ ] - Start the project on NextJS; <br>
[ ] - Setup the Auth and permissions; <br>
[ ] - Setup page to handle with admins subjects; <br>
[ ] - Setup page to handle with companies; <br>
[ ] - Create home page; <br>
[ ] - Create pipeline page; <br>
[ ] - Implement to websockts to handle with pipelines changes; <br>
[ ] - Create leeds page; <br>
[ ] - Create clients page; <br>
[ ] - Create contacts page; <br>
[ ] - Create deals page; <br>
[ ] - Create a pipeline CI/CD to run tests each push to main branch; <br>

---

# Contacts

LinkedIn: [@fabioacarvalho](https://linkedin.com/in/fabioacarvalho) <br>
Medium: [@fabioacarvalho](https://medium.com/@fabioacarvalho)