# Academic Integrity Statement
# filename: Menu.py
# author: Kayden Hong
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 07 September 2025
# description: Menu class
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
        
    
    
    def display_menu(self):
        print("\n".join(self.initial_menu_options))
        return
    
    def new_component(self) -> None:
        
        while True:
            self.display_menu(self.new_component_menu)
            choice = self.get_choice(9)

            if choice == 1:  # Wire
                print("\nNEW WIRE")
                length = int(input("Please enter length (mm): "))
                price = float(input("Please enter price: "))
                qty = int(input("Please enter number of Wires: "))
                print("Added " + str(length) + "mm Wire $" + "{:.2f}".format(price) + " X " + str(qty) + "\n")

                voltage = float(input("Please enter a voltage that matches the battery size: "))
                price = float(input("Please enter price: "))
                qty = int(input("Please enter number of Batteries: "))
                print("Added " + "{:.1f}".format(voltage) + "V " + size + " Battery $" + "{:.2f}".format(price) + " X " + str(qty) + "\n")

            elif choice == 9:  # Back
                break

            else:
                print("Feature not implemented yet. Choose Wire or Battery for now.\n")

    def view_components(self):
    
     if not self.components:
        print("No components have been created yet.")
     else:
        print("\nALL COMPONENTS")
        for i in range(len(self.components)):
            print(str(i + 1) + ". " + self.components[i])

    def component_menu_loop(self) -> None:
    
     running = True
     while running:
        self.display_menu(self.component_menu)
        choice = self.get_choice(3)

        if choice == 1:  # New Component
            self.new_component()
        elif choice == 2:  # View Components
            self.view_components()
        elif choice == 3:  # Back
            running = False

    def home_menu_loop(self):
     running = True
     while running:
        self.display_menu(self.initial_menu_options)
        choice = self.get_choice(6)



        

    def __str__(self) -> str:
        return "\n".join(self.initial_menu_options)



            
    

    


if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()
    choice = menu.get_choice()
    pass
