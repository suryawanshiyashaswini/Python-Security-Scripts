# 🔐 Python Security Scripts

This repository contains real-world Python scripts developed to support common Identity & Access Management (IAM) and Security Operations use cases. These scripts help automate repetitive security tasks and provide insights from user activity data — perfect for environments using Azure AD, login auditing, and compliance tracking.

> 👩‍💻 Created by **Yashaswini**  
> Security & Data Analyst | Microsoft Entra ID (Azure AD) | IAM | Python | Power BI

---

## 📌 Use Cases Covered

| Script Name | Functionality |
|-------------|----------------|
| `ad_group_audit.py` | Audits users in privileged AD groups like “Admin” |
| `failed_logins_report.py` | Filters and reports failed login attempts |
| `generate_excel_report.py` | Converts raw CSV into styled Excel sheets |
| `password_policy_checker.py` | Checks passwords against complexity rules |
| `user_account_status.py` | Flags inactive or disabled accounts for IAM clean-up |

---

## 📁 Folder Structure

Python-Security-Scripts/
├── ad_group_audit.py
├── failed_logins_report.py
├── generate_excel_report.py
├── password_policy_checker.py
├── user_account_status.py
├── requirements.txt
├── README.md
└── sample_data/
├── login_audit_sample.csv
├── ad_group_members.csv
└── user_status.csv


---

## ⚙️ How to Run the Scripts (Step-by-Step)

### ✅ Prerequisites:
- Python 3.10+ installed (with `Add Python to PATH` enabled)
- Basic knowledge of terminal (PowerShell / CMD / VSCode)

### 🧪 Setup:

```bash

# Install required libraries
python -m pip install -r requirements.txt

| Script                        | Command                             |
| ----------------------------- | ----------------------------------- |
| Admin group audit             | `python ad_group_audit.py`          |
| Failed login report           | `python failed_logins_report.py`    |
| Export login report to Excel  | `python generate_excel_report.py`   |
| Password policy validation    | `python password_policy_checker.py` |
| Inactive/Disabled user report | `python user_account_status.py`     |


▶️ Run Scripts
Script	Command
Admin group audit
python ad_group_audit.py
Failed login report
python failed_logins_report.py
Export login report to Excel
python generate_excel_report.py
Password policy validation
python password_policy_checker.py
Inactive/Disabled user report
python user_account_status.py

🧾 Sample Output: failed_logins_report.py
        User        Timestamp           SourceIP
0   john.doe   2025-07-21 09:00:00   192.168.1.10
2  ravi.kumar  2025-07-21 10:05:00   192.168.1.14
🔍 Sample Data Source Files
File	Purpose
login_audit_sample.csv	:-Contains login events and outcomes
ad_group_members.csv	:-Sample Azure AD group membership
user_status.csv	:-User status and last login data

All data is sample and mock data for demonstration purposes.

📫 Contact
🔗 LinkedIn – suryawanshiyashaswini

📧 Email: suryawanshi.yashaswini@gmail.com

🌐 GitHub: @suryawanshiyashaswini


