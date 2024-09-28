# django_crud_demo
Django, DRF, CRUD Operations

# Django DRF Project Setup

This guide will walk you through setting up a Django project with Django REST Framework.

## Prerequisites

Make sure you have Python installed on your system. You can verify this by running:

```bash
python --version
```

## Setup Instructions

1. **Create a Virtual Environment**

   Create a virtual environment to isolate your project dependencies:

   ```bash
   python -m venv _venv
   ```

2. **Activate the Virtual Environment**

   - On macOS/Linux:

     ```bash
     source _venv/bin/activate
     ```

   - On Windows:

     ```bash
     _venv\Scripts\activate
     ```

3. **Install Dependencies**

   Install Django and Django REST Framework:

   ```bash
   python -m pip install Django==4.2
   pip install djangorestframework
   ```

4. **Create a Django Project**

   Start a new Django project:

   ```bash
   django-admin startproject crud_demo
   ```

5. **Create an Application**

   Navigate into your project directory and create a new app:

   ```bash
   cd crud_demo
   python manage.py startapp items
   ```

6. **Run the Development Server**

   Run the Django development server on port `8080`:

   ```bash
   python manage.py runserver 0.0.0.0:8080
   ```

7. **Create Migrations**

   After making changes to your models, create migrations:

   ```bash
   python manage.py makemigrations
   ```

8. **Apply Migrations**

   Apply the migrations to update the database schema:

   ```bash
   python manage.py migrate
   ```

## Notes

- Make sure to activate the virtual environment every time you work on the project by running the activation command (`source _venv/bin/activate` or `_venv\Scripts\activate` for Windows).
- For production deployments, consider configuring settings such as allowed hosts, database connections, and static files.


## Super Admin Creds
- Username : admin 
- Email address: admin@email.com
- Password: admin@123