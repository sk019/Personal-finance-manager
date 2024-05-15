from datetime import datetime, timedelta


class Transaction:
    """
    Represents a single financial transaction.
    """

    def __init__(self, date, description, amount):
        """
        Initializes a transaction with date, description, and amount.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            description (str): Description of the transaction.
            amount (float): Amount of the transaction.
        """
        self.date = date
        self.description = description
        self.amount = amount


class FinanceManager:
    """
    Manages financial transactions and provides functionalities to add transactions, view transaction history,
     and calculate balance.
    """

    def __init__(self):
        """
        Initializes the FinanceManager with an empty list of transactions.
        """
        self.transactions = []

    def add_transaction(self, date, description, amount):
        """
        Adds a new transaction to the list.

        Args:
            date (str): Date of the transaction in YYYY-MM-DD format.
            description (str): Description of the transaction.
            amount (float): Amount of the transaction.
        """
        self.transactions.append(Transaction(date, description, amount))
        print("Transaction added successfully!")

    def view_transactions(self, period='all'):
        """
        Displays the transaction history for the specified period.

        Args:
            period (str): Period for which transactions should be displayed. Options: 'all', 'daily', 'weekly',
             'monthly'.
        """
        if not self.transactions:
            print("Your transaction history is empty!")
            return

        print("\nTransaction History:")

        if period == 'all':
            transactions_to_display = self.transactions
        else:
            transactions_to_display = self._filter_transactions_by_period(period)

        for transaction in transactions_to_display:
            print(f"Date: {transaction.date}, Description: {transaction.description}, Amount: {transaction.amount}")

    def _filter_transactions_by_period(self, period):
        """
        Helper method to filter transactions by period.

        Args:
            period (str): Period for which transactions should be filtered. Options: 'daily', 'weekly', 'monthly'.

        Returns:
            list: Filtered transactions based on the specified period.
        """
        today = datetime.today()
        if period == 'daily':
            return [t for t in self.transactions if t.date == today.strftime('%Y-%m-%d')]
        elif period == 'weekly':
            start_of_week = today - timedelta(days=today.weekday())
            end_of_week = start_of_week + timedelta(days=6)
            return [t for t in self.transactions if
                    start_of_week <= datetime.strptime(t.date, '%Y-%m-%d') <= end_of_week]
        elif period == 'monthly':
            start_of_month = today.replace(day=1)
            end_of_month = today.replace(day=1, month=today.month % 12 + 1) - timedelta(days=1)
            return [t for t in self.transactions if
                    start_of_month <= datetime.strptime(t.date, '%Y-%m-%d') <= end_of_month]
        else:
            return []

    def calculate_balance(self):
        """
        Calculates the total income, total expenses, and current balance.
        """
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.amount > 0)
        total_expenses = sum(transaction.amount for transaction in self.transactions if transaction.amount < 0)
        balance = total_income + total_expenses
        print(f"\nTotal Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Current Balance: {balance}")


def main():
    """
    Main function to run the Personal Finance Manager.
    """
    finance_manager = FinanceManager()

    while True:
        print("\n===== Personal Finance Manager =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Transactions for Today")
        print("5. View Transactions for This Week")
        print("6. View Transactions for This Month")
        print("7. Calculate Balance")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter income amount: "))
            finance_manager.add_transaction(date, description, amount)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter expense amount: "))
            finance_manager.add_transaction(date, description, -amount)
        elif choice == "3":
            finance_manager.view_transactions()
        elif choice == "4":
            finance_manager.view_transactions('daily')
        elif choice == "5":
            finance_manager.view_transactions('weekly')
        elif choice == "6":
            finance_manager.view_transactions('monthly')
        elif choice == "7":
            finance_manager.calculate_balance()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
