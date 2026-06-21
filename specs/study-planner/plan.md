# Study Planner (Spec)

## 🎯 Objective
Build a simple AI-assisted study planner that helps students:
- Plan daily/weekly study tasks
- Track progress
- Stay consistent with goals

---

## 🧩 Core Features

### 1. Daily Plan Generator
- Input: subjects, available time
- Output: structured study schedule for the day

### 2. Task Management
- Add tasks (subject, topic, deadline)
- Mark tasks as completed
- View pending tasks

### 3. Weekly Overview
- Show progress summary
- Highlight incomplete tasks

### 4. Smart Suggestions (Optional AI layer)
- Suggest what to study next based on backlog
- Prioritize weak topics

---

## 🗂️ Data Model (Simple)

### Task
- id
- title
- subject
- status (pending/completed)
- due_date

---

## 🛠️ Tech Notes
- Frontend: Streamlit / Web UI
- Storage: JSON or local file (later DB)
- Optional: AI agent for planning logic

---

## 🚀 Future Improvements
- Calendar integration
- Notifications
- Performance analytics