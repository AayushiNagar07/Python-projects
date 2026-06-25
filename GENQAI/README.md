Here’s a **professional GitHub README** you can directly copy-paste for your GenQAI project. It is structured like an internship-ready project (clean, formal, and impressive).

---

# 📌 GENQAI — AI Question Paper Generator

## 🚀 Overview

**GENQAI** is a Streamlit-based web application that helps teachers automatically generate structured question papers from a pre-defined question bank.
It allows selection of class, subject, exam type, and chapters/units, and generates a formatted question paper along with a downloadable PDF.

This project is designed as a **teacher productivity tool / ed-tech MVP**.

---

## 🎯 Features

- 🔐 Simple login system (session-based authentication)
- 📚 Select Class, Subject, Exam Type
- 🧩 Choose Units/Chapters dynamically
- ⚡ Auto question paper generation from JSON database
- 📊 Automatic total marks calculation
- 📄 Professional PDF generation (ReportLab)
- ⬇️ Download question paper as PDF
- 🧠 Structured output similar to school exam papers

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit (Python)
- **Backend Logic:** Python
- **Data Storage:** JSON-based question bank
- **PDF Generation:** ReportLab
- **State Management:** Streamlit Session State

---

## 📁 Project Structure

```
GENQAI/
│
├── app.py
├── data/
│   └── question_bank.json
├── fonts/ (optional for Unicode support)
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. User logs in
2. Selects:
   - Class (7 / 8)
   - Subject (Maths / Hindi / English)
   - Exam Type (PT-1 / Half Yearly / Final)
   - Units

3. Clicks **Generate Question Paper**
4. System:
   - Fetches questions from JSON database
   - Calculates total marks
   - Displays formatted paper

5. User downloads **PDF version**

---

## 📄 Sample Output

- Question Paper Title
- Class & Subject Info
- Exam Type
- Unit-wise Questions
- Marks per question
- Total Marks
- Downloadable PDF format

---

## 📦 Installation & Setup

```bash
git clone https://github.com/your-username/genqai.git
cd genqai
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Requirements

```
streamlit
reportlab
```

---

## 💡 Future Improvements

- 🤖 AI-based automatic question generation from textbooks (PDF input)
- 🗄️ Database integration (Firebase / Supabase)
- 👨‍🏫 Multi-teacher login system
- 🎨 Improved exam paper formatting (CBSE-style layout)
- ☁️ Cloud deployment (Streamlit Cloud / Vercel backend)

---

## 🧑‍💻 Author

**Aayushi Nagar**
BCA Student | Aspiring Full Stack Developer
Passionate about building AI + Education tools

---

## ⭐ Project Purpose

This project was built as a **real-world academic automation tool** to reduce manual effort in question paper creation and explore AI-assisted education systems.

---

## 📢 Note

This is an MVP (Minimum Viable Product) version and will be continuously improved into a full SaaS platform for teachers.

---
