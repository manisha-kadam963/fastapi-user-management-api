# FastAPI User Management API

A backend API built using FastAPI for handling user authentication and management.

## 🚀 Features
- User Registration
- User Login (JWT Authentication)
- Password hashing using bcrypt
- CRUD operations
- SQLite database

## 🛠️ Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT

## 📂 Project Structure
app/
 ├── main.py
 ├── models.py
 ├── schemas.py
 ├── database.py
 ├── routes/

## ⚙️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/manisha-kadam963/fastapi-user-management-api.git
```

2. Go to folder:
```bash
cd fastapi-user-management-api
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run server:
```bash
uvicorn app.main:app --reload
```

## 🌐 API Docs
http://127.0.0.1:8000/docs

## 👩‍💻 Author
Manisha Kadam
