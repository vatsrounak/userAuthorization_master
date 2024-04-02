```
# Project Documentation - "Wyse Project"

## Project Description
The "Wyse Project" is a Django web application with Django Rest Framework and Djongo for MongoDB support, integrated with Firebase for user authentication. It provides user registration and login features and allows authenticated users to access and manage their profiles. This documentation provides an overview of the project's structure, files, and important components.

## Project Structure

```
.
├── manage.py
├── middleware
│   └── firebase_middleware.py
├── requirements.txt
├── serviceAccountKey.json
├── wyse_appDir
│   ├── admin.py
│   ├── apps.py
│   ├── db_connection.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-39.pyc
│   │       └── __init__.cpython-39.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-39.pyc
│   │   ├── apps.cpython-39.pyc
│   │   ├── __init__.cpython-39.pyc
│   │   ├── models.cpython-39.pyc
│   │   ├── serializers.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── views.cpython-39.pyc
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── wyse_projDir
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-39.pyc
    │   ├── settings.cpython-39.pyc
    │   └── urls.cpython-39.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## File Descriptions
1. `manage.py`: Django's command-line tool for managing the project.
2. `middleware/firebase_middleware.py`: Middleware to handle Firebase authentication tokens.
3. `requirements.txt`: A list of Python packages and versions required for the project.
4. `serviceAccountKey.json`: Firebase service account key for authentication.

In the `wyse_appDir` directory:
5. `admin.py`: Configuration for Django admin interface.
6. `apps.py`: Configuration for the app.
7. `db_connection.py`: Django MongoDB connection configuration.
8. `migrations/`: Directory for database schema migrations.
9. `models.py`: Django models for the project's database.
10. `serializers.py`: Serializers for the API.
11. `tests.py`: Unit tests for the app.
12. `urls.py`: URL routing for the app.
13. `views.py`: Views for API endpoints.

In the `wyse_projDir` directory:
14. `asgi.py`: ASGI application entry point.
15. `settings.py`: Django project settings.
16. `urls.py`: Project-level URL routing.
17. `wsgi.py`: WSGI application entry point.

## Getting Started
1. Make sure you have Python, Django, and Djongo installed.
2. Set up the project's database configuration in `settings.py`.
3. Configure Firebase for user authentication and update `serviceAccountKey.json`.
4. Run migrations: `python manage.py makemigrations` and `python manage.py migrate`.
5. Start the development server: `python manage.py runserver`.

## Usage
- Access the Django admin interface for user management.
- Implement API views and endpoints in `views.py`.
- Connect to the MongoDB database via Djongo in `db_connection.py`.

## Requirements
- Python
- Django
- Djongo
- Django Rest Framework
- Firebase Admin SDK

This documentation provides an overview of the "Wyse Project," including its structure and key components. Follow the provided steps to set up and run the project for user authentication and profile management.
```
