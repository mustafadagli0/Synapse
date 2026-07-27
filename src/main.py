def learning_hub():
    print("Welcome to the Learning Hub!")
def project_hub():
    print("Welcome to the Project Hub!")
def data_lab():
    print("Welcome to the Data Lab!")
def machine_learning_lab():         
    print("Welcome to the Machine Learning Lab!")
def ai_lab():
    print("Welcome to the AI Lab!")
def growth_tracker():
    print("Welcome to the Growth Tracker!")  










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
        