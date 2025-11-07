from datetime import datetime
import re 
import json
import random
import string

print('\nWelcome to the CRM system for freelancers!\n')
class Clients(): 
    def __init__(self, name, phone_num, company, notes): 
        self.name = name
        self.phone = phone_num 
        self.company = company 
        self.email = self.name + '.' + self.company + '@gmail.com'
        self.notes = notes

    def __str__(self):
        return f'{self.name} | {self.email} | {self.phone} | {self.company} | {self.notes}'
    
    def __repr__(self):
        return f'{self.name} | {self.email} | {self.phone} | {self.company} | {self.notes}'
    
    def save_clients(self, filename='clients.txt'):
        with open(filename, 'a') as client_file:
            line =  f'{self.name} | {self.email} | {self.phone} | {self.company} | {self.notes}\n'
            client_file.write(line)

'''Projects Class related to the project Sub Menu'''
class Projects: #Project adding and creation
    def __init__(self, client_name, project_type, status, deadline):
        self.client_name = client_name
        self.project = project_type
        self.status = status
        self.start_date = datetime.now().strftime('%d/%m/%Y') #Recording the time we begin the task
        self.deadline = deadline

    def __str__(self):
        return f'{self.client_name} | {self.project} | {self.status}| {self.start_date} | {self.deadline}'
    
    def saving_projects(self, filename='projects.json'):
        try: 
            with open(filename, 'r') as file:    #To read and append to the list if projects exist before.
                projects_list = json.load(file)
        except FileNotFoundError:
            projects_list = []

        projects = {
        "client_name": self.client_name,
        "project": self.project,
        "status": self.status,
        "start_date": self.start_date,
        "deadline": self.deadline
            }
        
        projects_list.append(projects)

        try:
            with open(filename, 'w') as project_file:
                json.dump(projects_list, project_file, indent=4)
        except FileNotFoundError:
            print('Couldn\'t find the file.')

        return projects_list

# Invoices Class
class Invoice:
    def __init__(self, invoice_id, client_name, project_name, amount, status, issue_date, due_date):
        self.invoice_id = random.choice(string.ascii_letters + string.digits)
        self.client_name = client_name,
        self.project_name = project_name, 
        self.amout = amount,
        self.status = stauts, 
        self.issue_date = datetime.now().strftime('%d/%m/%Y')
        self.due_date = due_date
    

# Function to check for correct name input pattern
def is_valid_pattern(user_input):
    return bool(re.match(r"^[A-Za-z0-9\s\-\']+$", user_input.strip()))
    
'''This Functions are Under Manage client Functions'''
# Client Adding Section
def add_client():
    while True:
        name = input('What is the name of the client? ').strip()
        if is_valid_pattern(name):
            break
        print('Invalid name. Please provide a correct name')
    
    def is_valid_phone(phone_num):
        pattern = r'^[\+]?\d[\d\s\-]*$'
        return bool(re.match(pattern, phone_num))
        
    while True:
        phone_num = input('What is the Phone number? ')
        if is_valid_phone(phone_num):
            break
        print('Please, Provide the right input!')
            
    while True:
        company = input('What is the Company name?').strip()
        if re.match(r'^[A-Za-z0-9\s\-]+$', company):
            break
        print('Company name can only include string, numbers, sapces, and hyphen!')
 
    notes = input('What Notes would you like to add? ')

    return name, phone_num, company, notes 

# File openeing function, main use is to modularize
def client_file_opening(filename='clients.txt'):
    """
    Opens the client file and returns a the clients. 
    We are going to use it is multiple times. 
    """
    try:
        with open(filename, 'r') as clients_file:
            clients = clients_file.readlines()

            if not clients:
                print('❌ No clients are found!')
            
        return clients
    except FileNotFoundError:
        print('❌ The file is not found! ')
        return []

# Viewing All Clients 
'''Here in the function below we will both read the 
   clients and also save them in a client list for later
   use for searching'''

def view_all_clients(clients):
    client_list = []

    # Using the returned clients file form the client_file_opening function

    for each_client in clients:
        name, email, phone_num, company, notes = each_client.strip().split('|', 4)
        client = {
            "name": name,
            "email": email,
            "phone": phone_num,
            "company": company,
            "notes": notes,
        }
        client_list.append(client)
        print(f'{name} | {phone_num} | {company} | {notes}')

    return client_list

# Searching Clients
def search_clients(clients):
    while True: 
        key_word = input('\nInput the first name of the client as key word for searching or \'q\' if you want to quit. ')

        if key_word == 'q':
            print('\n✅ Exited Successfully!')
            break

        if not key_word: 
            print('⚠️ Input is neccessary to search for a client!')
            continue

        for client in clients:
            client_name = client.split()[0].strip()
            if re.match(key_word, client_name, re.I):
                print(f'\n ✅ Client Found: {client}')
                return client_name
            
        print('❌ Client not found.\n')

# The above two functions(view-all-clients and searching) will work together to provide the desired out come
def delete_client(client_lines, filename='clients.txt'):

    for index, each_client in enumerate(client_lines, start= 1):
        print(f'{index}, {each_client.strip()}')

    if not client_lines:
        print('❌ No clinets found to delete!')
        return

    while True:
        user_deletion_input = input('Which client would you like to delete? Choose the associated number ')
        try: 
            user_deletion_input = int(user_deletion_input)
            if 0 < user_deletion_input <= len(client_lines):
                break 
            else: 
                print('⚠️ Please choose with in the range of the list')
        except ValueError:
                print('⚠️ You provided the wrong value, Input the valid value')
            
    deleted_client = client_lines.pop(user_deletion_input - 1)

        #After deletion update the list and write it on the file.

    with open(filename, 'w') as file:
        for line in client_lines:
            if not line.endswith('\n'):
                line += '\n'
            file.write(line)

    print(f'✅Client deleted successfully: {deleted_client.strip()} ')

''' Here I used helper function, becuase there was an issue 
    regarding the add_clients function -- it always shows the add
    client input request first, but the right thing should be the main
    menu ''' 

def handle_add_client(): # Add clients helper function
    name, phone_num, company, notes = add_client() 
    client = Clients(name, phone_num, company, notes) 
    client.save_clients()
    print('\n✅ Client Added Succesfully!\n')

def handle_view_clients(): # View helper function
    client_lines = client_file_opening()
    view_all_clients(client_lines)

def handle_search_clients(): # Search helper function
    clients = client_file_opening()
    search_clients(clients)

def handle_client_deletion():
    client_lines = client_file_opening()
    delete_client(client_lines)

''' since we used helper function, we should change the options 
    for the main menu function'''

def manage_clients():
    sub_choice_mapping = { 
                1: handle_add_client,
                2: handle_view_clients,
                3: handle_search_clients,
                4: handle_client_deletion,
                5: None 
                }
    
    while True: 
        sub_choices = [
                ' Add Clients',
                ' View All Clients',
                ' Search Clients',
                ' Delete a Client',
                ' Back to Main Menu'
                ]
        
        for index, choice in enumerate(sub_choices, start=1):
            print(f'{index}: {choice}\n')
      
        try: 
            sub_choice_input = int(input('What do you want to manage? Choose form the above choices! '))
            action = sub_choice_mapping.get(sub_choice_input)
            if action:
                action()
            elif sub_choice_input == 5: # Because you'll be adding a deletion features
                break
            else:
                print('Please Choose a valid option.')

        except ValueError:
            print('Please, Provide the right input!')

'''End of Managing Client Section, Next section is project managing'''

# PROJET MANAGMENT SECTION

def project_adding(client_name=None, new_client=True):
    """
    Get the inputs about the project from the user. 
    This function has to use function parametrization
    to make it reusable to add project both for existing client 
    and new client. 
    """

    # If it is new client, client_adding should be called.
    if new_client:
        name, phone_num, company, notes = add_client() 
        client = Clients(name, phone_num, company, notes) 
        client.save_clients()
        print('\n✅ Client Added Succesfully!\n')

    if client_name:
        name = client_name

    # After adding the client, proceede with adding projects. 

    while True:
        project = input('What is the project type? ')

        if not project:
            print('❌ Project can not be empty!')
            continue
        
        if not is_valid_pattern(project):
            print('⚠️ Provide a valid Project type.')
            continue
        else:
            break

    # Status Choice
    possible_status = ["Not-Started", "In Progress", "Completed"]
    while True:
        print('\nSelect the project status:')
        for index, status in enumerate(possible_status, start=1):
            print(f'\n{index}: {status}')
        status_input = input('What is the status of your project? Selcet the number From the options. ') 
        
        if not status_input:
            print('❌ Input can not be empty. Please choose from the option.')
            continue

        try:
            status_input = int(status_input)
        except ValueError:
            print('❌ Choose only from the numbers.')
            continue
        
        if status_input:
            status = possible_status[int(status_input)-1]
            break

    # Deadline
    while True:
        deadline = input('When is the deadline?(dd/mm/yyyy) ')
        try:
            datetime.strptime(deadline, "%d/%m/%Y")
            break
        except ValueError:
            print('Invalid date format. Please use dd/mm/yyyy')
    
    return name, project, status, deadline

def client_verification(): # this is just a function that reads and searchs for the client
    """
    We can use search client to find for the client, if the client is there
    we will call the Project adding function and we will, add the project to 
    the project-file as well as the client it self. 
    """
    clients = client_file_opening()
    result = search_clients(clients)
    
    if result is None:
        while True:
            user_choice = input(
            '❌ Client is not found, please add the client first! Would you like to proceede to the client? (Yes or No) '
            ).strip().lower()
            
            if not user_choice:
                print('❌ Inuput is required. Type "Yes" or "No".')
                continue

            if user_choice in ('yes', 'no'):
                if user_choice == 'yes':
                    print('✅ Proceeding to add a new client')
                    handle_project_adding(for_new=True)
                    break
                else: 
                    print('👋 Exiting project Adding')
                    break          
            else: 
                print('❌ Invalid input. Type "Yes" or "No" only.')

    else:
        print('✅ Client is found, proceeding into adding project to a client!')
    return result
    
    
def preparation_function(): 
    while True: 
        choices = ['Existing', 'New', 'Return']
        for index, choice in enumerate(choices, start= 1):
            print(f'{index} : {choice}\n')

        user_input = input('Are you adding a project to an existing or new client? Select 1 or 2. If you want to return back enter "3". ') 
        # Becuase there is one to many relation between clients and projects. 

        # validating Input
        if not user_input:
            print('\n❌ Input cannot be empty choose either Existing or New!')
            continue
        try:
            user_input = int(user_input)
        except ValueError:
            print('❌ Input can only be an integer!')
            continue 
        if user_input not in (1, 2, 3): 
            print('\n❌ Please select form the given choices! (1, 2 or 3)')
            continue 

        if user_input == 1:
            print('✅ Searching for the client.')
            client_name = client_verification()
            if client_name:
                handle_project_adding(client_name, for_new=False)
            # Searching Function, if the name exists call the adding function 
        elif user_input == 3:
            print('✅Exited Successfully!\n')
            break 
        else:
            user_choice = input('You first need to add the client? would you like to proceed(Yes/No)? ').lower().strip()
            
            if not user_choice: 
                print('❌ Input is required, choose either Yes or No!')
            
            if user_choice in ('yes', 'no'):
                if user_choice == 'yes':
                    handle_project_adding(for_new=True)
                elif user_choice == 'no':
                    print('👋 Exiting project adding.')
                break
            else:
                print('❌ You provided the wrong input. Type Yes or No.')

def handle_project_adding(client_name=None, for_new=True):
    if for_new:
        name, project, status, deadline = project_adding(new_client=True)
        projects = Projects(name, project, status, deadline)
        projects.saving_projects()
        print('\n✅ Project Added Successfully!\n')
    
    if not for_new:
        name, project, status, deadline = project_adding(client_name, new_client=False)
        projects = Projects(name, project, status, deadline)
        projects.saving_projects()
        print('\n✅ Project Added Successfully!\n')

# Project Reading Function 
def project_file_openeing(filename="projects.json"):
    try:
        with open(filename, 'r') as file:
            projects_list = json.load(file)
    except FileNotFoundError:
        print('❌The file is not found! ')

    return projects_list 

# Project Viewing Section 
def view_projects():
    """
    Reusable function for the other CRUD operations as i.e. updating and 
    deleting projects.
    """
    projects_list = project_file_openeing()
    for index, each_project in enumerate (projects_list, start=1):
        name = each_project["client_name"]
        project_type = each_project["project"]
        status = each_project["status"]
        deadline = each_project["deadline"]

        print(f'{index}: {name} | {project_type} | {status} | {deadline}')
    
    return projects_list

# Project Updating Function
def update_projects(filename="projects.json"):
    projects_list = view_projects()

    while True: 
        try:
            user_choice = int(input('\nSelect the project number you would like to update. '))

            if not user_choice:
                print('❌ Input can not be empty. Choose the number associated with the project.')
                continue

            if user_choice < 1 or user_choice > len(projects_list):
                print('❌Invlaid selection. Select from the numbers associated with the data.')
                continue

            else:
                project = projects_list[user_choice-1]
                name = project["client_name"]
                project_type = project["project"]
                status = project["status"]
                deadline = project["deadline"]
                print(f'\n✅{name} | {project_type} | {status} | {deadline}')
                print('\n')
                break
        except ValueError:
            print('⚠️ Only number is allowed as an input. ')

    # Asking which section the user would like to update. 
    update_choices = ['Client Name', 'Project Type', 'Status', 'Deadline']
    while True:
        for index, options in enumerate(update_choices, start=1):
            print(f'{index}: {options}')
    
        try:
            user_input= int(input('\nWhich section would you like to update? '))

            if not user_input:
                print('❌ Input can not be empty. Select from the possible options.')
                continue
            
            # If User input is with in this numbers, updating will continue depending on the input
            if user_input in [1, 2, 3, 4]:
                # Frist user choice
                if user_input == 1:
                    while True:
                        new_name = input('What is the new client name? ')

                        if not new_name:
                            print('❌ Input can not be empty!')
                            continue
                        
                        if not is_valid_pattern(new_name):
                            print('⚠️ Provide a valid name.')
                            continue
                        else:
                            name = new_name
                            break

                # Second user choice
                elif user_input == 2:
                    while True:
                        new_project = input('What is the new project type? ')

                        if not new_project:
                            print('❌ Project can not be empty!')
                            continue
                        
                        if not is_valid_pattern(new_project):
                            print('⚠️ Provide a valid Project type.')
                            continue
                        else:
                            project = new_project
                            break

                # Third user choice
                elif user_input== 3:
                    possible_status = ["Not-Started", "In Progress", "Completed"]
                    while True:
                        print('\nSelect the new project status:')
                        for index, valid_status in enumerate(possible_status, start=1):
                            print(f'\n{index}: {valid_status}')
                        new_status_input = input('What is the new status of your project? Selcet the number From the options. ') 
                        
                        if not new_status_input:
                            print('❌ Input can not be empty. Please choose from the option.')
                            continue

                        try:
                            new_status_input = int(new_status_input)
                        except ValueError:
                            print('❌ Choose only from the numbers.')
                            continue
                        
                        if new_status_input:
                            status = possible_status[int(new_status_input)-1]
                            break

                # Fourth user choice
                elif user_input == 4:
                    while True:
                        new_deadline = input('When is the deadline?(dd/mm/yyyy) ')
                        try:
                            datetime.strptime(new_deadline, "%d/%m/%Y")
                            deadline = new_deadline
                            break
                        except ValueError:
                            print('Invalid date format. Please use dd/mm/yyyy')
                else: 
                    print('❌ Invlaid selection. Choose only from 1-4')
                
                break  #Exit the update loop

        except ValueError:
            print('❌ Only numbers are allowed. Select from the option 1-4')

    # Update the project_list and the projects_file

    with open(filename, 'w') as file:
        json.dump(projects_list, file, indent=4)
    print(f'\n{name} | {project} | {status} | {deadline}')
    print('✅ Project updated successfully! ')

# Project Deletion Section 
def project_deletion(filename='projects.json'):
    projects_list = view_projects()

    while True:
        try:
            delete_choice = int(input('\nWhich Project would you like to delete? Select the number associated with it. '))

            if not delete_choice:
                print('❌ Input can not be empty!')
                continue

            if delete_choice < 1 or delete_choice > len(projects_list):
                print('❌Invlaid selection. Select from the numbers associated with the data.')
                continue
            else:
                break
        except ValueError:
            print('⚠️ Invalid Selection. Select only numbers.')

    deleted_project = projects_list.pop(delete_choice - 1)
    try:
        with open(filename, 'w') as file:
            json.dump(projects_list, file, indent=4)
    except FileNotFoundError:
        print('❌ Projects file not found. ')

    name = deleted_project["client_name"]
    project = deleted_project["project"]
    status = deleted_project["status"]
    deadline = deleted_project["deadline"]
    
    print(f'\n✅ Project deleted successfully: {name} | {project} | {status} | {deadline}')

def manage_projects(): 
    project_management_mapping = {
         1: preparation_function, # This is the function that calls the project_adding function depending on the condition
         2: view_projects,
         3: update_projects,
         4: project_deletion
    }

    while True:
        project_managment_choices = [
             'Add Projects',
             'View Projects',
             'Update Project',
             'Delete Project',
             'Back to Main Menu'
        ]

        for index, choices in enumerate(project_managment_choices, start=1):
            print(f'\n{index}: {choices}')

        try: 
            user_choice_input = int(input('\nWhat do you want to manage in projects? '))
            print()
            action = project_management_mapping.get(user_choice_input) 
            if action:
                action()
            elif user_choice_input == 5:
                break
            else:
                print('Please, choose the right number(1-5)')                
        except ValueError:
            print('Please, provide the right input!')
          
# Main menu section 
def main_menu():
    main_function_mapping = {
        1: manage_clients,
        2: manage_projects,
        # Here function will be mapped. For every option in the main choice
    }

    while True:
        main_choices =[ 
                    ' Manage Clients',
                    ' Manage Projects',
                    ' Create Invoices',
                    ' Record Payments',
                     ]
        
        for index, option in enumerate(main_choices, start=1):
            print(f'{index}: {option}\n')

        try: 
            choice_input = int(input('Hello, what do you want to do? '))
            action = main_function_mapping.get(choice_input)
            if action:
                action()
            else:
                print('Please, choose the right number')
        except ValueError:
            print('Please, provide the right input!')            

if __name__ == '__main__':
    main_menu() 
