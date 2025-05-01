# 🛒 Checkout-Kata

A full-stack application that simulates a supermarket checkout system. Users can view products, add them to the cart, apply discounts, and calculate the total cost dynamically.

---

## 📦 Tech Stack

- **Backend:** Django (DRF)
- **Frontend:** React.js
- **Database:** SQLite (default), configurable
- **API Style:** REST
- **Authentication:** Admin-only via Django Admin

---

## ✅ Requirements

Ensure the following are installed on your machine:

- Python 3.x
- Node.js and npm
- Git
- `virtualenv` (Python virtual environments)

> To install `virtualenv` on Ubuntu:
```bash
sudo apt install python3.10-venv
```
## 🔧 Backend Setup (Django)

- 1. Clone the Repository
```bash
git clone https://github.com/Rockon-collab/Checkout-Kata.git
cd Checkout-Kata
```
2. Setup Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
# OR
env\Scripts\activate     # On Windows
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Apply Migrations
```bash
python manage.py migrate
```

5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

6. Run the Server
```bash
python manage.py runserver
```

---

## 🌐 Frontend Setup (React)

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Dependencies:
```bash
npm install
```

3. Start the React App:
```bash
npm start
```

4. Run Migrations
```bash
python manage.py migrate
```

5. Create Superuser
```bash
python manage.py createsuperuser
```

6. Run the Server
```bash
python manage.py runserver 0.0.0.0:8000
```
The backend will be running at `http://localhost:8000

7. Access Admin Panel
- URL: `http://localhost:8000/admin/

---

## 🌐 Frontend Setup (React)

- 1. Navigate to the Frontend Directory
```bash
cd frontend
```

2. Install Dependencies
```bash
npm install
```

3. Start the React Application
```bash
npm start
```

---
## Directory Flow
```bash
Checkout-Kata/
│
├── CheckoutKata/              # Backend Django Project
│   ├── manage.py
│   ├── requirements.txt       # Dependencies for backend
│   └── ...
│
├── checkout_kata_frontend/    # React frontend
│   ├── package.json
│   ├── public/
│   ├── src/
│   └── ...
└── README.md
```
