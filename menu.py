# Academic Integrity Statement
# filename: menu.py
# author: Kayden Hong and Sandy
# student ID: 523258
# email: 523258@learning.eynesbury.edu.au
# date: 04 September 2025
# description: menu class
# This is my own work as defined by the Academic Integrity Policy
import datetime

class Menu:
    def __init__(self):
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

        self.new_circuit_kit_menu_options = [
            "NEW CIRCUIT KIT MENU",
            "1. LIGHT GLOBE CIRCUIT KIT",
            "2. LED LIGHT CIRCUIT KIT",
            "3. SENSOR CIRCUIT KIT WITH LIGHT GLOBE",
            "4. SENSOR CIRCUIT KIT WITH LED LIGHT",
            "5. SENSOR CIRCUIT KIT WITH BUZZER",
            "6. SENSOR CIRCUIT KIT WITH LIGHT GLOBE AND SWITCH",
            "7. SENSOR CIRCUIT KIT WITH LED LIGHT AND SWITCH",
            "8. SENSOR CIRCUIT KIT WITH BUZZER AND SWITCH",
            "9. BACK",
        ]

        self.circuit_kit_menu_options = [
            "CIRCUIT KIT MENU",
            "1. NEW CIRCUIT KIT",
            "2. VIEW CIRCUIT KITS",
            "3. BACK",
        ]    

        self.buy_sell_menu_options = [
            "Buy",
            "Sell",
            "Pack",
            "Unpack",
            "Back"
        ]

        self.sort_options = [
            "Sort by date (ascending)",
            "Sort by date (descending)",
            "Sort by wholesale price (ascending)",
            "Sort by wholesale price (descending)",
            "Sort by retail price (ascending)",
            "Sort by retail price (descending)",
            "Back (Cancel Sorting)"
        ]
        self.components = []  # list of dicts
        self.circuit_kits = [] # list of dicts for kits
        self.transactions = []
        
    def get_choice(self, max_option):
        while True:
            try:
                choice = int(input("Please enter a number: "))
                if choice >= 1 and choice <= max_option:
                    return choice
                else:
                    print("Wrong input, must be a number between 1 and " + str(max_option))
            except:
                print("Invalid input, please enter a number.")

    def display_menu(self, lines):
        print("\n".join(lines))

    def add_component(self, desc, price, qty):
        self.components.append({"desc": desc, "price": price, "qty": qty})
        print("Added " + desc + " $" + str(price) + " X " + str(qty) + "\n")

    def add_circuit_kit(self, desc, price, qty):
        self.circuit_kits.append({"desc": desc, "price": price, "qty": qty})
        print("Added Circuit Kit " + desc + " $" + str(price) + " X " + str(qty) + "\n")

    def new_circuit_kit(self):
        self.display_menu(self.new_circuit_kit_menu_options)
        choice = self.get_choice(9)
        if choice != 9:
            desc = input("Enter description for new circuit kit: ")
            price = float(input("Enter price: "))
            qty = int(input("Enter quantity: "))
            self.add_circuit_kit(desc, price, qty)
    
    def view_circuit_kits(self):
        if not self.circuit_kits:
            print("No circuit kits have been created yet.")
            return
        exit_loop = False
        while not exit_loop:
            print("ALL CIRCUIT KITS")
            for i, kit in enumerate(self.circuit_kits, start=1):
                print(str(i) + ". " + kit["desc"] + " $" + str(kit["price"]) + " X " + str(kit["qty"]))
            print(str(len(self.circuit_kits) + 1) + ". BACK")
            choice = self.get_choice(len(self.circuit_kits) + 1)
            if choice == len(self.circuit_kits) + 1:
                exit_loop = True
            else:
                self.kit_actions(choice - 1)
    
    def kit_actions(self, index):
        kit = self.circuit_kits[index]
        running = True
        while running:
            print(kit["desc"] + " $" + str(kit["price"]))
            print("1. SELL\n2. PACK\n3. UNPACK\n4. BACK")
            choice = self.get_choice(4)
            if choice == 4:
                running = False
            else:
                qty = int(input("Please enter number of " + kit["desc"] + " $" + str(kit["price"]) + ": "))
                if choice == 1:
                    print("Selling " + kit["desc"])
                    kit["qty"] = max(0, kit["qty"] - qty)
                    print("Sold " + kit["desc"] + " X " + str(qty))
                elif choice == 2:
                    print("Packing " + kit["desc"])
                    kit["qty"] = kit["qty"] + qty
                    print("Packed " + kit["desc"] + " X " + str(qty))
                elif choice == 3:
                    print("Unpacking " + kit["desc"])
                    kit["qty"] = max(0, kit["qty"] - qty)
                    print("Unpacked " + kit["desc"] + " X " + str(qty))

    def circuit_kit_menu_loop(self):
        running = True
        while running:
            self.display_menu(self.circuit_kit_menu_options)
            choice = self.get_choice(3)
            if choice == 1:
                self.new_circuit_kit()
            elif choice == 2:
                self.view_circuit_kits()
            elif choice == 3:
                running = False
        
    def new_component(self):
        running = True
        while running:
            self.display_menu(self.new_component_menu_options)
            choice = self.get_choice(9)

            if choice == 1:  # wire
                print("NEW WIRE")
                length = int(input("Please enter length (mm): "))
                price = float(input("Please enter price: "))
                qty = int(input("Please enter number of Wires: "))
                desc = str(length) + "MM WIRE"
                self.add_component(desc, price, qty)

            elif choice == 2:  # battery
                print("NEW BATTERY")
                print("Battery sizes are AA or AAA or C or D or E")
                size = input("Please enter battery size: ").strip().upper()
                print("AA, AAA and C batteries are either 1.2 Volts or 1.5 Volts")
                print("D batteries are 1.5 Volts")
                print("E batteries are 9.0 Volts")
                voltage = float(input("Please enter a voltage that matches the battery size: "))
                price = float(input("Please enter price: "))
                qty = int(input("Please enter number of Batteries: "))
                desc = str(voltage) + "V " + size + " BATTERY"
                self.add_component(desc, price, qty)

            elif choice == 3:  # solar panel
                print("NEW SOLAR PANEL")
                voltage = float(input("Please enter voltage (V): "))
                current = float(input("Please enter current (mA): "))
                price = float(input("Please enter price: "))
                qty = int(input("Please enter number of Solar Panels: "))
                desc = str(voltage) + "V " + str(current) + "MA SOLAR PANEL"
                self.add_component(desc, price, qty)

            elif choice == 4:  # light globe
                print("NEW LIGHT GLOBE")
                colour = input("Please enter light globe colour: ").strip()
                voltage = float(input("Please enter voltage (V): "))
                current = float(input("Please enter current (mA): "))
                price = float(input("Please enter price: "))
                qty = int(input("Please enter number of Light Globes: "))
                desc = str(voltage) + "V " + str(current) + "MA " + colour.upper() + " LIGHT GLOBE"
                self.add_component(desc, price, qty)

            elif choice == 5:  # LED light
                print("NEW LED LIGHT")
                colour = input("Please enter LED light colour: ").strip()
                voltage = float(input("Please enter voltage (V): "))
                current = float(input("Please enter current (mA): "))
                price = float(input("Please enter price: "))
                qty = int(input("Please enter number of LED Lights: "))
                desc = str(voltage) + "V " + str(current) + "MA " + colour.upper() + " LED LIGHT"
                self.add_component(desc, price, qty)

            elif choice == 6:  # switch
                print("NEW SWITCH")
                stype = input("Please enter switch type: ").strip()
                voltage = float(input("Please enter voltage (V): "))
                price = float(input("Please enter price: "))
                qty = int(input("Please enter number of Switches: "))
                desc = str(voltage) + "V " + stype.upper() + " SWITCH"
                self.add_component(desc, price, qty)

            elif choice == 7:  # sensor
                print("NEW SENSOR")
                stype = input("Please enter sensor type: ").strip()
                voltage = float(input("Please enter voltage (V): "))
                price = float(input("Please enter price: "))
                qty = int(input("Please enter number of Sensors: "))
                desc = str(voltage) + "V " + stype.upper() + " SENSOR"
                self.add_component(desc, price, qty)

            elif choice == 8:  # buzzer
                print("NEW BUZZER")
                freq = float(input("Please enter frequency (Hz): "))
                spl = float(input("Please enter sound pressure (dB): "))
                voltage = float(input("Please enter voltage (V): "))
                current = float(input("Please enter current (mA): "))
                price = float(input("Please enter price: "))
                qty = int(input("Please enter number of Buzzers: "))
                desc = str(voltage) + "V " + str(current) + "MA " + str(freq) + "HZ " + str(int(spl)) + "DB BUZZER"
                self.add_component(desc, price, qty)

            elif choice == 9:
                running = False
            else:
                print("Feature not implemented yet.\n")

    def view_components(self):
        if not self.components:
            print("No components have been created yet.")
            return
        exit_loop = False
        while not exit_loop:
            print("ALL COMPONENTS")
            for i, comp in enumerate(self.components, start=1):
                print(f"{i}. {comp['desc']} ${comp['price']} X {comp['qty']}")
            print(f"{len(self.components) + 1}. BACK")
            choice = self.get_choice(len(self.components) + 1)
            if choice == len(self.components) + 1:
                exit_loop = True
            else:
                self.buy_sell_menu(choice - 1)
    
    def buy_sell_menu(self, item):
        while True:
            self.display_menu(self.buy_sell_menu_options)
            choice = self.get_choice(self.buy_sell_menu_options)

            if choice == 1:  # Buy
                qty = int(input("Enter quantity to buy: "))
                item["qty"] += qty
                print("Bought successfully.")
            elif choice == 2:  # Sell
                qty = int(input("Enter quantity to sell: "))
                if qty <= item["qty"]:
                    item["qty"] -= qty
                    print("Sold successfully.")
                else:
                    print("Not enough stock.")
            elif choice == 3:  # Pack
                print(f"Packing {item['desc']}...")
            elif choice == 4:  # Unpack
                print(f"Unpacking {item['desc']}...")
            elif choice == 5:  # Back
                return
            
    def component_menu_loop(self):
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

    def home_menu_loop(self):
        running = True
        while running:
            self.display_menu(self.initial_menu_options)
            choice = self.get_choice(6)
            if choice == 1:
                self.component_menu_loop()
            elif choice == 2:
                self.circuit_kit_menu_loop()
            elif choice == 3:
                self.purchase_orders_menu()
            elif choice == 4:
                self.customer_sales_menu()
            elif choice == 5:
                self.transaction_history_menu()
            elif choice == 6:
                running = False

    def purchase_orders_menu(self):
        current_order = []  # temporary list of items for this order
        running = True
        while running:
            print("\nPURCHASE ORDER")
            print("1. Add Item from Catalogue to Order")
            print("2. View Order")
            print("3. Clear Order")
            print("4. Complete Order")
            print("5. BACK (CANCEL ORDER)")
            choice = self.get_choice(5)

            if choice == 1:
                self.add_item_to_order(current_order, for_sale=False)
            elif choice == 2:
                self.view_order(current_order)
            elif choice == 3:
                current_order.clear()
                print("Order cleared.")
            elif choice == 4:
                if current_order:
                    total = sum(item['price'] * item['qty'] for item in current_order)
                    self.transactions.append({
                        "type": "Purchase Order",
                        "datetime": datetime.datetime.now(),
                        "items": current_order.copy(),
                        "total": total,
                        "wholesale": total,
                        "retail": total
                    })
                    print(f"Completing Purchase Order {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    current_order.clear()
                else:
                    print("Order is empty, cannot complete.")
            elif choice == 5:
                return
            
    def customer_sales_menu(self):
        current_sale = []  # temporary list of items for this sale
        running = True
        while running:
            print("\nCUSTOMER SALE")
            print("1. Add Item from Inventory to Sale")
            print("2. BACK (CANCEL ORDER)")
            choice = self.get_choice(2)

            if choice == 1:
                self.add_item_to_order(current_sale, for_sale=True)
            elif choice == 2:
                return

    def add_item_to_order(self, order_list, for_sale):
        if not self.components and not self.circuit_kits:
            print("No items in inventory.")
            return

        print("\nCATALOGUE")
        catalogue = self.components + self.circuit_kits
        for i, item in enumerate(catalogue, 1):
            if 'qty' in item:
                stock = f" X {item['qty']}"
            else:
                stock = ""
            print(f"{i}. {item['desc']} ${item['price']}{stock}")
        print(f"{len(catalogue)+1}. BACK")

        choice = self.get_choice(len(catalogue)+1)
        if choice == len(catalogue)+1:
            return

        selected_item = catalogue[choice-1]
        qty = int(input("Quantity: "))
        if for_sale:
            if qty > selected_item['qty']:
                print("Not enough stock available.")
                return
            selected_item['qty'] -= qty

        order_list.append({
            "desc": selected_item["desc"],
            "price": selected_item["price"],
            "qty": qty
        })
        print(f"Adding {qty} x {selected_item['desc']} ${selected_item['price']}")
    
    def transaction_history_menu(self):
        while True:
            print("\nTRANSACTION HISTORY")
            if not self.transactions:
                print("No transactions available.")
                return

            for i, t in enumerate(self.transactions, 1):
                print(f"{i}. {t['type']} {t['datetime'].strftime('%Y-%m-%d %H:%M:%S')}, total ${t['total']:.2f}")

            print(f"{len(self.transactions)+1}. SORT")
            print(f"{len(self.transactions)+2}. BACK")

            choice = self.get_choice(range(len(self.transactions) + 2))

            if choice == len(self.transactions) + 1:
                self.sort_transactions()
            elif choice == len(self.transactions) + 2:
                return
            
    def view_order(self, order_list):
        if not order_list:
            print("Order is empty.")
            return
        print("\nORDER")
        total_tally = 0
        for item in order_list:
            line_total = item['price'] * item['qty']
            print(f"{item['desc']} ${item['price']} X {item['qty']}")
            print(f"QUANTITY: {item['qty']}")
            print(f"PRICE: ${item['price']:.2f}")
            print(f"TOTAL: ${line_total:.2f}\n")
            total_tally += line_total  
        print(f"TOTAL TALLY: ${total_tally:.2f}")
    
    def transaction_history_menu(self):
        while True:
            print("\nTRANSACTION HISTORY")
            if not self.transactions:
                print("No transactions available.")
                return

            for i, t in enumerate(self.transactions, 1):
                print(f"{i}. {t['type']} {t['datetime'].strftime('%Y-%m-%d %H:%M:%S')}, total ${t['total']:.2f}")

            print(f"{len(self.transactions)+1}. SORT")
            print(f"{len(self.transactions)+2}. BACK")

            choice = self.get_choice(len(self.transactions)+2)

            if choice == len(self.transactions)+1:
                self.sort_transactions()
            elif choice == len(self.transactions)+2:
                return   
    
    def sort_transactions(self):
        while True:
            print("\nSORT OPTIONS")
            self.display_menu(self.sort_options)
            choice = self.get_choice(self.sort_options)

            if choice == 1:
                self.transactions.sort(key=lambda x: x["datetime"])
            elif choice == 2:
                self.transactions.sort(key=lambda x: x["datetime"], reverse=True)
            elif choice == 3:
                self.transactions.sort(key=lambda x: x["wholesale"])
            elif choice == 4:
                self.transactions.sort(key=lambda x: x["wholesale"], reverse=True)
            elif choice == 5:
                self.transactions.sort(key=lambda x: x["retail"])
            elif choice == 6:
                self.transactions.sort(key=lambda x: x["retail"], reverse=True)
            elif choice == 7:
                return
if __name__ == "__main__":
    Menu().home_menu_loop()
