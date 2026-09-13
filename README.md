# LostLink 🔎

A modern **Lost & Found Management System** built with **FastAPI**, **Jinja2**, HTML, CSS, and JavaScript.

LostLink allows users to report lost or found items, search through reported items, and manage their accounts through a simple authentication system.

## ✨ Features

* 🔐 User Registration & Login
* 🚪 Login / Logout with Session Authentication
* 🔒 Protected routes for authenticated users
* 🔑 Secure password hashing with Argon2
* 📦 Report lost or found items
* 🔎 Search items by:

  * Category
  * Location
  * Status
* 📝 Item CRUD operations
* 👤 Track who reported an item
* 🎨 Professional responsive UI
* ⚡ FastAPI-powered REST API
* 🖥️ Server-side rendering with Jinja2

## 🛠️ Tech Stack

| Technology                  | Purpose                 |
| --------------------------- | ----------------------- |
| Python                      | Backend                 |
| FastAPI                     | Web framework / API     |
| Jinja2                      | HTML templating         |
| HTML5                       | Structure               |
| CSS3                        | Styling                 |
| JavaScript                  | Frontend interactions   |
| Starlette SessionMiddleware | Authentication sessions |
| Pwdlib + Argon2             | Password hashing        |

## 📁 Project Structure

```text
LostLink/
│
├── main.py
│
├── templates/
│   ├── index.html
│   ├── create.html
│   ├── search.html
│   ├── login.html
│   └── register.html
│
├── static/
│   └── auth.css
│
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/JobayerProdhan/LostLink.git
cd LostLink
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn jinja2 itsdangerous "pwdlib[argon2]" python-multipart
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## 🔐 Authentication

LostLink uses session-based authentication.

### Registration

Users can create an account with:

* Username
* Password

Passwords are **hashed using Argon2** before being stored.

### Login

After successful authentication, a session is created:

```python
request.session["username"] = username
```

### Logout

Logging out clears the session:

```python
request.session.clear()
```

Protected pages redirect unauthenticated users to the login page.

## 📌 Main Routes

| Method | Endpoint           | Description           |
| ------ | ------------------ | --------------------- |
| GET    | `/`                | Homepage              |
| GET    | `/register`        | Registration page     |
| POST   | `/register`        | Create account        |
| GET    | `/login`           | Login page            |
| POST   | `/login`           | Authenticate user     |
| GET    | `/logout`          | Logout                |
| GET    | `/create`          | Create item page      |
| POST   | `/items/`          | Report an item        |
| GET    | `/search`          | Search items          |
| GET    | `/items/{item_id}` | Get specific item     |
| PUT    | `/items/{item_id}` | Update item           |
| PATCH  | `/items/{item_id}` | Partially update item |
| DELETE | `/items/{item_id}` | Delete item           |

## 🔎 Item Status

LostLink supports two item statuses:

```python
class ItemStatus(str, Enum):
    lost = "lost"
    found = "found"
```

Example item:

```json
{
    "name": "Black Wallet",
    "category": "Wallet",
    "location": "Dhaka University",
    "date": "2026-09-10",
    "description": "Black leather wallet",
    "status": "lost"
}
```

## 🔍 Search

Items can be filtered using query parameters.

Example:

```text
/search?category=Wallet
```

Multiple filters can also be used:

```text
/search?category=Wallet&location=Dhaka&status=lost
```

## 🔒 Security

LostLink currently implements:

* Password hashing with **Argon2**
* Session-based authentication
* Protected routes
* Authentication-aware navigation
* Invalid login handling

> **Note:** The current development version uses in-memory storage. User accounts and reported items will be lost when the server restarts.

## 🗺️ Future Improvements

Planned improvements include:

* [ ] PostgreSQL database
* [ ] SQLAlchemy / SQLModel integration
* [ ] Persistent user accounts
* [ ] Persistent lost & found items
* [ ] User profile page
* [ ] Image upload for items
* [ ] Email notifications
* [ ] Password reset
* [ ] Admin dashboard
* [ ] Item ownership verification
* [ ] Docker deployment
* [ ] Automated tests
* [ ] Production deployment

## 🎯 Learning Goals

This project was built to practice real-world backend development concepts including:

* FastAPI routing
* Path parameters
* Query parameters
* Request forms
* Pydantic models
* CRUD operations
* Authentication
* Password hashing
* Sessions
* Jinja2 templates
* Static files
* HTTP status codes
* API design
* Frontend/backend integration

## 👨‍💻 Author

**Jobayer Prodhan**

Mathematics graduate → Software Engineering / ML Engineering

GitHub: [JobayerProdhan](https://github.com/JobayerProdhan)

Live Link: [LostLink](https://lostlink-69xe.onrender.com/)
---

⭐ If you find this project useful, consider giving it a star!
