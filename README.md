# Chat Assistant (Django + SQLite)
A Django-based chat assistant that interacts with an SQLite database to answer user queries using natural language.

## 🚀 Features
- Supports **natural language queries** related to employees & departments.
- Uses **SQLite** for storing data.
- Handles **invalid queries** gracefully.
- Provides a **simple web interface** for interaction.

---

## 📂 Project Structure
ChatAssistant/ │── assistant/ │ │── management/commands/populate_db.py # Database seeding script │ │── models.py # Database schema │ │── views.py # Handles user queries │ │── urls.py # API endpoints │ ├── templates/index.html # Frontend UI │── ChatAssistant/ │── db.sqlite3 # SQLite database │── manage.py # Django management script │── README.md # Project documentation │── requirements.txt # Python dependencies



---

## ⚙️ **Setup & Installation**
### **Clone the Repository**

bash
git clone https://github.com/mukkamalasivakartheek/Ajackus_Task.git
cd chat-assistant

pip install -r requirements.txt
python manage.py makemigrations assistant
python manage.py migrate
python manage.py populate_db
python manage.py runserver

Visit http://127.0.0.1:8000/assistant/ #to access the assistant.

Employees
ID	Name	Department	Salary	Hire Date

Departments
ID	Name	Manager

Tests
Get All Employees in a Department
Show me all employees in the Sales department.
Show me all employees in the Engineering department.
Show me all employees in the Marketing department.

Get Manager of a Department
Who is the manager of the Sales department?
Who is the manager of the Engineering department?
Who is the manager of the Marketing department?

Get Employees Hired After a Specific Date
List all employees hired after 2021-01-01.
List all employees hired after 2022-01-01.
List all employees hired after 2023-01-01.

Get Total Salary Expense for a Department
What is the total salary expense for the Sales department?
What is the total salary expense for the Engineering department?
What is the total salary expense for the Marketing department?

Invalid Queries (Handled Gracefully)
Show me all employees in the HR department.
Who is the manager of the Finance department?
Tell me something about employees.


---

### **✔ Summary**
- **`requirements.txt`** lists required dependencies.
- **`README.md`** includes **setup, test cases, database schema, deployment, and debugging steps**.

This makes your project **easy to install, understand, and use** for anyone. 🚀🎯  

Let me know if you need further modifications! 😊


