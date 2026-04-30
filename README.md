# 💸 Expense Tracker (PyQt5)

A clean and simple **desktop Expense Tracker** built using **PyQt5**.
This app lets you record, view, search, and export your expenses with a smooth UI and minimal setup.

---

## 👀 Preview

Simple, fast, and does exactly what you need —
no bloat, just tracking 💯

<img width="883" height="537" alt="image" src="https://github.com/user-attachments/assets/7b42de14-edbf-4c36-a15a-03d28b7e9cf7" />

https://github.com/user-attachments/assets/00265227-008d-4755-b82e-31d6741f88c7

---

## ✨ Features

* ➕ **Add Expenses**

  * Category, description, amount
  * Auto records date

* 📄 **View Expenses**

  * Displays all saved expenses
  * 🔍 Real-time search (category, description, or date)

* 📊 **Monthly Summary**

  * Enter month (1–12)
  * Get total expenses + breakdown

* 📤 **Export to CSV**

  * Choose where to save the file
  * Clean CSV format for Excel or analysis

* 🎨 **Modern UI**

  * Gradient background
  * Styled buttons with hover effects

---

## 🛠️ Tech Stack

* Python 🐍
* PyQt5 (GUI)
* JSON (data storage)
* CSV (export)

---

## 📁 Project Structure

```
expense-tracker/
│
├── main.py
├── expenses.ico
├── Expense Record.json (auto-created)
└── README.md
```

---

## 🚀 How to Run (Python)

### 1. Install dependencies

```bash
pip install PyQt5
```

### 2. Run the app

```bash
python app.py
```

---

## 📦 Running the EXE File (Windows)

If you downloaded the **.exe version** of the app:

1. Double-click the `.exe` file
2. If Windows shows a warning:

### ⚠️ Windows SmartScreen Warning

You may see:

> *“Windows protected your PC”*

This happens because the app is not digitally signed (common for personal projects).

👉 To run it anyway:

1. Click **More info**
2. Click **Run anyway**

✅ The app is safe if you built it yourself or downloaded it from a trusted source.

---

## 📦 Data Storage

* All expenses are saved in:

```
Expense Record.json
```

Example:

```json
[
  {
    "Category": "Food",
    "Description": "Burger",
    "Amount": 120.0,
    "Recording time": "30/04/2026"
  }
]
```

---

## 📤 CSV Export

* Click **Export to CSV**
* Choose location
* File includes:

  * Category
  * Description
  * Amount
  * Date

---

## 📜 License

MIT License.

---



