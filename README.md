# MINI-CRM 

This is the second personal project that I built only using python to solidify my understanding in the language. This is a CLI App that is usefull for freelancers.
It is designed to help freelancers to track their projects, manage clients, and manage their finances. 


## Features of the app

<img width="679" height="173" alt="Screenshot 2025-11-22 at 9 12 57 PM" src="https://github.com/user-attachments/assets/ae8fe88b-6325-4be6-90ae-47a6c97b8756" />

This is a CRUD app that has CRUD operations functionality for each objects of the system (Clients, Projects, Invoices) in the app. The main fucntionality is:

    1. Managing Clients
    2. Managing Projects
    3. Creating Invoices
    
## Instalation 

Python 3.8+ is required

Clone the repo and head to the folder.

    git clone https://github.com/kanofiadmasu/Mini-CRM
    cd Mini-CRM
    
## Usage 

Once installed, simply run the file and you can interact with the software easily. 

When running on the terminal, there will be an option to select which object to manage, either Clients, Projects, or, Invoices. After selecting one you can do full CRUD opretions on them. 

If For Example we selected to manage Clients and add a new clients, an option for a CRUD will be prompted 

<img width="725" height="177" alt="Screenshot 2025-11-22 at 9 24 10 PM" src="https://github.com/user-attachments/assets/7d77878b-0ce1-4158-a270-e9e447f02fba" /> 

**after we select to manage client and add a new client a series of prompts will asked for the data regarding the client to add the client** 

<img width="681" height="282" alt="Screenshot 2025-11-22 at 9 26 08 PM" src="https://github.com/user-attachments/assets/4a571d30-f6a7-4e78-a9f0-e1cd4f08deea" />

Therefore, a new client will be added on the clients file and will be saved there.

<img width="808" height="59" alt="Screenshot 2025-11-22 at 9 30 47 PM" src="https://github.com/user-attachments/assets/ea2a0e14-774e-4877-bc38-cfea6af530ba" />

## Project Structure 

    
    Mini-CRM/
    │
    ├── crm.py      # Main CLI script
    ├── clients.txt         # Saved Clients
    ├── projects.json       # Saved Projects
    ├── invoices.json       # Saved Invoices
    ├── README

## Learning Outcomes 

This project taught me a lot of new concepts in python and also industry standard concepts like software development cycle, design flows, planning software before building it and technical lessons like function dispatching, some design patterns(extensible design pattern), and many more concpets.  

Concepts/Things I learned From this project

        1. Debbuging --> Since the codebase was getting larger, I was getting a lot of errors, thus I was forced to learn to find errors and the one I found extremly hard I used AI to debug.
        2. Modularize  --> Assigning specific part of the code for specific task.
        3. Reuseblity --> Since this app was a CRUD app there was a lot of things that repeats. For that reason I got into the habit of building things that I can reuse mulitple times. 

Generally, there are a lot of other important concepts that I learned from doing this project. 
        

## Contributing 

1. Fork the repo
2. Add or improve features, report an issue or a bug
3. Open a pull request

## License







   


 
