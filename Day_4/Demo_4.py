
'''
CosTools Indus:
- Enroll vendors with their name and GST number.
- Bill products using quantity, unit cost and 18% tax.
- Maintain billing records in vendor_prods.log with date and time.
'''

from datetime import datetime

LOG_FILE = "vendor_prods.log"


class Vendor:
    def __init__(self, vName, vGst):
        self.vName = vName
        self.vGst = vGst
        print(f"Vendor initialized: {self.vName}, GST: {self.vGst}")

    def display(self):
        print(f"Vendor Name: {self.vName}")
        print(f"GST: {self.vGst}")

    def billing(self, pName, pQty, pCost):
        total = pQty * pCost
        tax = total * 0.18
        total_with_tax = total + tax

        print(
            f"Billing - Product: {pName}, Quantity: {pQty}, "
            f"Cost: {pCost:.2f}, Total: {total:.2f}, "
            f"Total with Tax: {total_with_tax:.2f}"
        )

        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(
                f"{datetime.now().ctime()} | {self.vName} | "
                f"{self.vGst} | {pName} | {pQty} | "
                f"{pCost:.2f} | {total:.2f} | "
                f"{tax:.2f} | {total_with_tax:.2f}\n"
            )


# Write the header only when the file is empty
with open(LOG_FILE, "a", encoding="utf-8") as log_file:
    if log_file.tell() == 0:
        log_file.write(
            "Date/Time | Vendor | GST | Product | Qty | "
            "Unit Cost | Total | Tax | Total+Tax\n"
        )


# Enroll vendors
vendor1 = Vendor("ABC Supplies", "GST1234")
vendor2 = Vendor("XYZ Traders", "GST5678")

# Display details and bill products
vendor1.display()
vendor1.billing("Laptop", 2, 50000)

vendor2.display()
vendor2.billing("Mouse", 10, 500)