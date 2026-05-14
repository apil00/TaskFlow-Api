TaskFlow is a project management and team productivity tool.

# Tech stack:
- Python Django
- Django Rest Framework
- SQlite
- django-environ

# Setup instruction

1. Clone the repository
   ```bash
   git clone https://github.com/apil00/TaskFlow-Api.git
   cd TaskFlow-Api

2. Create and activate virtual environment
    ```bash
    python -m venv venv
    venv\Scripts\activate # window
    source venv/bin/activate #macOS/linux

3. Install dependencies
    ```bash
    pip install -r requirements.txt

4. Set up environment variables
    ```bash
    cp .env.example .env
    # edit .env with your values

5. Run migrations
    ```bash
    python manage.py migrate

6. start the server
    ```bash
    python manage.py runserver


API endpoints:

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :---: |
| POST | `/api/v1/auth/register/` | Register new user | ❌ |
| POST | `/api/v1/auth/login/` | Login user | ❌ |


# Register -> Post
request body:
{
  "email": "john@example.com",
  "password": "strongpassword123",
  "first_name": "John",
  "last_name": "Doe"
}

Response(201 Created)
{
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe"
}

# Login -> Post
request body:
{
  "email": "john@example.com",
  "password": "strongpassword123"
}

Response (200 OK)
{
    "token": "generated_token",
    "user": {
        "email": "john@example.com",
        "first_name": "Jhon",
        "last_name": "Doe"
    }
}