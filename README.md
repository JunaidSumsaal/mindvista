# **MindVista**

**MindVista** is a **goal-setting and productivity platform** designed to help users take control of their time, focus on meaningful tasks, and track progress effortlessly. Whether you're planning your day, setting long-term goals, or building productive habits, MindVista provides a seamless and visually intuitive workspace powered by **Django and Tailwind CSS**.

With built-in **task management, focus sessions, habit tracking, and mind mapping**, MindVista is your all-in-one productivity hub.

## **Features**

✔ **Goal Setting & Tracking** _(Set goals, define milestones, track progress)_  
✔ **Daily Planner** _(Tasks with due dates, priorities, drag-and-drop organization)_  
✔ **Focus Sessions** _(Timed work sessions, auto-tracking productivity stats)_  
✔ **Notes & Journals** _(Organized notes with linking and tagging)_  
✔ **Mind Maps & Visual Planning** _(Drag-and-drop nodes, exportable mind maps)_  
✔ **Habit Tracking** _(Track daily/weekly habits, streaks, and analytics)_  
✔ **Statistics & Reports** _(Generate insights with weekly/monthly reports)_

## **Tech Stack**

- **Backend:** Django
- **Frontend:** Tailwind CSS _(Configured in `ui/static_src/`)_
- **Database:** SQLite
- **Deployment:** Docker + Render

## **File Structure**
```bash
mindvista/
│── Dockerfile
│── manage.py
│── requirements.txt
│── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│── dashboard/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│── goals/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│── habits/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│── focus/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│── mindmaps/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│── notes/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│── reports/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│── task/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│── landing/
│   ├── __init__.py
│   ├── views.py
│── ui/
│   ├── static/
│   ├── static_src/
│   │   ├── tailwind.config.js
│   │   ├── package.json
│   │   ├── postcss.config.js
│   ├── templates/
│── .git/
│── .vscode/
│── .venv/
```

## **Setup Guide**

### ** Clone the Repository**

```bash
git clone https://github.com/JunaidSumsaal/mindvista.git
cd mindvista
```

### ** Create & Activate Virtual Environment**

```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# OR
.venv\Scripts\activate  # Windows
```

### ** Install Dependencies**

```bash
pip install -r requirements.txt
```

### ** Apply Migrations**

```bash
python manage.py makemigrations
python manage.py makemigrations django_otp
python manage.py migrate
```

### ** Create Superuser (Admin Access)**

```bash
python manage.py createsuperuser
```

### ** Run Development Server**

```bash
python manage.py runserver
```

App will be live at: **`http://127.0.0.1:8000/`**

## **Tailwind CSS Setup**

> **Tailwind configurations are inside `ui/static_src/`**

### **Option 1: Using NPM**

```bash
cd ui/static_src
npm install
```

#### **Build Tailwind Styles**

```bash
npm run dev  # For development
npm run build  # For production
```

### **Option 2: Using Django Tailwind CLI**

```bash
python manage.py tailwind install  # Install Tailwind dependencies
python manage.py tailwind start   # For development
python manage.py tailwind build   # For production
```

## **Docker Deployment on Render**

> **MindVista uses Dockerfile, as we deploy on Render**

### ** Build the Docker Image**

```bash
docker build -t mindvista .
```

### ** Run the Container Locally**

```bash
docker run -p 8000:8000 mindvista
```

## **Future Enhancements**

🔹 **AI-Powered Smart Suggestions** _(Personalized task & habit recommendations)_  
🔹 **Drag-and-Drop Task Organization** _(Seamless task reordering in planner)_  
🔹 **Customizable Themes & Dark Mode**  
🔹 **Goal Sharing & Collaboration** _(Share progress with teams & friends)_  
🔹 **Automated Habit Insights** _(AI-driven habit tracking & trends)_  
🔹 **Cross-Platform Mobile App** _(iOS & Android version in the works)_  
🔹 **Integration with Google Calendar & Notion**

## **Contributing**

We welcome contributions! Open **issues**, submit **pull requests**, and help shape **MindVista**!

## **License**

MIT License
