
try:
    order_amount = float(input("Enter order amount (TRY): "))
    available_stock = int(input("Enter available stock: "))
    requested_quantity = int(input("Enter requested quantity: "))
    is_member_input = input("Is the customer a member? (yes/no): ").strip().lower()
    is_member = is_member_input in ["yes", "y", "true", "evet"]

   
    if requested_quantity <= 0:
        print("Order Rejected: Requested quantity must be greater than zero.")
    elif requested_quantity > available_stock:
        print("Order Rejected: Insufficient stock available.")
    else:
        
        if is_member and order_amount >= 500:
            discount = order_amount * 0.10
            final_price = order_amount - discount
            approval_reason = "Member discount (10%) applied for orders >= 500 TRY."
        else:
            final_price = order_amount
            approval_reason = "Standard pricing applied (no discount)."

        print("\n--- Order Summary ---")
        print(f"Status: Approved")
        print(f"Reason: {approval_reason}")
        print(f"Final Price: {final_price:.2f} TRY")

except ValueError:
    print("Invalid input! Please enter numeric values for amount and quantities.")
