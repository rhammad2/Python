# 1. Module-Level Variable (Global Scope)
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
        print(f"[{server_name}]: {SERVERS[server_name]}")


def update_server(server_name, status="Online"):
    if server_name in SERVERS:
        SERVERS[server_name] = status
        print(f"Task: Setting {server_name} to {status}...")
    else:
        print("Server not found.")


def add_server():
    new_name = input("Enter new server name: ")

    if new_name in SERVERS:
        print("That server already exists.")
    else:
        initial_state = input("Enter initial state (Online/Offline): ")
        SERVERS[new_name] = initial_state
        print(f"Added {new_name} with state {initial_state}")


def main():
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
            show_status()

        elif choice == "2":
            server_name = input("Which server name? ")
            new_status = input("Enter new status (Online/Offline): ")
            update_server(server_name, new_status)

        elif choice == "3":
            add_server()

        elif choice == "4":
            print("Exiting System. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")


# ALWAYS PUT THIS AT THE VERY BOTTOM
if __name__ == "__main__":
    main()
