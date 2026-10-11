# 🧠 Synapse

**Synapse** is a Python-based learning and development platform designed to help learners improve their programming, data analysis, machine learning, and artificial intelligence skills through structured learning roadmaps and practical projects.

The application brings learning resources, project management, data analysis tools, machine learning exercises, AI-powered features, and progress tracking together in one place.

## 🎯 Project Goals

- Learn programming through structured learning roadmaps.
- Practice data analysis using real datasets.
- Explore fundamental machine learning algorithms.
- Integrate AI models into practical applications.
- Create and manage personal projects.
- Track learning progress and acquired skills.
- Develop a modular and maintainable Python application.

## 🏗️ Application Structure

Synapse consists of six main modules and a central navigation system.

1. Learning Hub
2. Project Hub
3. Data Lab
4. Machine Learning Lab
5. AI Lab
6. Growth Tracker

The application uses a menu-based interface to navigate between modules.

## 📚 1. Learning Hub

The Learning Hub provides structured roadmaps for learning programming and development tools.

### Python Roadmap

Topics include:

- Variables
- Data Types
- Operators
- If / Else
- Loops
- Functions
- Modules
- Object-Oriented Programming (OOP)
- File Handling

### SQL Roadmap

Topics include:

- SQL Basics
- SELECT
- WHERE
- ORDER BY
- Aggregate Functions
- GROUP BY
- JOINs
- INSERT, UPDATE, DELETE

### Git Roadmap

Topics include:

- Git Basics
- Repositories
- git add
- git commit
- git status
- git log
- Branches
- GitHub

Each roadmap provides explanations and examples to help users understand the fundamental concepts.

## 📁 2. Project Hub

The Project Hub helps users create, organize, and manage their projects.

### Features

- Create new projects.
- View existing projects.
- Explore project roadmaps.
- Store project information locally.
- Load saved projects when the application restarts.

Project information is stored in JSON files.

## 📊 3. Data Lab

The Data Lab introduces data analysis and manipulation using Python.

### Dataset Management

- Load CSV datasets using Pandas.
- Preview the first and last rows.
- Inspect dataset dimensions and columns.
- Examine data types and summary information.

### Data Cleaning

- Identify and handle missing values.
- Remove duplicate records.
- Convert columns to appropriate data types.
- Handle invalid date values.
- Clean inconsistent categorical data.

### Data Visualization

The application includes examples of:

- Bar charts
- Histograms
- Scatter plots
- Line charts

### Technologies

- Pandas
- NumPy
- Matplotlib

## 🤖 4. Machine Learning Lab

The Machine Learning Lab provides introductory exercises using Scikit-learn.

### Regression

- Prepare features and target variables.
- Split datasets into training and testing sets.
- Train a Linear Regression model.
- Generate predictions.
- Evaluate model performance using R².

### Classification

- Prepare numerical features and categorical targets.
- Train a Logistic Regression model.
- Predict class labels.
- Evaluate classification performance.

### Clustering

- Standardize numerical features.
- Apply the K-Means clustering algorithm.
- Assign observations to clusters.

### Model Evaluation

The application demonstrates common classification metrics:

- Accuracy
- Precision
- Recall
- F1-score

**Note:** The current machine learning exercises use a small dataset for educational purposes. Their results should not be considered reliable assessments of real-world model performance.

## 🧠 5. AI Lab

The AI Lab integrates Google's Gemini API to provide AI-powered learning features.

### AI Chat

- Send messages to an AI model.
- Receive AI-generated responses.
- Maintain conversation context during a chat session.

### PDF Analysis

- Read PDF documents.
- Extract text from PDF pages.
- Ask questions about document content.
- Generate explanations and summaries using AI.

### Prompt Engineering

- Define the AI's role using system instructions.
- Customize prompts for beginner-friendly explanations.
- Request structured responses.
- Experiment with different prompting techniques.

### AI Study Assistant

- Generate explanations about selected topics.
- Create study summaries.
- Generate practice questions.

### Technologies

- Google Gen AI SDK
- Gemini API
- PyPDF

**Note:** AI features require a valid API key, an available model, and sufficient API quota. Availability and usage limits may affect functionality.

## 📈 6. Growth Tracker

The Growth Tracker provides an overview of learning progress, projects, and skills.

### Learning Progress

- Display Python learning topics.
- Show completion status for individual topics.
- Count completed topics.
- Calculate the completion percentage.

### Completed Projects

- Display completed projects.
- Handle empty project lists with an appropriate message.

### Skills

The application tracks skills such as:

- Python
- Pandas
- Data Visualization
- Machine Learning
- Gemini API

Skills currently use beginner-level labels.

### Statistics

The Statistics section summarizes information such as:

- Completed learning topics
- Completed projects
- Total skills

## 💾 Data Persistence

Synapse uses JSON files to store application data locally.

### Current Uses

- Save and load learning progress.
- Save and load project information.
- Preserve supported data between application sessions.

Separate functions are used to load and save different types of data.

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Machine learning |
| Google Gen AI SDK | Gemini API integration |
| PyPDF | PDF text extraction |
| JSON | Local data persistence |
| Git | Version control |
| GitHub | Remote repository hosting |

## ▶️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Replace `<your-repository-url>` with the URL of your GitHub repository.

### 2. Navigate to the Project Directory

```bash
cd <project-directory>
```

Replace `<project-directory>` with the actual name of your project folder.

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install pandas numpy matplotlib scikit-learn pypdf google-genai
```

It is recommended to use a virtual environment to keep project dependencies isolated.

### 4. Configure the Gemini API Key

Set the `GEMINI_API_KEY` environment variable before using the AI features.

On macOS or Linux:

```bash
export GEMINI_API_KEY="your-api-key"
```

Replace `your-api-key` with your own API key.

**Security:** Never commit API keys, passwords, or other sensitive information to GitHub.

### 5. Run the Application

Run the main Python file:

```bash
python3 main.py
```

Replace `main.py` with the actual filename of your application's entry point if it is different.

## 🗺️ Development Roadmap

### Implemented Features

- [x] Main menu and navigation
- [x] Python learning roadmap
- [x] SQL learning roadmap
- [x] Git learning roadmap
- [x] Project creation and listing
- [x] Project roadmaps
- [x] Dataset loading and inspection
- [x] Data cleaning exercises
- [x] Data visualization examples
- [x] Regression
- [x] Classification
- [x] Clustering
- [x] Model evaluation
- [x] AI Chat
- [x] PDF Analysis
- [x] Prompt Engineering
- [x] AI Study Assistant
- [x] Learning progress tracking
- [x] Skills overview
- [x] Growth statistics
- [x] JSON-based data persistence
- [x] Basic navigation tests
- [x] Basic persistence tests
- [x] Empty-data handling

### Planned Improvements

- [ ] Improve error handling for missing or invalid JSON files.
- [ ] Strengthen input validation across menus.
- [ ] Refactor repetitive code where appropriate.
- [ ] Expand progress tracking to cover additional learning roadmaps.
- [ ] Improve skill management.
- [ ] Add more comprehensive application tests.
- [ ] Improve dependency management and setup documentation.
- [ ] Continue improving the user experience.

## 📌 Current Status

**Status: In Development**

Synapse currently includes learning roadmaps, project management, data analysis tools, introductory machine learning exercises, AI-powered learning features, and progress tracking.

The next development phase focuses on error handling, code quality, testing, and overall application reliability.

## 💡 Project Philosophy

Synapse is built around the idea that learning programming becomes more effective through structured topics, practical exercises, experimentation, and continuous progress tracking.

The long-term goal is to develop Synapse into a more complete personal learning and development platform.

## 👨‍💻 Author

Developed as a personal project to practice and improve skills in Python, data analysis, machine learning, and artificial intelligence.