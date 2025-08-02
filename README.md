# 🧠 QuickDesk - Smart Helpdesk Ticketing System  
*Efficient. Scalable. Built for the Enterprise.*

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?style=flat-square&logo=django)
![Status](https://img.shields.io/badge/Project-Odoo%20Hackathon%202025-blueviolet?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 🔍 Overview

**QuickDesk** is a modular, role-based Helpdesk Ticketing System tailored for SMEs and enterprise teams looking for a streamlined solution to manage internal and external support queries. Developed during the **Odoo Hackathon 2025**, it is a modern Django-based solution with a future-ready foundation for AI, analytics, and ERP integration.

---

## 💡 Problem Statement

In growing organizations, traditional helpdesk systems often:

- Lack user-role distinction and automation
- Provide limited ticket lifecycle transparency
- Are difficult to scale and extend into other systems (ERP/CRM)

---

## ✅ Our Solution

QuickDesk delivers a centralized platform for:

- 📥 Submitting, managing, and collaborating on support tickets
- 👤 Role-based views for agents, users, and admins
- 💬 Comment-driven communication per ticket
- 📊 Expandable architecture for analytics & AI recommendations

---

## 🚀 Features

- **User Roles & Auth**
  - Role-based login: `User`, `Agent`, `Admin`
  - Secure session management

- **Ticketing System**
  - Create, update, view, and track tickets
  - Attach files and select categories
  - Automated timestamp tracking

- **Comment System**
  - Threaded ticket discussions for collaboration
  - Audit trail of responses

- **Admin Panel**
  - View all tickets
  - Assign agents, manage users

- **Scalable Design**
  - Prepared for AI integration, e.g., auto-prioritization, sentiment tagging

---

## 🏗️ System Architecture
Frontend (Bootstrap + HTML Templates)
↓
Django Views (Business Logic & Routing)
↓
Models (User, Ticket, Comment)
↓
SQLite (default) / PostgreSQL (for production)

---

## 📁 Project Structure

quickdesk/
├── helpdesk/ # Core app: models, views, URLs for ticketing
├── users/ # Custom user model & roles
├── templates/ # HTML templates for UI
├── static/ # CSS/JS/assets
├── media/ # Uploaded files
├── manage.py
└── db.sqlite3

---

## 🛠️ Setup & Installation

### 🔁 Clone Repository

```bash
git clone https://github.com/your-username/quickdesk.git
cd quickdesk
```
### ⚙️ Create Virtual Environment & Install Dependencies
```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
```
🧱 Apply Migrations & Run Server
```bash
python manage.py migrate
python manage.py createsuperuser  # Create admin account
python manage.py runserver
```
👥 Roles & Permissions

| **Role**   | **Permissions**                                                             |
|------------|------------------------------------------------------------------------------|
| **User**   | - Create tickets<br>- View own tickets<br>- Add comments                    |
| **Agent**  | - View all tickets<br>- Comment on any<br>- Assist with resolution          |
| **Admin**  | - Full access<br>- View/manage all tickets<br>- Assign agents<br>- Manage users |

### 🔮Roadmap/Future Enhancements
| Feature                              | Description                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| ✅ **AI-based Ticket Prioritization** | Leverage machine learning to auto-assign priority levels based on ticket content and urgency.         |
| 📈 **Admin Analytics Dashboard**     | Visual dashboards with heatmaps, SLA tracking, ticket trends, and performance metrics.                |
| 🔔 **Email/SMS Notifications**       | Real-time notifications to users and agents on ticket creation, assignment, and updates.              |
| 🌍 **Multilingual & Accessible UI**  | Support for multiple languages and WCAG-compliant accessible design.                                  |
| 📲 **Mobile App / PWA**              | Build a Progressive Web App or dedicated mobile app for seamless ticket handling on the go.           |
| 🤝 **Odoo Module Integration**       | Integrate with Odoo ERP to enable real-time synchronization of support tickets, users, and workflows. |




