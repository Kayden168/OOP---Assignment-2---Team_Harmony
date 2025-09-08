# Academic Integrity Statement
# filename: UI.py
# author: Kayden Hong
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 07 September 2025
# description: UI class
# This is my own work as defined by the Academic Integrity Policy
class UI:
    def __init__(self) -> None:
        self.menu_options = [
            "HOME MENU",
            "1. COMPONENTS",
            "2. CIRCUIT KITS",
            "3. PURCHASE ORDERS",
            "4. CUSTOMER SALES",
            "5. TRANSACTION HISTORY",
            "6. CLOSE",
        ]
        return None
    
    def get_choice(self):
        while True:
            try:
                choice = int(input("Please enter a number: "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Invalid number, enter a number between 1 and 6.")
                    pass
            except ValueError:
                print("Invalid input, please enter a number.")
        
    def __str__(self):
        return "\n".join(
            self.menu_options
        )
    
    def display_menu(self):
        print("\n".join(self.menu_options))
        return
    pass

if __name__ == "__main__":
    ui = UI()
    ui.display_menu()
    choice = ui.get_choice()
    pass
git