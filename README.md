# 💼 Employee Expense Tracker — SQL + Streamlit

An interactive **data-driven dashboard** built using **Streamlit** and **MySQL**.  
This project visualizes employee expenses across departments and provides real-time analytics — demonstrating the integration of SQL-based backends with modern data visualization frameworks.

---

## ⚙️ Features

- Relational **MySQL database schema** (`employees`, `expenses`)
- SQL joins, aggregation, and CRUD operations
- Interactive **Streamlit dashboard**
- Department-wise expense analytics (bar chart + summary)
- Dynamic data filters and metrics cards
- Secure `.env`-based credential management (no hardcoded passwords)

---

## 🧰 Tech Stack

| Layer | Tools |
|-------|-------|
| **Frontend** | Streamlit |
| **Backend** | Python, SQLAlchemy |
| **Database** | MySQL (XAMPP) |
| **Utilities** | Pandas, PyMySQL, dotenv |

---

## 🗂️ Folder Structure
```text
employee-expense-tracker-dashboard/
│
├── app.py # Streamlit dashboard
├── employee_expense_tracker.sql # Exported MySQL database
├── .env # Environment variables (not pushed to GitHub)
├── .gitignore
├── requirements.txt
├── README.md
└── screenshots/
├── dashboard-summary.png
├── expenses-table.png
└── filter-view.png
```

yaml
Copy code

---

## 🧾 Database Setup (MySQL)

1. Open **phpMyAdmin** or **MySQL CLI**
2. Create a new database:
   ```sql
   CREATE DATABASE expense_tracker;
Import the provided file employee_expense_tracker.sql

via phpMyAdmin → Import tab → Select file → Go
or

via terminal:

bash
Copy code
mysql -u root -p expense_tracker < employee_expense_tracker.sql
🔒 Environment Configuration
Before running, create a .env file in the project root:

ini
Copy code
DB_USER=root
DB_PASS=yourpassword
DB_HOST=localhost
DB_NAME=expense_tracker
⚠️ Never commit .env to GitHub!
It’s already added to .gitignore.

🚀 Run Locally
1️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
2️⃣ Run the Streamlit app
bash
Copy code
streamlit run app.py
Then open http://localhost:8501

📊 Dashboard Preview
🏠 Dashboard Summary

📋 Expenses Table

🔍 Filter View

🧠 Key Learning Outcomes
✅ Relational database schema design
✅ SQL joins, aggregations, and data filtering
✅ Secure backend connection handling via .env
✅ Interactive frontend visualization with Streamlit

🧾 Author
Koushik Yadagiri
📍 Hyderabad, India
🔗 LinkedIn
💻 GitHub

⭐ If you found this project helpful, don’t forget to star the repository!

---

### 💡 Next Steps
- Add this `README.md` to your repo root.  
- Commit and push it:
  ```bash
  git add README.md
  git commit -m "Added final project README with screenshots and .env setup"
  git push origin main
