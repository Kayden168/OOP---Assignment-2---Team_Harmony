# Academic Integrity Statement
# filename: menu.py
# author: Kayden Hong and Sandy
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 04 September 2025
# description: menu class
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
        self.component_menu_options = [
            "COMPONENT MENU",
            "1. NEW COMPONENT",
            "2. VIEW COMPONENTS",
            "3. BACK",
        ]
        self.new_component_menu_options = [
            "NEW COMPONENT MENU",
            "1. WIRE",
            "2. BATTERY",
            "3. SOLAR PANEL",
            "4. LIGHT GLOBE",
            "5. LED LIGHT",
            "6. SWITCH",
            "7. SENSOR",
            "8. BUZZER",
            "9. BACK",
        ]
        self.components = []

    def get_choice(self, max_option: int) -> int:
        while True:
            try:
                choice = int(input("Please enter a number: "))
                if 1 <= choice <= max_option:
                    return choice
                else:
                    print(f"Wrong input, must be a number between 1 and {max_option}")
            except ValueError:
                print("Invalid input, please enter a number.")

    def display_menu(self, lines: list[str]) -> None:
        print("\n".join(lines))

    def new_component(self) -> None:
        while True:
            self.display_menu(self.new_component_menu_options)
            choice = self.get_choice(9)
            if choice == 1:
                print("NEW WIRE")
                length = int(input("Please enter length (mm): "))
                price = float(input("Please enter price: "))
                qty = int(input("Please enter number of Wires: "))
                item = f"{length}MM WIRE ${price:.2f} X {qty}"
                self.components.append(item)
                print(f"Added {length}mm Wire ${price:.2f} X {qty}\n")
            elif choice == 2:
                print("NEW BATTERY")
                print("Battery sizes are AA or AAA or C or D or E")
                size = input("Please enter battery size: ").strip().upper()
                print("AA, AAA and C batteries are either 1.2 Volts or 1.5 Volts")
                print("D batteries are 1.5 Volts")
                print("E batteries are 9.0 Volts")
                voltage = float(input("Please enter a voltage that matches the battery size: "))
                price = float(input("Please enter price: "))
                qty = int(input("Please enter number of Batteries: "))
                item = f"{voltage:.1f}V {size} BATTERY ${price:.2f} X {qty}"
                self.components.append(item)
                print(f"Added {voltage:.1f}V {size} Battery ${price:.2f} X {qty}\n")
            elif choice == 9:
                break
            else:
                print("Feature not implemented yet.\n")

    def view_components(self) -> None:
        if not self.components:
            print("No components have been created yet.")
        else:
            print("ALL COMPONENTS")
            for i, line in enumerate(self.components, start=1):
                print(f"{i}. {line}")
            print(f"{len(self.components)+1}. BACK")

    def component_menu_loop(self) -> None:
        running = True
        while running:
            self.display_menu(self.component_menu_options)
            choice = self.get_choice(3)
            if choice == 1:
                self.new_component()
            elif choice == 2:
                self.view_components()
            elif choice == 3:
                running = False

    def home_menu_loop(self) -> None:
        running = True
        while running:
            self.display_menu(self.initial_menu_options)
            choice = self.get_choice(6)
            if choice == 1:
                self.component_menu_loop()
            elif choice == 2:
                print("Circuit Kits menu not implemented yet.\n")
            elif choice == 3:
                print("Purchase Orders menu not implemented yet.\n")
            elif choice == 4:
                print("Customer Sales menu not implemented yet.\n")
            elif choice == 5:
                print("Transaction History menu not implemented yet.\n")
            elif choice == 6:
                print("Closing program...")
                running = False


if __name__ == "__main__":
    Menu().home_menu_loop()
