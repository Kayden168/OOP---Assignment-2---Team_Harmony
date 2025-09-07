# Academic Integrity Statement
# filename: UI.py
# author: Kayden Hong
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 07 September 2025
# description: UI class
# This is my own work as defined by the Academic Integrity Policy
class UI:
    def __init__(self, menu) -> None:
        self.menu = menu
        return
    @property
    def menu(self):
        return "\n".join([
            "HOME MENU",
            "1. COMPONENTS",
            "2. CIRCUIT KITS",
            "3. PURCHASE ORDERS",
            "4. CUSTOMER SALES",
            "5. TRANSACTION HISTORY",
            "6. CLOSE",
            int(input("Please enter a number: "))
        ])
    pass
if __name__ == "__main__":
    print(UI.menu())
    pass