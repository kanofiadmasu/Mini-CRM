import re 

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

'''This Functions are Under Manage Functions'''
# Client Adding Section
def add_client():
    while True:
        name = input('What is the name: ').strip()
        if name.isalpha():
            break
        print('Please, Provide the right input!')

    def is_valid_phone(phone_num):
        pattern = r'^[\+]?\d[\d\s\-]*$'
        return bool(re.match(pattern, phone_num))
        
    while True:
        phone_num = input('What is the Phone number?')
        if is_valid_phone(phone_num):
            break
        print('Please, Provide the right input!')
            
    while True:
        company = input('What is the Company name?').strip()
        if company.isalpha():
            break
        print('Company name can only include string and numbers!')
 
    notes = input('What Notes would you like to add?').strip()

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
                name, phone_num, company, notes = line.strip().split('-', 3)
                client = {
                    "name": name,
                    "phone": phone_num,
                    "company": company,
                    "notes": notes,
                }
                client_list.append(client)

                print(f'{name} | {phone_num} | {company} | {notes}')

      return client_list
    except FileNotFoundError:
        print('Could not acces file!')
          
def search_clients(client_list):
        while True: 
            key_word = input('Input the first name of the client key word for searching.')
            if key_word.isalpha():
                found = False
                for client in client_list:
                    first_name = client['name'].split()[0]
                    if first_name.lower() == key_word.lower():
                        print(f'{client["name"]} | {client["phone"]} | {client["company"]} | {client["notes"]}')
                        found = True
                if not found:
                    print('Client not found.')
                break
            else: 
                print('Only Alphabetic input is allowed!')

# So the above two functions will work together to provide the desired out come

''' Here I used helper function, becuase there was an issue 
    regarding the add_clients function -- it always shows the add
    client file input first, but the right thing should be the main
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

''' since we used helper function, we should change the options 
    for the main menu function'''

def manage_clients():

    sub_choice_mapping = { 
                1: handle_add_client,
                2: handle_view_clients,
                3: handle_search_clients,
                4: None 
                }
    
    while True: 
        sub_choices = [
                ' Add Clients',
                ' Veiw All Clients',
                ' Searching Clients',
                ' Back to Main Menu'
                ]
        
        for index, choice in enumerate(sub_choices, start=1):
            print(f'{index}: {choice}')
      
        try: 
            sub_choice_input = int(input('What Do you want to manage? '))
            action = sub_choice_mapping.get(sub_choice_input)
            if action:
                action()
            elif sub_choice_input == 4:
                break
            else:
                print('Please Choose a valid option.')

        except ValueError:
            print('Please, Provide the right input!')
            
# Main menu section 

def main_menu():
    main_function_mapping = {
        1: manage_clients,
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
            print(f'{index}: {option}')

        try: 
            choice_input = int(input('Hello, what do you want to do?'))
            action = main_function_mapping.get(choice_input)
            if action:
                action()
            else:
                print('Please, choose the right number')
        except ValueError:
            print('Please, provide the right input!')

     
main_menu()
            
