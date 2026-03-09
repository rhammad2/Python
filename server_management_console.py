# Module-Level Variable (Global Scope)
SERVERS = {
    "Web_Alpha": "Online",
    "DB_Storage": "Offline",
    "Mail_Relay": "Online"
}

def display_menu():
    print("\n>>> SYSADMIN MENU <<<")
    print("1. View All Servers")
    print("2. Change Server Status")
    print("3. Add New Server")
    print("4. Exit")
    print("====================")

def show_status():
    print("\n--- CURRENT SERVER STATUS ---")
    for server_name in SERVERS:
        print(f"{server_name} : {SERVERS[server_name]}")

def update_server():
    server_name = input("Enter server name: ")

    if server_name in SERVERS:
        status = input("Enter new status (Online/Offline): ")
        print(f"Task: Setting {server_name} to {status}...")
        SERVERS[server_name] = status
    else:
        print("Server not found.")

def add_server():
    server_name = input("Enter new server name: ")

    if server_name in SERVERS:
        print("Server already exists.")
    else:
        status = input("Enter status (Online/Offline): ")
        SERVERS[server_name] = status
        print(f"Added {server_name} with state {status}")

# Jump Table (must come after functions)
JUMP_TABLE = {
    "1": show_status,
    "2": update_server,
    "3": add_server
}

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")

        if choice == "4":
            print("Exiting System. Goodbye!")
            break

        action = JUMP_TABLE.get(choice)

        if action:
            action()
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
