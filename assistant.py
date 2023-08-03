def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Invalid input. Please try again."
        except IndexError:
            return "Invalid command. Please try again."
    return inner

def greet():
    print("How can I help you?")

@input_error
def add_contact(data):
    name, phone = data.split(" ")
    contacts[name] = phone
    return f"Contact {name} with phone number {phone} added."


@input_error
def change_contact(data):
    name, phone = data.split(" ")
    contacts[name] = phone
    return f"Phone number for contact {name} updated."


@input_error
def show_phone(data):
    name = data.strip()
    return f"Phone number for {name}: {contacts[name]}"


def show_all_contacts():
    if not contacts:
        return "No contacts found."
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result


def main():
    greet()
    while True:
        command = input().lower()
        if command.startswith("hello"):
            greet()
        elif command.startswith("add"):
            print(add_contact(command[4:]))
        elif command.startswith("change"):
            print(change_contact(command[7:]))
        elif command.startswith("phone"):
            print(show_phone(command[6:]))
        elif command.startswith("show all"):
            print(show_all_contacts())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    contacts = {} 
    main()
