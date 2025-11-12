# Soft

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
flask db migrate
```

<br>

3 - As soon as you run migrate, do it the upgrade: <br>

```bash
flask db upgrade
```
