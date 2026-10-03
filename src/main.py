import math
import json
import pandas as pd

with open("progress.json", "r") as f:
    data = json.load(f)


def load_projects():
    with open("projects.json", "r") as f:
        raw_data = json.load(f)
    return raw_data.get("projects", [])


def save_projects(projects):
    with open("projects.json", "w") as f:
        json.dump({"projects": projects}, f, indent=4)


def save_progress(a):
    data["pythonProgress"][a] = True
    with open("progress.json", "w") as f:
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


def sqlRoadMap():
     print("You selected SQL Roadmap.")
def gitRoadMap():
     print("You selected GİT Roadmap.")

             
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

        for index,topic in enumerate(pythonTopics,start=1):
                  print(f"{index}. {topic} Progress: {'Completed' if data['pythonProgress'][index-1] else 'Not Completed'}")
                   
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



def project_hub():
    while True:
        print("Welcome to the Project Hub!")
        print("1. My Projects")
        print("2. Create Project")
        print("3. Project Roadmaps")
        print("4. Back")
        input_prompt = int(input("the selected option: ")
)
        FFunction=[my_projects,create_project,project_roadmaps]
        if input_prompt == 4:
            return
        FFunction[int(input_prompt)-1]()

def my_projects():
    print("You selected My Projects.")
    projects = load_projects()
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
    print("You selected Load Dataset.")
def view_dataset():
    print("You selected View Dataset.")
def data_cleaning():
    print("You selected Data Cleaning.")
def data_visualization():
    print("You selected Data Visualization.")          
def machine_learning_lab():         
     while True:
                print("Welcome to the Machine LearningHub!")
                print("1. Regression")
                print("2. Classification")
                print("3. Clustering")
                print("4. Model Evaluation")
                print("5. Back")
                input_prompt = input("Please select an option: ")
        
                match input_prompt:
                    case "1":
                        print("You selected Regression.")
                    case "2":
                        print("You selected Classification.")
                    case "3":
                        print("You selected Clustering.")
                    case "4":
                        print("You selected Model Evaluation.")
                    case "5":
                        break
                    case _:
                        print("Invalid input. Please try again.")
def ai_lab():
    while True:
                   print("Welcome to the AI Hub!")
                   print("1. AI Chat")
                   print("2. PDF Analysis")
                   print("3. Prompt Engineering")
                   print("4. AI Projects")
                   print("5. Back")
                   input_prompt = input("Please select an option: ")
           
                   match input_prompt:
                       case "1":
                           print("You selected AI Chat.")
                       case "2":
                           print("You selected PDF Analysis.")
                       case "3":
                           print("You selected Prompt Engineering.")
                       case "4":
                           print("You selected AI Projects.")
                       case "5":
                           break
                       case _:
                           print("Invalid input. Please try again.")
def growth_tracker():
    while True:
                       print("Welcome to the growth_tracker Hub!")
                       print("1. Learning Progress")
                       print("2. Completed Projects")
                       print("3. Skills")
                       print("4. Statistics")
                       print("5. Back")
                       input_prompt = input("Please select an option: ")
               
                       match input_prompt:
                           case "1":
                               print("You selected Learning Progress.")
                           case "2":
                               print("You selected Completed Projects.")
                           case "3":
                               print("You selected Skills.")
                           case "4":
                               print("You selected Statistics.")
                           case "5":
                               break
                           case _:
                               print("Invalid input. Please try again.")










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
