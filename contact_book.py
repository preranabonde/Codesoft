class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("\nContact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No contacts found.")

    def search_contact(self, search_key):
        search_results = []
        for contact in self.contacts:
            if search_key.lower() in contact.name.lower() or search_key in contact.phone_number:
                search_results.append(contact)
        if search_results:
            print("\nSearch Results:")
            for contact in search_results:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No matching contacts found.")

    def update_contact(self, search_key, new_contact):
        for contact in self.contacts:
            if search_key.lower() in contact.name.lower() or search_key in contact.phone_number:
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, search_key):
        for contact in self.contacts:
            if search_key.lower() in contact.name.lower() or search_key in contact.phone_number:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_key = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_key)
        elif choice == '4':
            search_key = input("Enter name or phone number to update: ")
            name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.update_contact(search_key, new_contact)
        elif choice == '5':
            search_key = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_key)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()