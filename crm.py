from datetime import datetime
import re 
import json

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
            with open(filename, 'r') as file:    #To read and append to list if projects exist before.
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
    
    
'''This Functions are Under Manage Functions'''
# Client Adding Section
def add_client():
    while True:
        name = input('What is the name of the client? ').strip()
        if name.isalpha():
            break
        print('Please, Provide the right input!')

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
 
# Viewing All Clients 

'''Here in the function below we will both read the 
   clients and also save them in a client list for later
   use for searching'''

def veiw_all_clients(filename='clients.txt'):
    client_list = []
    try:
      with open(filename, 'r') as file:
            lines = file.readlines()
            if not lines:
                print('No clinets are found.')
            for line in lines:
                name, email, phone_num, company, notes = line.strip().split('|', 4)
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
    except FileNotFoundError:
        print('Could not acces file!')

# Searching Clients
def search_clients(client_list):
        while True: 
            key_word = input('Input the first name of the client as key word for searching.')
            if key_word.isalpha():
                found = False
                for client in client_list:
                    first_name = client['name'].split()[0]
                    if first_name.lower() == key_word.lower():
                        print(f'{client["name"]} | {client["phone"]} | {client["company"]} | {client["notes"]}')
                        found = True
                if not found:
                    print('Client not found.\n')
                break
            else: 
                print('\n Only Alphabetic input is allowed!')
# So the above two functions will work together to provide the desired out come

# Deleteing Clients
def delete_client(filename='clients.txt'):
    try:
        with open(filename, 'r') as file:
            clients_list = file.readlines()
        if not clients_list:
            print('❌No clients found to delete!')
            return 
        for index, line in enumerate(clients_list, start= 1):
            print(f'{index}, {line.strip()}')
    except FileNotFoundError:
        print('The file is not found')
        return # So that a function doesn't try to proceed with the execution

    while True:
        user_deletion_input = input('Which client would you like to delete? Choose the associated number ')
        try: 
            user_deletion_input = int(user_deletion_input)
            if 0 < user_deletion_input <= len(clients_list):
                break 
            else: 
                print('Please choose with in the range of the list')
        except ValueError:
                print('You provided the wrong value, Input the valid value')
            
    deleted_client = clients_list.pop(user_deletion_input - 1)

        #then after deletion you have to update the list so you are going 
        #to write it using write mode in python

    with open(filename, 'w') as file:
        for line in clients_list:
            file.write(line)

    print(f'✅Client deleted succecssfully:, {deleted_client.strip()} ')

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
    veiw_all_clients()

def handle_search_clients(): # Search helper function
    client_list = veiw_all_clients()
    if client_list:
        search_clients(client_list)

def handle_client_deletion():
    delete_client()

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
                ' Veiw All Clients',
                ' Searching Clients',
                ' Delete a client',
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

#Project Management section
'''Client Verfication Fucntion for adding projects'''
def client_verification(client_list): #This is helper function for the add projects function
    if  not client_list:
        print('Clients list is empty, Please add clients first!')
        return None
    
    while True:
        user_input = input('Enter client name or (type \"menu" to go back) ' ).strip()
        
        #Allowing to retunr to main menu
        if user_input.lower() == "menu":
            print('Returning to main menu...')
            return None
        
        if not user_input or user_input.isdigit():
            print('Invalid Input! Please enter the name of the client for checking!')
            continue
        #There is another function that returns the clients list

        for client in client_list: 
            if client['name'].lower() == user_input.lower():
                print('Client exists, Lets proceed to add project!')
                return client
        print('Client Not found. Try agian')

        #Add projcets function
def add_projects(client_list):
    choice = input('Add project to new client? Yes/No: ').strip().lower()
    if choice == 'yes':
        print('Please add client from main menu first.')
        return 
    elif choice == 'no':
        client = client_verification(client_list)
        if client:
            project_type_input = input('What is the Project type? ').strip() 
            #It can be anything(it can be represented with a number or anything)

            allowed_statuses = ['Not Started', 'Started', 'Completed']
            while True: 
                status_input = input('What is the status of the project? choose form').strip()
                if status_input not in allowed_statuses:
                    print('Invalid Status! Please choose from', ", ".join(allowed_statuses))
                    continue
                else: 
                    break

            while True:
                    project_deadline = input('When is the dedline?(dd/mm/yyyy) ')
                    try:
                        datetime.strptime(project_deadline, "%d/%m/%y")
                        break
                    except ValueError:
                        print('Invalid date format. Please use dd/mm/yyyy')
    else:
        print('Invalid Choice. Please enter Yes/No.')
 

    return client, project_type_input, status_input, project_deadline 


# client, project_type_input, status_input, project_deadline = add_projects(client_list)
# project = Projects(client, project_type_input, status_input, project_deadline)
# project.saving_projects()
# print('\n✅ Project Added Succesfully!\n')

def view_projects():
    pass
def update_project_status():    
    pass
def delete_project():   
    pass


def manage_projects():
    project_function_mapping = {
                1: add_projects,
                2: view_projects,
                3: update_project_status,
                4: delete_project,
                5: None
    }
    while True:
        project_choices = [
                        'Add Projects to Client',
                        'View Client Projects',
                        'Update Project Status',
                        'Delete a Project',
                        'Back to main Menu'
                        ] 
        for index, project_choice in enumerate(project_choices, start=1):
            print(f'{index}: {project_choice}\n')

        try:
            user_manage_input =  int(input('What do you want to manage in projects? '))
            action = project_function_mapping.get(user_manage_input)
            if action:
                action()
            else:
                print('Please choose the right number ')
        except ValueError:
            print('Please provide the right input! ')
            continue
        
  
    
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

main_menu()


