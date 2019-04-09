import datetime
import re
import csv

#list options a) add task to file b) read file c) search through file

def ask_question():
    choice = input(" Would you like to: \nA) Add task to file \nB) Read File \nC) Search Through File \nAnswer: ").upper()
    if choice == "A":
        add_to()
    if choice == "B":
        read_file()
    if choice == "C":
        search_file()
    else:
        print("invalid answer — quitting program")

#choice A create new file, add task to it (name of task, date, and time spent), then close
def get_date():
	# repeat all this logic until its valid.
	
    not_valid = True
    
    while not_valid:
        intial_date = input("Date Completed — MM/DD/YY format: ")
        try:           
            intial_date = datetime.datetime.strptime(intial_date, '%m/%d/%y')
            date = intial_date.strftime('%m/%d/%y')
            not_valid = False
        except ValueError:
            print("Opps! Wrong date format. Please post in MM/DD/YY format ")
            
    return date     

def add_to():
    task = input("Task name: ")
    initial_date = get_date() 

    #continue on with input
    time_spent = input("Time spent in HH:MM: ")
    notes = input("notes: ")
    
    #open file and add to file (name of task, date, and time spent)      
    with open("work_log.csv", 'a') as csvfile:
        fieldnames = ['Task', 'Date','Time_spent', 'Notes']
        filewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        filewriter.writerow({
            'Task': task,
            'Date': initial_date,
            'Time_spent': time_spent,
            'Notes': notes

            })
 
    run_script()        

#choice B open file, show full file

def read_file():
    #open file
    with open("work_log.csv", newline='') as csvfile:
        artreader = csv.reader(csvfile, delimiter = ',')
        rows = list(artreader)
        for row in rows:
            print(','.join(row))
        
    run_script()            


#choice C search file, look by or pattern, return results that match

def match_results(search):

    match_results = []

    with open("work_log.csv", newline='') as csvfile:
        artreader = csv.reader(csvfile, delimiter = ',')
        for row in artreader:
            results = re.findall(search, str(row))
            if results:
              match_results.append(row)                

    print(match_results)

    run_script()

    
def search_file():

    type_of_search = input("Type of Search: \nA) General Search (String) \nB) By Pattern \nAnswer: ")
    if type_of_search == "A":
        string_field = input("What string do you want to search by? Input date, task name, or time spent ")

        match_results(string_field)        

        
    if type_of_search == "B":
        pattern = input("Input regex pattern: ")

        match_results(pattern)  

                
#then close program and ask to go through options again

def run_script():
    answer = input("Would you like to start over? ").upper()
    if answer == "YES":
        ask_question()
        
#run script
ask_question()
