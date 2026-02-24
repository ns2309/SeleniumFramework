# Selenium Automation Framework (Python + PyTest)

## 🔥 Overview
This is a scalable Selenium automation framework built using **Python and PyTest**, designed with industry-standard practices like Page Object Model (POM), reusable fixtures, and data-driven testing.

The framework focuses on maintainability, modular design, and test reliability.

---

## 🛠 Tech Stack

- Python 3.x
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- JSON-based test data
- HTML Test Reports
- Screenshot capture on failure

---

## 📂 Project Structure
PythonSeleniumProject1/
│
├── pageobjects/ # Page classes (POM design)
├── pytestDemo/ # Test cases
├── utils/ # Browser utilities & reusable functions
├── data/ # JSON test data
├── assets/ # Static resources
├── .gitignore
└── README.md

---

## ✅ Framework Features

✔ Page Object Model implementation  
✔ Reusable PyTest fixtures (conftest.py)  
✔ Data-driven testing using JSON  
✔ Cross-browser execution support  
✔ Automatic screenshot capture on failure  
✔ HTML test reporting  
✔ Modular and scalable structure  

---

## 🚀 How To Run

### 1️⃣ Install dependencies
pip install -r requirements.txt

### 2️⃣ Run all tests
pytest -v

### 3️⃣ Run specific test file
pytest pytestDemo/test_e2eTestFramework.py -v

### 4️⃣ Generate HTML report
pytest --html=report.html --self-contained-html

---

## 📸 Failure Handling

On test failure:
- Screenshot is captured automatically
- HTML report is generated
- Logs help identify root cause quickly

---

## 🎯 Design Approach

This framework follows:

- Separation of test logic and page logic
- Single Responsibility Principle
- Reusable browser setup via fixtures
- Clean test structure for scalability

---

## 📌 Future Improvements

- CI/CD integration (GitHub Actions)
- Docker execution support
- Allure reporting
- Parallel execution with pytest-xdist

---

## 👨‍💻 Author

Nishant Sulgudle  
MS Information Technology & Analytics  
Automation & QA Enthusiast
