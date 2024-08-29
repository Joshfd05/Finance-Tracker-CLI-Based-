import json
from datetime import datetime

#Global list to store transactions
transactions = []

#File handling functions
#Load the transactions which are already written to the JSON files 
def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            return json.load(file)
    #If there is no transactions written to a JSON file, here shows an error message
    except FileNotFoundError:
        print("Can't find any transactions. Let's get started!!")
    return[]

#Save the transactions made so far into JSON file
def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent = 1)
    return[]

#Add new transactions 
def add_transaction():
    amount = input_errors("amount", "Enter the amount: ", len(transactions))
    category = input_errors("category", "Enter the category: ", len(transactions)).capitalize()
    transaction_type = input_errors("type", "Enter the type (Income/Expense): ", len(transactions)).capitalize()
    date = input_errors("date", "Enter the date (YYYY-MM-DD): ", len(transactions))
    transactions.append({"amount": amount, "category": category, "type": transaction_type, "date": date})
    print("\nTransaction saved successfully!!\n")
    save_transactions(transactions)
    print(transactions)
    return[]

#View all the transactions made so far as a list
def view_transactions():
    if transactions:
        # Iterate over the indices of transactions
        for i in range(len(transactions)):  
            # Print index and details of each transaction
            print(f"{i+1}. {transactions[i]}")  
    else:
        print("No transactions are available still!!.")    

#Update transactions that are already made as the user's choice
#If there is no any transactions so far, this would print a message to show that it to the user
def update_transactions():
    if not transactions:
        print("Yet there are no transactions available for")
        return
    #Update transactions
    view_transactions()
    update = input_errors("index", "Enter which transaction you need to update: ", len(transactions))
    amount = input_errors("amount", "Enter the amount: ", len(transactions))
    category = input_errors("category", "Enter the category: ", len(transactions)).capitalize()
    transaction_type = input_errors("type", "Enter the type (Income/Expense): ", len(transactions)).capitalize()
    date = input_errors("date", "Enter the date (YYYY-MM-DD): ", len(transactions))
    
    transactions[update-1] = {"amount": amount, "category": category, "type": transaction_type, "date": date}
    print("\nYour transaction updated successfully!!\n")
    save_transactions(transactions)

#Delete transactions as user's choice    
def delete_transaction():
    view_transactions()
    if transactions:
        delete = input_errors("index", "Enter which transaction you want to delete: ", len(transactions))
        del transactions[delete - 1]
        print("\nTransaction deleted successfully!!\n")
        save_transactions(transactions)
    #Print an error message if there is no transactions
    else:
        print("No transactions available so far!!")

#Display summary of transactions
def display_summary():
    total_income = 0
    total_expenses = 0
    #Calculate total income, total expenses and net income
    for transaction in transactions:
        if transaction["type"] == "Income":
            total_income += transaction["amount"]
        elif transaction["type"] == "Expense":
            total_expenses += transaction["amount"]
    net_income = total_income - total_expenses

    print("\nSummary Of Transactions: ")
    print(f"Total Income: Rs{total_income}")
    print(f"Total Expenses: Rs{total_expenses}")
    print(f"Net Income: Rs{net_income}")

#This function handle input errors and validate user inputs
def input_errors(slot, message, total_transactions ):
    while True:
        try:
            if slot == "choice":
                value = int(input(message))
                
                if 1 <= value <= 6:
                    return value
                else:
                    print("Invalid choice. Please select a choice between 1 and 6.")

            elif slot == "amount":
                try:
                    value = float(input(message))
                    if value > 0:
                        return value
                    else:
                        print("Invalid Amount. Amount can't be negative ")
                except ValueError:
                    print("Invalid input. Please enter a valid number for the amount.")

            elif slot == "category":
                value = input(message).capitalize()
                return value
            
            elif slot == "type":
                value = input(message).capitalize()
                if value =="Income" or value =="Expense":
                    return value
                else:
                    print("Invalid input. Please enter 'Income' or 'Expense'.")

            elif slot == "date":
                value = input(message)
                try:
                    datetime.strptime(value, '%Y-%m-%d')
                    return value
                except ValueError:
                    print("Invalid date format. Please re-enter the date")

            elif slot == "index":
                value = int(input(message))
                if 1 <= value <= total_transactions:
                    return value
                else:
                    print(f"Invalid index. Please enter a number between 1 and {total_transactions}.")
        except ValueError:
            print("Invalid input. Please try again.")

#Main function to call all the other functions as them needed by the user
def main_menu():
    #Load transactions at the start
    load_transactions()  
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        #Choices to select for the user to which option do they want
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transactions()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()