import json
import os

class Contact:
    def user_input():
        name = input("Enter Name: ")
        mobile = int(input("Enter Mobile Number: "))
        email = input("Enter Email ID: ")

        info = {
            "name":name,
            "mobile": mobile,
            "email": email
        }
        
        Contact.store(info)

    def store(info):
        if os.path.exists("data.json"):
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                data = []
        else:
            data = []
        
        if info not in data:
            data.append(info)

        with open("data.json", "w") as f:
            json.dump(data, f, indent= 4)
        
        print("Data Stored Successfully")

    def display_contact():
        try:
            if os.path.exists("data.json"):
                with open("data.json", "r") as f:
                    data = json.load(f)
                    
                    print("\n==============================================\n")
                    for k, v in data[-1].items():
                            print(f"{k.capitalize()}: {v}")
                    print("\n==============================================\n")
            
            else:
                print("FileNotFound: Please check if the file exists")
        
        except Exception as e:
                print(e)    
    

class ContactBook:
    def add_contact():
        Contact.user_input()
        print("Contact Added Successfully.")
        option = input("Do you want to view added contact?  ")
        if option.lower().strip() == "yes":
            Contact.display_contact()
    
    def view_contacts():
        try:
            if os.path.exists("data.json"):
                with open("data.json", "r") as f:
                    data = json.load(f)
                    
                    for i in data:
                        for k, v in i.items():
                            print(f"{k.capitalize()}: {v}")
                        print("\n==============================================\n")
            
            else:
                print("FileNotFound: Please check if the file exists")
        
        except Exception as e:
                print(e)  

    def search_contact(name):
        try:
            if os.path.exists("data.json"):
                with open("data.json","r") as f:
                    data = json.load(f)
                    for i in data:
                        if i["name"] == name:
                            for k, v in i.items():
                                print(f"{k.capitalize()}: {v}")
                            return
                        
                    print("Contact Not Found!")

        except Exception as e:
            print(e)

    def delete_contact(name):
        try:
            if os.path.exists("data.json"):
                with open("data.json","r") as f:
                    data = json.load(f)
                    for i in data:
                        if i["name"] == name:
                            data.remove(i)
                            with open("data.json", "w") as f:
                                json.dump(data, f, indent=4)
                            print("Contact Deleted")
                            return
                    print("Contact Not Found!")

        except Exception as e:
            print(e)

    def update_contact(name):
        try:
            if os.path.exists("data.json"):
                with open("data.json", "r") as f:
                    data = json.load(f)

                for i in data:
                    if i["name"].lower() == name.lower():
                        print("Current Details:")
                        for k, v in i.items():
                            print(f"{k.capitalize()}: {v}")

                        new_name = input("Enter New Name: ")
                        new_mobile = int(input("Enter New Mobile Number: "))
                        new_email = input("Enter New Email ID: ")

                        i["name"] = new_name
                        i["mobile"] = new_mobile
                        i["email"] = new_email

                        with open("data.json", "w") as f:
                            json.dump(data, f, indent=4)

                        print("Contact Updated Successfully")
                        return

                print("Contact Not Found!")

        except Exception as e:
            print(e)


def main_program():
    print("==========================================================================================")
    print("Welcome to contact Book")
    print("==========================================================================================")

    while(True):
        print("\n\nSelect from the below options")
        print("==========================================================================================")
        print("1. Add Contact")
        print("2. View All Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        print("==========================================================================================")

        choice = int(input("Enter Your Choice: "))
        
        contact = ContactBook

        if choice == 1:
            contact.add_contact()
        elif choice == 2:
            print("\n==============================================\n")
            contact.view_contacts()
        elif choice == 3:
            name = input("Name of contact you want to view: ")
            contact.search_contact(name)
        elif choice == 4:
            name = input("Name of contact you want to delete: ")
            contact.delete_contact(name)
        elif choice == 5:
            name = input("Name of contact you want to update: ")
            contact.update_contact(name)
        elif choice == 6:
            break

main_program()