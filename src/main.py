def learning_hub():
    while True:
        print("Welcome to the Learning Hub!")
        print("1. Python")
        print("2. SQL")
        print("3. GİT")
        print("4. Back")
        input_prompt = input("Please select an option: ")

        match input_prompt:
            case "1":
                pythonRoadMap()
            case "2":
                print("You selected Data Science.")
            case "3":
                print("You selected Machine Learning.")
            case "4":
                break
            case _:
                print("Invalid input. Please try again.")
                
def pythonRoadMap():
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
     for index,topic in enumerate(pythonTopics,start=1):
        print(f"{index}. {topic}")
     input_prompt = input("Please select an option: ")              
def project_hub():
    while True:
        print("Welcome to the Project Hub!")
        print("1. My Projects")
        print("2. Create Project")
        print("3. Project Roadmaps")
        print("4. Back")
        input_prompt = input("Please select an option: ")

        match input_prompt:
            case "1":
                print("You selected Project 1.")
            case "2":
                print("You selected Project 2.")
            case "3":
                print("You selected Project 3.")
            case "4":
                break
            case _:
                print("Invalid input. Please try again.")
def data_lab():
    while True:
            print("Welcome to the Data Hub!")
            print("1. Load Dataset")
            print("2. View Dataset")
            print("3. Data Cleaning")
            print("4. Data Visualization")
            print("5. Back")
            input_prompt = input("Please select an option: ")
    
            match input_prompt:
                case "1":
                    print("You selected Load Dataset.")
                case "2":
                    print("You selected View Dataset.")
                case "3":
                    print("You selected Data Cleaning.")
                case "4":
                    print("You selected Data Visualization.")
                case "5":
                    break
                case _:
                    print("Invalid input. Please try again.")
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
        