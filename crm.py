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

name, phone_num, company, notes = add_client()

client = Clients(name, phone_num, company, notes)
#client.save_clients()

print('\n✅ Client Added Succesfully!\n')
 
# Viewing All Clients 
def veiw_all_clients(filename='clients.txt'):
    try:
      with open(filename, 'r') as file:
        lines = file.readlines()
        if not lines:
            print('No clinets are found.')
        for line in lines:
            name, phone_num, company, notes = line.strip().split('-', 3)
            print(f'{name} | {phone_num} | {company} | {notes}')
    except FileNotFoundError:
        print('Could not acces file!')
          
def search_clients():
    pass

def manage_clients():
    def add_client(): pass
    def veiw_all_clients(): pass
    def search_clients(): pass
   
    
    sub_choice_mapping = { 
                1: add_client,
                2: veiw_all_clients,
                3: search_clients,
                4: None 
                }
    
    while True: 
        sub_choices = [
                ' Add Clients',
                ' Veiw All Clients',
                ' Searching Clients',
                ' Edit Clients',
                ' Back to Main Menu'
                ]
        
        for index, choice in enumerate(sub_choices, start=1):
            print(f'{index}: {choice}')
        sub_choice_input = int(input('What Do you want to manage'))

        try: 
            sub_choice_input = int(input('What Do you want to manage'))
            action = sub_choice_mapping.get(sub_choice_input)
            if action:
                action()
            elif sub_choice_input == 5:
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
                    ' Exit']
        
        for index, option in enumerate(main_choices, start=1):
            print(f'{index}: {option}')

        try: 
            choice_input = int(input('Hello, what do you want to do?'))
            action = main_choices.get(choice_input)
            if action:
                action()
            else:
                print('Please, choose the right number')
        except ValueError:
            print('Please, provide the right input!')

        manage_clients()
                

main_menu()
            
