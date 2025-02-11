
data_storage = [{"Name": "Jesu", "Phone_no": "09015535558", "Favourite": True}]

def add_contact():
    contact_details = {}
    contact_name = input("Enter the contact name: ")
    phone_number = input("Enter the phone number: ")
    set_favourite = input("Select Yes or No to add this contact as favourite: ").lower().strip()

    contact_details["Name"] = contact_name
    contact_details["Phone_no"] = phone_number
    
    if set_favourite == "yes":
        contact_details["Favourite"] = True
    
    if set_favourite == "no":
        contact_details["Favourite"] = False
    
    data_storage.append(contact_details)

    return "Contact added successfully"

def view_contacts():
    for index, contact in enumerate(data_storage):
        print(f" {index + 1} -- {contact}")
    
    return""
    
def update_contact(phone_number):
        
        def update_contact_name(updated_contact_name):
            contact["Name"] = updated_contact_name
        
        def update_phone_no(updated_phone_no):
            contact["Phone_no"] = updated_phone_no

        def update_all_details(all_new_updated_name, all_new_updated_no):

            contact["Name"] = all_new_updated_name
            contact["Phone_no"] = all_new_updated_no


# Update Operations

        for contact in data_storage:
            if contact["Phone_no"] == phone_number:
                
                print(f"current details: {contact}")
                while True:

                    print('''
                            
SELECT 1 to Update the contact name
SELECT 2 to Update the phone number
SELECT 3 to Update all
SELECT 4 to Quit
                            
''')
                    update_selection = input("Select an operation from 1 - 4: ")
                    
                    if update_selection == "4":
                        break

                    if update_selection == "1":
                        new_contact_name = input("Enter the new contact name: ")
                        update_contact_name(new_contact_name)

                    elif update_selection == "2":
                        new_phone_no = input("Enter the new phone number: ")
                        update_phone_no(new_phone_no)
                    
                    elif update_selection == "3":
                        all_new_contact_name = input("Enter a new contact name: ")
                        all_new_phone_no = input("Enter a phone number: ")
                        update_all_details(all_new_contact_name, all_new_phone_no)
                    
                    else:
                        print("Only pick an option from 1 to 4.")
                    
                    return "Book Updated Successfully"

def delete_contact(phone_number):
   for index, contact in enumerate(data_storage):
        if contact["Phone_no"] == phone_number:
            data_storage.pop(index)
            return "Contact deleted!"
        return "Incorrect Phone number "
    
def search_contact(name):
    for index, contact in enumerate(data_storage):
        if contact["Name"] == name:
            return f"{index + 1} -- {contact}"
        

def mark_favourite(phone_number):
    for contact in data_storage:
        if contact["Phone_no"] == phone_number:
            if contact["Favourite"] == False:
                contact["Favourite"] = True
                return ("Contact updated successfully...")
            
            return "The contact is already your favourite"

def unmark_favourite(phone_number):
    for contact in data_storage:
        if contact["Phone_no"] == phone_number:
            if contact["Favourite"] == True:
                contact["Favourite"] = False
                return ("Contact updated successfully...")
        
            return "The contact is already not your favourite"


# Main Operations

while True:

    print('''

Select 1 to add new contact to the phone book.
Select 2 to display all the contacts in the phone book.
Select 3 to update the information of a contact given their phone number.
Select 4 to remove a contact from the phone book using their phone number.
Select 5 to search for a contact by their exact name.
Select 6 to mark a contact as a favorite.
Select 7 to unnmark a contact as a favorite.
Select 8 to quit
        

''')

    user_inputs = input("Select an Operation from 1- 8: ")

    if user_inputs == "8":
        break

    if user_inputs == "1":
        print(add_contact())

    elif user_inputs == "2":
         print(view_contacts())

    elif user_inputs == "3":
        update_search_with_phone_no = input("Enter the phone number of the contact you want to update: ")
        print(update_contact(update_search_with_phone_no))
    
    elif user_inputs == "4":
        delete_search_with_phone_no = input("Enter the phone number of the contact you want to update: ")
        print(delete_contact(delete_search_with_phone_no))
    
    elif user_inputs == "5":
        search_with_name = input("Enter the contact name you are searching for: ")
        print(search_contact(search_with_name))
    
    elif user_inputs == "6":
        mark_favourite_search = input("Enter the phone number of the contact you want to mark as your favourite: ")
        print(mark_favourite(mark_favourite_search))

    elif user_inputs == "7":
        unmark_favourite_search = input("Enter the phone number of the contact you want to unmark as your favourite: ")
        print(unmark_favourite(unmark_favourite_search))
    
    else:
        print("Error!!!... only select from 1 - 8")

