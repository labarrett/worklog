import datetime

#list options a) add task to file b) read file c) search through file


def ask_question():
    choice = input(" Would you like to: \nA) Add task to file \nB) Read File \nC) Search Through File \nAnswer: ").upper()
    if choice == "A":
        add_to()
    if choice == "B":
        read_file()
    if choice == "C":
        search_file()


#choice A create new file, add task to it (name of task, date, and time spent), then close

def add_to():
    task = input("Task name: ")
    intial_date = input("Date Completed — MM/DD/YY format: ")
    time_spent = input("Time spent in HH:MM: ")

    #fix date
    date = datetime.strftime(intial_date, '%m/%d/%Y')
    
    #open file    
    with open("work_log.txt", "a") as file:
    #add to file (name of task, date, and time spent)    
        file.write(task + ", " + date + ", " + time_spent + ",")

    run_script()        
    
#choice B open file, show full file

def read_file():
    #open file
    with open("work_log.txt") as file:
        print("\nWORK LOG FILE:")
        for line in file:
            print(line)
        print("****End of File
    run_script()            

#choice C search file, look by or pattern, return results that match

def search_file():
    type_of_search = input("Type of Search: \nA) General Search (String) \nB) By Pattern \nAnswer: ")
    if type_of_search == "A":
        string_field = input("What do you want to search by? ")
    if type_of_search == "B":
        pattern = input("Input regex pattern ")
    pass
    

#then close program and ask to go through options again

def run_script():
    answer = input("Would you like to start over? ").upper()
    if answer == "YES":
        ask_question()
        
#run script
ask_question()
