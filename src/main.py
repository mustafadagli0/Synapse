import math
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from google import genai
from pypdf import PdfReader
from google.genai import types

with open("progress.json", "r") as f:
    data = json.load(f)


df=None

skills=[
    {"Name":"Python ","level":"beginner"},
    {"Name":"Pandas ","level":"beginner"},
    {"Name":"Data Visualization ",   "level":"beginner "},
    {"Name":"Machine Learning ","level":"beginner "},
    {"Name":"Gemini API ","level":"beginner"}
        ]

def load_projects():
    with open("projects.json", "r") as f:
        raw_data = json.load(f)
    return raw_data.get("projects", [])

def load_progress():
    with open("progress.json") as f:
        data = json.load(f)
    return data.get("pythonProgress",[])
        
def save_projects(projects):
    with open("projects.json", "w") as f:
        json.dump({"projects": projects}, f, indent=4)
def sqlSaveProgress(a):
    with open("progressSql.json") as f:
        data=json.load(f)
    data["sqlProgress"][a]["status"]=True
    with open("progressSql.json", "w") as f:
        json.dump(data, f)
def save_progress(a):
    with open ("progress.json") as f:
        data=json.load(f)
    data["pythonProgress"][a]["status"]=True
    with open("progress.json", "w") as f:
        json.dump(data, f)
def gitSaveProgress(a):
    with open("progressGit.json") as f:
        data=json.load(f)
    data["gitProgress"][a]["status"]=True
    with open("progressGit.json", "w") as f:
        json.dump(data, f)

def learning_hub():
    while True:
        print("Welcome to the Learning Hub!")
        print("1. Python")
        print("2. SQL")
        print("3. GİT")
        print("4. Back")
        input_prompt = int(input("Please select an option: "))
        if input_prompt == 4:
            return
        functions = [pythonRoadMap, sqlRoadMap, gitRoadMap]
        functions[input_prompt - 1]()  


             
def pythonRoadMap():
     while True:
        pythonTopics=[
            "Variables",
            "Data Types",
            "Operators",
            "If / Else",
            "Loops",
            "Functions",
            "Modules",
            "OOP",
            "File Handling",
            "Back"
        ]
        
        with open("progress.json", "r") as f:
            data = json.load(f)      
        data=data["pythonProgress"]
        for index, item in enumerate(data, start=1):
            print(
                    f"{index}. Name: {item['Name']}   Progress: "
                f"{'Completed' if item['status'] else 'Not Completed'}"
            )

   
        print("9. Press for Back")
        input_prompt = input("Please select an option: ") 

        if int(input_prompt) == 10:
            return 
        Functions=[Veriables,Data_Types,Operators,If_Else,Loops,FFunctions,Modules,OOP,File_Handling]
        Functions[int(input_prompt)-1]()  
       

def Veriables():

    print("\n--- Variables ---")
    print("A variable is used to store data in Python.")
    print("You can create a variable by giving it a name and assigning a value.")  
    print("\nExample:")
    print("name = 'Ahmet'")
    print("age = 25")  
    print("\nHere, name stores a string and age stores an integer.") 
    
    name = input("\nEnter your name: ")
    print("hello "+name)  

    
    save_progress(0)

def Data_Types():
    print("\n--- Data Types ---")
    print("Python has different data types for storing different kinds of data.")

    print("\nCommon data types:")
    print("str   -> Text")
    print("int   -> Whole numbers")
    print("float -> Decimal numbers")
    print("bool  -> True or False")

    print("\nExamples:")
    print("name = 'Ahmet'      # str")
    print("age = 25            # int")
    print("height = 1.75       # float")
    print("is_student = True   # bool")

    name = input("\nEnter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in meters: "))
    print(f"Hello {name}, you are {age} years old and {height} meters tall.")

    save_progress(1)
   
def Operators():
    print("\n--- Operators ---")
    print("Operators are used to perform operations on values.")

    print("\nArithmetic operators:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("%  Modulus")

    print("\nExamples:")
    print("10 + 5 = 15")
    print("10 - 5 = 5")
    print("10 * 5 = 50")
    print("10 / 5 = 2")
    print("10 % 3 = 1")

    digit1 = float(input("\nEnter first number: "))
    digit2 = float(input("Enter second number: "))
    print(f"{digit1} + {digit2} = {digit1 + digit2}")
    print(f"{digit1} - {digit2} = {digit1 - digit2}")
    print(f"{digit1} * {digit2} = {digit1 * digit2}")
    print(f"{digit1} / {digit2} = {digit1 / digit2}")

  
    save_progress(2)

def If_Else():
    print("\n--- If / Else ---")
    print("If / Else is used to make decisions in Python.")

    print("\nExample:")
    print("age = 18")
    print("if age >= 18:")
    print("    print('You are an adult.')")
    print("else:")
    print("    print('You are not an adult.')")

    print("\nPython checks a condition and executes the appropriate block.")

    age=int(input("\nEnter your age: "))
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are not an adult.")

   
    save_progress(3)

def Loops():
    print("\n--- Loops ---")
    print("Loops are used to repeat code.")

    print("\nFor loop example:")
    print("for i in range(5):")
    print("    print(i)")

    print("\nThis prints numbers from 0 to 4.")

    print("\nWhile loop example:")
    print("count = 0")
    print("while count < 5:")
    print("    print(count)")
    print("    count += 1")

    for x in range(1,5):
        print(x)
    i=0
    while i<5:
        i=i+1
        print(i)
   
    save_progress(4)



    
def FFunctions():
    def greet():
        print("Hello, welcome to Synapse!")

    print("\n--- Functions ---")
    print("A function is a reusable block of code.")

    print("\nExample:")
    print("def greet():")
    print("    print('Hello!')")
    print("")
    print("greet()")

    print("\nFunctions help us organize and reuse code.")
    greet()
    
    save_progress(5)

def Modules():
    print("\n--- Modules ---")
    print("A module is a Python file containing code that can be reused.")

    print("\nExample:")
    print("import math")
    print("print(math.sqrt(25))")

    print("\nPython provides many built-in modules.")
    print("You can also create your own modules.")

    print("math.sqrt(25)= ", math.sqrt(25))
    print("math.pow(5, 2)= ", math.pow(5, 2))
    
    save_progress(6)


    
def OOP():
    print("\n--- Object-Oriented Programming ---")
    print("OOP is a programming approach based on objects and classes.")

    print("\nA class is like a blueprint for creating objects.")

    print("\nExample:")
    print("class Person:")
    print("    def __init__(self, name):")
    print("        self.name = name")

    print("\nOOP helps us organize larger programs.")

    class Student:
        name = "Mustafa"
        age = 21
    student = Student()    
    print(student.name)
    print(student.age)
    
    save_progress(7)

def File_Handling():    
    print("\n--- File Handling ---")
    print("File handling allows Python to read and write files.")

    print("\nWriting to a file:")
    print("with open('data.txt', 'w') as file:")
    print("    file.write('Hello Python')")

    print("\nReading a file:")
    print("with open('data.txt', 'r') as file:")
    print("    content = file.read()")

    print("\nPython can create, read and modify files.")

    with open('synapse.txt', 'w') as file:
         file.write('I am learning Python with Synapse.')
         file.close()
    with open('synapse.txt', 'r') as file:     
        print(file.read())

    
    save_progress(8)

def sqlRoadMap():
    while True:
        sqlTopics=[
            "SQL Basics",
            "SELECT",
            "WHERE",
            "ORDER BY",
            "Aggregate Functions (COUNT, SUM, AVG)",
            "GROUP BY",
            "JOINs",
            "INSERT, UPDATE, DELETE",
            "Back"
        ]
             
        with open("progressSql.json", "r") as f:
            data = json.load(f)      
        data=data["sqlProgress"]
        for index, item in enumerate(data, start=1):
            print(
                 f"{index}. Name: {item['Name']}     Progress: "
                 f"{'Completed' if item['status'] else 'Not Completed'}"
                )
     
        
        print("9. Press for Back")
        input_prompt = input("Please select an option: ") 
     
        if int(input_prompt) == 9:
            return 
        
        Functions=[sqlBasics,select,where,orderBy,aggregateFunctions,groupBy,joins,ınsertUpdateDelete]
        Functions[int(input_prompt)-1]()  
            
def sqlBasics():    
    print("\n--- SQL Basics ---")
    print("SQL stands for Structured Query Language.")
    print("SQL is used to communicate with databases.")
    print("A database is an organized collection of data.")
    print("A table stores data in rows and columns.")
    print("A row represents a single record.")
    print("A column represents a specific type of information.")

    print("\nExample:")
    print("Table: Students")
    print("ID | Name | Age")
    print("1  | Ali  | 20")
    print("2  | Ayse | 22")

    print("\nIn this example:")
    print("- Students is the table name.")
    print("- Each student is represented by a row.")
    print("- ID, Name, and Age are columns.")
    sqlSaveProgress(0)

def select():    
    print("\n--- SELECT ---")
    print("SELECT is used to retrieve data from a database.")
    print("\nExample table: Students")
    print("ID | Name  | Age")
    print("1  | Ali   | 20")
    print("2  | Ayse  | 22")
    print("3  | Mehmet| 19")

    print("\nSelect all columns:")
    print("SELECT * FROM Students;")

    print("\nSelect specific columns:")
    print("SELECT Name, Age FROM Students;")

    print("\nThe * symbol selects all columns.")
    print("You can specify column names to select particular data.")

    sqlSaveProgress(1)
def where():    
    print("\n--- WHERE ---")
    print("WHERE is used to filter records based on a condition.")

    print("\nExample table: Students")
    print("ID | Name   | Age")
    print("1  | Ali    | 20")
    print("2  | Ayse   | 22")
    print("3  | Mehmet | 19")

    print("\nSelect students older than 20:")
    print("SELECT * FROM Students WHERE Age > 20;")

    print("\nSelect a student by name:")
    print("SELECT * FROM Students WHERE Name = 'Ali';")

    print("\nCommon comparison operators:")
    print(">   Greater than")
    print("<   Less than")
    print("=   Equal to")
    print(">=  Greater than or equal to")
    print("<=  Less than or equal to")
    print("<>  Not equal to")
    sqlSaveProgress(2)
    
def orderBy():    
    print("\n--- ORDER BY ---")
    print("ORDER BY is used to sort query results.")

    print("\nExample table: Students")
    print("ID | Name   | Age")
    print("1  | Ali    | 20")
    print("2  | Ayse   | 22")
    print("3  | Mehmet | 19")

    print("\nSort by age, ascending:")
    print("SELECT * FROM Students ORDER BY Age ASC;")

    print("\nSort by age, descending:")
    print("SELECT * FROM Students ORDER BY Age DESC;")

    print("\nASC means ascending order (smallest to largest).")
    print("DESC means descending order (largest to smallest).")
    print("If you omit ASC or DESC, ascending order is used by default.")
    sqlSaveProgress(3)

def aggregateFunctions():    
    print("\n--- Aggregate Functions ---")
    print("Aggregate functions perform calculations on multiple rows.")

    print("\nExample table: Students")
    print("ID | Name   | Age")
    print("1  | Ali    | 20")
    print("2  | Ayse   | 22")
    print("3  | Mehmet | 19")

    print("\nCOUNT - Counts the number of records:")
    print("SELECT COUNT(*) FROM Students;")

    print("\nSUM - Calculates the total:")
    print("SELECT SUM(Age) FROM Students;")

    print("\nAVG - Calculates the average:")
    print("SELECT AVG(Age) FROM Students;")

    print("\nMIN - Finds the smallest value:")
    print("SELECT MIN(Age) FROM Students;")

    print("\nMAX - Finds the largest value:")
    print("SELECT MAX(Age) FROM Students;")
    sqlSaveProgress(4)

def groupBy():    
    print("\n--- GROUP BY ---")
    print("GROUP BY groups rows that have the same values.")
    print("It is often used with aggregate functions.")

    print("\nExample table: Students")
    print("ID | Name   | City")
    print("1  | Ali    | Istanbul")
    print("2  | Ayse   | Ankara")
    print("3  | Mehmet | Istanbul")
    print("4  | Zeynep | Ankara")

    print("\nCount students in each city:")
    print("SELECT City, COUNT(*)")
    print("FROM Students")
    print("GROUP BY City;")

    print("\nGROUP BY groups students by city.")
    print("COUNT(*) counts the students in each group.")
    print("The result shows the number of students in each city.")
    sqlSaveProgress(5)

def joins():    
    print("\n--- JOINs ---")
    print("JOIN is used to combine data from multiple tables.")
    
    print("\nStudents table:")
    print("ID | Name")
    print("1  | Ali")
    print("2  | Ayse")
    
    print("\nGrades table:")
    print("StudentID | Grade")
    print("1         | 90")
    print("2         | 85")
    
    print("\nINNER JOIN:")
    print("SELECT Students.Name, Grades.Grade")
    print("FROM Students")
    print("INNER JOIN Grades")
    print("ON Students.ID = Grades.StudentID;")
    
    print("\nINNER JOIN returns rows that match in both tables.")
    
    print("\nOther common JOIN types:")
    print("LEFT JOIN  - Returns all rows from the left table.")
    print("RIGHT JOIN - Returns all rows from the right table.")
    print("FULL JOIN  - Returns matching and non-matching rows from both tables.")
    sqlSaveProgress(6)

def ınsertUpdateDelete():    
    print("\n--- INSERT, UPDATE, DELETE ---")
    print("These commands are used to modify data in a database.")

    print("\n1. INSERT - Adds a new record:")
    print("INSERT INTO Students (ID, Name, Age)")
    print("VALUES (4, 'Mehmet', 21);")

    print("\n2. UPDATE - Modifies an existing record:")
    print("UPDATE Students")
    print("SET Age = 22")
    print("WHERE ID = 4;")

    print("\n3. DELETE - Removes a record:")
    print("DELETE FROM Students")
    print("WHERE ID = 4;")

    print("\nINSERT adds data.")
    print("UPDATE changes existing data.")
    print("DELETE removes data.")

    print("\nWarning: Always use WHERE carefully with UPDATE and DELETE.")
    print("Without WHERE, all records may be affected.")
    sqlSaveProgress(7)

def gitRoadMap():
    while True:
        gitTopics=[
            "Git Basics",
            "Repository",
            "git add",
            "git commit",
            "git status",
            "git log",
            "Branches",
            "GitHub",
            "Back"
           ]
           
        with open("progressGit.json", "r") as f:
            data = json.load(f)      
        data=data["gitProgress"]
        for index, item in enumerate(data, start=1):
               print(
                       f"{index}. Name: {item['Name']}    Progress: "
                   f"{'Completed' if item['status'] else 'Not Completed'}"
               )
   
      
        print("9. Press for Back")
        input_prompt = input("Please select an option: ") 
   
        if int(input_prompt) == 10:
               return 
        Functions=[gitBasics,repository,gitAdd,gitCommit,gitStatus,gitLog,branches,gitHub]
        Functions[int(input_prompt)-1]()      

def gitBasics():
    print("\n--- Git Basics ---")
    print("Git is a version control system.")
    print("It tracks changes made to files over time.")
    print("Git helps developers work on projects safely.")
    print("You can review previous changes and restore earlier versions.")
    print("\nGit and GitHub are different.")
    print("Git is a tool for tracking changes.")
    print("GitHub is an online platform for hosting Git repositories.")
    gitSaveProgress(0)

def repository():
    print("\n--- Repository ---")
    print("A repository is a place where Git tracks your project files.")
    print("It stores your files and their change history.")

    print("\nTwo common types of repositories:")
    print("1. Local Repository - Stored on your computer.")
    print("2. Remote Repository - Stored on a remote server, such as GitHub.")

    print("\nExample commands:")
    print("git init")
    print("git clone <repository-url>")

    print("\ngit init creates a new Git repository.")
    print("git clone copies an existing repository.")
    gitSaveProgress(1)

def gitAdd():
    print("\n--- Git Add ---")
    print("git add prepares changes for the next commit.")
    print("It adds changes to the staging area.")

    print("\nExample commands:")
    print("git add main.py")
    print("git add .")

    print("\ngit add main.py stages changes in main.py.")
    print("git add . stages changes in the current directory.")

    print("\nTypical workflow:")
    print("1. Modify your files.")
    print("2. Run git add.")
    print("3. Run git commit.")
    gitSaveProgress(2)

def gitCommit():
    print("\n--- Git Commit ---")
    print("A commit saves a snapshot of staged changes.")
    print("Each commit has a message describing the changes.")

    print("\nExample command:")
    print('git commit -m "Add login feature"')

    print("\nThe -m option lets you write a commit message.")
    print("A good message briefly explains what changed.")

    print("\nTypical workflow:")
    print("1. Modify your files.")
    print("2. Run git add .")
    print('3. Run git commit -m "Describe your changes"')
    gitSaveProgress(3)

def gitStatus():
    print("\n--- Git Status ---")
    print("git status shows the current state of your repository.")
    print("It tells you which files have changed.")
    print("It also shows which changes are staged or unstaged.")

    print("\nExample command:")
    print("git status")

    print("\nCommon file states:")
    print("Untracked - Git is not tracking the file yet.")
    print("Modified  - A tracked file has been changed.")
    print("Staged    - Changes are ready to be committed.")

    print("\nTip: Run git status before committing to review your changes.")
    gitSaveProgress(4)

def gitLog():
    print("\n--- Git Log ---")
    print("git log displays the commit history of a repository.")
    print("It shows previous commits and their information.")

    print("\nExample commands:")
    print("git log")
    print("git log --oneline")

    print("\ngit log shows detailed commit information.")
    print("git log --oneline displays each commit on a single line.")

    print("\nCommit history can help you understand how a project has changed.")
    gitSaveProgress(5)

def branches():
    print("\n--- Git Branches ---")
    print("A branch is a separate line of development.")
    print("Branches let you work on new features without changing the main branch.")

    print("\nExample commands:")
    print("git branch")
    print("git branch feature-login")
    print("git switch feature-login")
    print("git switch -c feature-login")

    print("\ngit branch lists your branches.")
    print("git branch feature-login creates a new branch.")
    print("git switch feature-login switches to an existing branch.")
    print("git switch -c feature-login creates and switches to a new branch.")

    print("\nBranches help developers work on features separately.")
    gitSaveProgress(6)

def gitHub():
    print("\n--- GitHub ---")
    print("GitHub is an online platform for hosting Git repositories.")
    print("It helps developers store, share, and collaborate on code.")

    print("\nCommon commands:")
    print("git remote add origin <repository-url>")
    print("git push -u origin main")
    print("git pull")

    print("\ngit remote add origin connects your local repository to a remote repository.")
    print("git push uploads your commits to the remote repository.")
    print("git pull downloads changes from the remote repository.")

    print("\nTypical workflow:")
    print("1. Create a repository on GitHub.")
    print("2. Connect your local repository.")
    print("3. Commit your changes.")
    print("4. Push your commits to GitHub.")
    gitSaveProgress(7)

def project_hub():
    while True:
        print("Welcome to the Project Hub!")
        print("1. My Projects")
        print("2. Create Project")
        print("3. Project Roadmaps")
        print("4. Back")
        input_prompt = int(input("the selected option: ").strip())
        FFunction=[my_projects,create_project,project_roadmaps]
        if input_prompt == 4:
            return
        FFunction[int(input_prompt)-1]()

def my_projects():
    print("You selected My Projects.")
    projects = load_projects()
    if len(projects)==0:
        print("You don't have any completed projects yet.")
        return
    print("My Projects:")
    for project in projects:
        techs = project.get("technologies", [])
        print(f"- {project['name']}: {project['description']}/ Technologies: {', '.join(techs) if techs else 'No technologies listed'}")


def create_project():
    print("You selected Create Project.")
    projects = load_projects()

    name = input("Enter project name: ")
    description = input("Enter project description: ")
    technologies = input("Enter technologies used (comma-separated): ").split(",")

    new_project = {
        "name": name,
        "description": description,
        "technologies": [tech.strip() for tech in technologies if tech.strip()]
    }

    projects.append(new_project)
    save_projects(projects)

def project_roadmaps():
    print("You selected Project Roadmaps.")
    print("""
    1. Python Project
       → Python Basics
       → File Handling
       → OOP
       → Project Development
    
    2. Data Analysis Project
       → NumPy
       → Pandas
       → Data Cleaning
       → Visualization""")
    
def data_lab():
    while True:
            print("Welcome to the Data Hub!")
            print("1. Load Dataset")
            print("2. View Dataset")
            print("3. Data Cleaning")
            print("4. Data Visualization")
            print("5. Back")
            input_prompt = input("Please select an option: ")
            if input_prompt == "5":
                return
            FFunctions=[load_dataset,view_dataset,data_cleaning,data_visualization]
            
            FFunctions[int(input_prompt)-1]()

            
def load_dataset():
    global df
    file_path = input("Enter the path to the CSV file: ").strip().strip("'\"")
    df=pd.read_csv(file_path)
    df.head()
    print("dataset loaded successfully.")
    
def view_dataset():
    df.head()
    df.tail()
    df.info()
def data_cleaning():
    global df
    print(df.isnull().sum())
    print(f"df.duplicated().sum(): {df.duplicated().sum()}")
    print(df.drop_duplicates())
    print(df.dtypes)
    print(df.describe())
    print(df["status"].value_counts())
    print(df["signup_date"].unique())
    df["status"] = df["status"].str.lower()
    df = df.drop_duplicates()   
    df.to_csv('/Users/mustafadagli/Desktop/python/Synapse-1/Synapse/customers-100.csv', index=False)
    print(df["age"].describe())
    df["age"]=df["age"].fillna(df["age"].median())
    print(df["income"].describe())
    df["income"]=df["income"].fillna(df["income"].mean())
    print(df["rating"].describe())
    df["rating"]=df["rating"].fillna(df["rating"].mean())
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")
    print(df["signup_date"].max())
    print(df["signup_date"].min())
    df["signup_date"] = df["signup_date"].fillna(df["signup_date"].median())
    print(df["email"].unique())
    print(df[df["email"]=="missing-email"])
    df["email"] = df["email"].replace("missing-email", np.nan)
def data_visualization():
    global df 
    a=df["city"].value_counts()       
    print(a)
    x=a.index
    y=df["city"].value_counts().values
    plt.bar(x,y)
    plt.xticks(rotation=45)
    plt.show()
    plt.close()
    print(df["age"].value_counts())
    x=df["age"]
    plt.hist(x,60)
    plt.show()
    plt.close()
    plt.scatter(df["age"],df["income"])
    plt.show()
    plt.close()
    df["signup_date"].value_counts().sort_index().plot()
    plt.xticks(rotation=45)
    plt.show()
    plt.close()
def machine_learning_lab():         
     while True:
                print("Welcome to the Machine LearningHub!")
                print("1. Regression")
                print("2. Classification")
                print("3. Clustering")
                print("4. Model Evaluation")
                print("5. Back")
                input_prompt = input("Please select an option: ")
                FFunctions=[Regression,Classification,Clustering,Model_Evaluation,]
                if input_prompt == "5":
                    return  
                FFunctions[int(input_prompt)-1]()
        
def Regression():
    X=pd.DataFrame(df["age"])
    y=pd.Series(df["income"])
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2,random_state=42
)

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = model.score(X_test, y_test)
    mea=mean_squared_error(y_test, predictions)
    print(f"Regression model accuracy: {accuracy:.2f}")
    print(model.predict([[35]]))
    print(f"{mea:.2f}")
def Classification():   
    df["status"].value_counts()
    X=df[["age","income","orders","rating"]]
    y=df["status"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train,y_train)
    predictions = model.predict(X_test)
    print(predictions)
    accuracy=model.score(X_test,y_test)
    print(f"Classificiton model accuracy:{accuracy:.2f}")

def Clustering():
    print("You selected Clustering.")
    X=df[["age","income","orders","rating"]]
    scaler=StandardScaler()
    X_scaled=scaler.fit_transform(X)
    model = KMeans(n_clusters=3,random_state=42)
    model.fit(X_scaled)
    labels=model.labels_
    print(labels)
def Model_Evaluation():
    print("You selected Model Evaluation.")  
    df["status"].value_counts()
    X=df[["age","income","orders","rating"]]
    y=df["status"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train,y_train)
    predictions = model.predict(X_test)
    precision=precision_score(predictions,y_test,pos_label="active") 
    recall = recall_score(predictions, y_test, pos_label="active")  
    f1 = f1_score(predictions,y_test, pos_label="active")
    print(precision)
    print(recall)
    print(f1)

def ai_lab():
    while True:
        print("Welcome to the AI Hub!")
        print("1. AI Chat")
        print("2. PDF Analysis")
        print("3. Prompt Engineering")
        print("4. AI Projects")
        print("5. Back")
        input_prompt = input("Please select an option: ")   
        
        if input_prompt=="5":
            return
        
        FFunctions = [aiChat,pdfAnalysis,promptEngineering,aiProjects]
        FFunctions[int(input_prompt)-1]()
client=genai.Client()
def aiChat():
    try:
        
        messages=[]

        while True: 
                message=input("enter the message: ") 
                if message=="exit":
                    break  
                messages.append(message) 
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=messages
        
                )
                messages.append(response.text)
                print(response.text)

    except Exception as e:
        print(f"Hata kodu {e}")
def pdfAnalysis():
    messages=[]
    print("PDFanalysis") 
    try:
        file_path=input("pdf dosya yolu girin: ").strip().strip("'\"")
        while True:
            message=input("Enter the message: ")
            if message=="exit":
                break
            messages.append(message)
            reader = PdfReader(file_path)
            uploaded_file=client.files.upload(file=file_path)
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=[
                    uploaded_file,
                    messages
                ]
            )
            messages.append(response.text)
            print(response.text)
    except Exception as e:
        print(f"hata kodu: {e}")
def promptEngineering():
    try:
          
        messages=[]

        while True: 
            message=input("Enter the message: ") 
            if message=="exit":
                break  
            messages.append(message) 
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=messages,
                config=types.GenerateContentConfig(system_instruction="sen python öğretmenisin ve cevap verirken sırasıyla konu,açıklama ve örnek şeklinde açıkla")
                )
            messages.append(response.text)
            print(response.text)

    except Exception as e:
     print(f"Hata kodu {e}")
def aiProjects():
    print("aiProjects")
    print("1. ia_Study_Assistant")
    print("2. Back")
    input_prompt = int(input("Please select an option: "))
    if input_prompt == 2:
        return
    if input_prompt == 1:
        ia_Study_Assistant()    

def ia_Study_Assistant():
    print("ia_Study_Assistant")
    try:
        topics=[]
        while True:
            topic=input("What is your topic?")
            if topic=="exit":
                break
            topics.append(topic)
            response=client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=topics,
                config=types.GenerateContentConfig(
                    system_instruction="sen sana verilen mesajı konu olarak algıla ve başlangıç seviyesinde açıkla maddeler şeklinde açıkla çok uzun cevap verme seçilen konu hakkında 3 pratik soru hazırla kolaydan zora doğru gitsin "
                )
            )
            topics.append(response.text)
            print(response.text)
    except Exception as e:
        print(f"Hata kodu: {e}")

def growth_tracker():
    while True:
        print("Welcome to the growth_tracker Hub!")
        print("1. Learning Progress")
        print("2. Completed Projects")
        print("3. Skills")
        print("4. Statistics")
        print("5. Back")
        input_prompt = int(input("Please select an option: "))

        if input_prompt == 5:
            return
        functions=[learningProgress,completedProjects,skills,statistics]
        functions[input_prompt-1]()

def learningProgress():
    with open("progress.json", "r") as f:
        data = json.load(f) 
    data=data['pythonProgress']
    for index,item in enumerate(data,start=1):
        print(f"{index}. {item["Name"]} STATUS: {item["status"]}")
    truedata=sum(1 for item in data if item.get("status") is True)
    print(f"completed topics: {truedata}/{len(data)}")
    print(f"Remaining topics: {len(data)-truedata}")
    overall=truedata/len(data)*100
    print(f"Overall Progress: {overall}%")
    
def completedProjects():
    data = load_projects()
    if len(data)==0:
        print("You don't have any completed projects yet.")
    for item in data:
        techs=item.get("technologies",[])
        print(f"{item["name"]}-{item["description"]}-{', '.join(techs) if techs else 'No technologies listed'}")
   
def getSkills():
    return [
        {"Name":"Python ","level":"beginner"},
        {"Name":"Pandas ","level":"beginner"},
        {"Name":"Data Visualization ",   "level":"beginner "},
        {"Name":"Machine Learning ","level":"beginner "},
        {"Name":"Gemini API ","level":"beginner"}
        ]

def skills():
    data=getSkills()
    for index,item in enumerate(data):
        print(f"Name:{data[index]["Name"]}- level:{data[index]["level"]}")

def statistics():
    data=load_progress()
    sumStatus=sum(1 for item in data if item.get("status") is True)
    print(f"Completed learning topics: {sumStatus}")
    sumProject=load_projects()
    print(f"Completed Projects: {len(sumProject)}")
    skills=getSkills()
    print(f"Total Skills: {len(skills)}")
                       


while True:

    print("1. Learning Hub")
    print("2. Project Hub")
    print("3. Data Lab")
    print("4. Machine Learning Lab")
    print("5. AI Lab")
    print("6. Growth Tracker")
    print("7. Exit")
    input_prompt = input("Please select an option: ")

    match input_prompt:
        case "1":
            learning_hub()  
        case "2":
            project_hub()
        case "3":
            data_lab()
        case "4":
            machine_learning_lab()
        case "5":
            ai_lab()
        case "6":
            growth_tracker()
        case "7":
            break
        case _:
            print("Invalid input. Please try again.")
