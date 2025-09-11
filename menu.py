# Academic Integrity Statement
# filename: UI.py
# author: Kayden Hong
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 07 September 2025
# description: UI class
# This is my own work as defined by the Academic Integrity Policy
class Menu:
    def __init__(self) -> None:
        self.initial_menu_options = [
            "HOME MENU",
            "1. COMPONENTS",
            "2. CIRCUIT KITS",
            "3. PURCHASE ORDERS",
            "4. CUSTOMER SALES",
            "5. TRANSACTION HISTORY",
            "6. CLOSE",
        ]

        self.component_menu = [
            "COMPONENT MENU",
            "1. VIEW COMPONENT",
            "2. VIEW COMPONENTS",
            "BACK"
        ]

        self.new_component_menu = [
            "NEW COMPONENT MENU"
            "1. WIRE",
            "2. BATTERY",
            "3. SOLAR PANEL",
            "4. LIGHT GLOBE",
            "5. LED LIGHT",
            "6. SWITCH",
            "7. SENSOR",
            "8. BUZZER",
            "9. BACK"
        ]
        return None
    
    def get_choice(self):
        while True:
            try:
                choice = int(input("Please enter a number: "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Wrong input, must be a number between 1 and 6.")
                    pass
            except ValueError:
                print("Invalid input, please enter a number.")
        
    def __str__(self):
        return "\n".join(
            self.initial_menu_options
        )
    
    def display_menu(self):
        print("\n".join(self.initial_menu_options))
        return
    pass

if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()
    choice = menu.get_choice()
    pass