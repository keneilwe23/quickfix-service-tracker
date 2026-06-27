from request_manager import RequestManager

def menu():
    print("\n--- QuickFix Service Tracker ---")
    print("1. Submit Request")
    print("2. View Requests")
    print("3. Update Request Status")
    print("4. Exit")

def main():
    manager = RequestManager()

    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            name = input("Customer name: ")
            appliance = input("Appliance type: ")
            issue = input("Issue description: ")
            manager.add_request(name, appliance, issue)
            print("Request submitted!")

        elif choice == "2":
            manager.view_requests()

        elif choice == "3":
            try:
                req_id = int(input("Request ID: "))
                status = input("New status (Pending/In Progress/Completed): ")
                if manager.update_request(req_id, status):
                    print("Updated successfully!")
                else:
                    print("Request not found.")
            except ValueError:
                print("Invalid ID.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()