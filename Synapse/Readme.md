# 🧠 Synapse

Synapse is a personal learning and development platform built with Python.

The project is designed to support a structured journey from **Python programming → Data Analysis → Machine Learning → AI** while also tracking learning progress and projects.

> 🚧 Synapse is an actively developed project. Some features are still under development.

---

## 🎯 Project Goal

The main goal of Synapse is to create a single platform where I can:

- Learn programming concepts
- Practice through projects
- Work with real datasets
- Track my learning progress
- Build Data Analysis skills
- Learn Machine Learning
- Explore AI
- Manage personal projects

---

## 🗂️ Application Structure

Synapse is organized into several main modules:

```text
Synapse
│
├── Learning Hub
│   ├── Python
│   ├── SQL
│   └── Git
│
├── Project Hub
│   ├── My Projects
│   ├── Create Project
│   └── Project Roadmaps
│
├── Data Lab
│   ├── Load Dataset
│   ├── View Dataset
│   ├── Data Cleaning
│   └── Data Visualization
│
├── Machine Learning Lab
│   ├── Regression
│   ├── Classification
│   ├── Clustering
│   └── Model Evaluation
│
├── AI Lab
│   ├── AI Chat
│   ├── PDF Analysis
│   ├── Prompt Engineering
│   └── AI Projects
│
└── Growth Tracker
    ├── Learning Progress
    ├── Completed Projects
    ├── Skills
    └── Statistics
```

---

## 🚀 Current Features

### 📚 Learning Hub

Currently includes a Python learning roadmap covering:

- Variables
- Data Types
- Operators
- If / Else
- Loops
- Functions
- Modules
- OOP
- File Handling

Python learning progress is tracked automatically.

Progress data is stored in JSON so it can persist between sessions.

---

### 📁 Project Hub

The Project Hub allows users to:

- Create projects
- View existing projects
- Store project information
- Use predefined project roadmaps

Project data is persisted using JSON.

Example project information:

```python
{
    "name": "Expense Tracker",
    "description": "Expense tracking application",
    "technology": "Python"
}
```

---

### 📊 Data Lab

The Data Lab is currently under active development.

Implemented features include:

- Loading CSV datasets
- Viewing datasets
- Inspecting dataset information
- Checking data types
- Descriptive statistics
- Missing value detection
- Duplicate detection
- Duplicate removal
- Data normalization
- Missing value handling
- Date conversion and cleaning
- Invalid value handling

The project currently uses **Pandas** for data analysis and cleaning.

---

## 🧹 Data Cleaning

Synapse includes a practical data-cleaning workflow using Pandas.

The current workflow covers:

```text
Load Dataset
      ↓
Inspect Dataset
      ↓
Check Missing Values
      ↓
Check Duplicates
      ↓
Normalize Data
      ↓
Handle Missing Values
      ↓
Clean Dates
      ↓
Handle Invalid Values
```

The goal is to practice working with imperfect, real-world-style data rather than only clean datasets.

---

## 🛠️ Technologies

Current technologies used in the project:

- Python
- Pandas
- NumPy
- JSON
- Matplotlib

More technologies will be added as the project evolves.

---

## 🗃️ Data Persistence

Synapse currently uses JSON files for persistent application data.

Examples:

```text
progress.json
projects.json
```

This allows learning progress and project information to remain available after restarting the application.

---

## 🗺️ Roadmap

### Phase 1 — Python Foundation

- [x] Variables
- [x] Data Types
- [x] Operators
- [x] If / Else
- [x] Loops
- [x] Functions
- [x] Modules
- [x] OOP
- [x] File Handling

### Phase 2 — Application Structure

- [x] Main Menu
- [x] Learning Hub
- [x] Project Hub
- [x] Data Lab
- [x] Machine Learning Lab
- [x] AI Lab
- [x] Growth Tracker
- [x] Navigation system

### Phase 3 — Progress & Projects

- [x] Learning progress tracking
- [x] JSON persistence
- [x] Project creation
- [x] Project storage
- [x] Project roadmaps

### Phase 4 — Data Analysis

- [x] Load datasets
- [x] Inspect datasets
- [x] Data cleaning
- [x] Missing value handling
- [x] Duplicate handling
- [x] Data normalization
- [x] Date cleaning
- [ ] Data visualization
- [ ] Exploratory Data Analysis

### Phase 5 — Machine Learning

- [ ] Regression
- [ ] Classification
- [ ] Clustering
- [ ] Model evaluation
- [ ] Model comparison
- [ ] ML projects

### Phase 6 — AI

- [ ] AI Chat
- [ ] PDF Analysis
- [ ] Prompt Engineering
- [ ] AI Projects
- [ ] AI integrations

### Phase 7 — Growth Tracker

- [ ] Learning statistics
- [ ] Skill tracking
- [ ] Project statistics
- [ ] Progress dashboard

---

## 📈 Learning Path

The long-term learning path of Synapse is:

```text
Python
   ↓
Data Analysis
   ↓
Machine Learning
   ↓
Artificial Intelligence
```

The project itself is also being used as a practical way to learn these technologies.

---

## 💡 Philosophy

Synapse is not only a software project.

It is also a learning project.

Instead of learning concepts only through theory, the goal is to learn by:

**Learning → Building → Breaking → Debugging → Improving**

The application will evolve together with my programming skills.

---

## 🔮 Future Plans

Future versions of Synapse may include:

- Better data visualization
- Interactive dashboards
- Machine learning experiments
- AI-powered learning tools
- Automated progress analysis
- More advanced project management
- Improved user interface
- More persistent application data
- Real-world datasets and projects

---

## 📌 Project Status

**Status:** 🚧 Active Development

Synapse currently has a functional application structure, Python learning system, project management system, JSON persistence, and an actively developing Data Lab.

The next major focus is **Data Visualization and Exploratory Data Analysis**.

---

## 👨‍💻 About

Synapse is being developed as part of my journey toward becoming a:

**Python Developer → Data Analyst → Machine Learning Engineer → AI Developer**

The project is continuously evolving as I learn new concepts and apply them directly to the application.