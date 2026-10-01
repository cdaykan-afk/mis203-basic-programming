
total_tickets = 0
total_revenue = 0.0
free_tickets = 0

while True:
    name_input = input("Enter name (or 'q' to quit): ").strip()
    if name_input.lower() == 'q':
        break
    if not name_input:
        print("Warning: Name cannot be empty.")
        continue

    age_input = input("Enter age (0-120): ").strip()
    if age_input.lower() == 'q':
        break
    try:
        age = int(age_input)
        if not (0 <= age <= 120):
            print("Warning: Age must be an integer between 0 and 120.")
            continue
    except ValueError:
        print("Warning: Invalid age. Please enter an integer.")
        continue

    day_input = input("Enter day type ('weekday' / 'weekend'): ").strip().lower()
    if day_input == 'q':
        break
    if day_input in ["weekday"]:
        base_price = 200.0
    elif day_input in ["weekend"]:
        base_price = 250.0
    else:
        print("Warning: Day type must be either 'weekday' or 'weekend'.")
        continue

    student_input = input("Are you a student? ('yes' / 'no'): ").strip().lower()
    if student_input == 'q':
        break
    if student_input in ["yes", "y"]:
        is_student = True
    elif student_input in ["no", "n"]:
        is_student = False
    else:
        print("Warning: Student status must be either 'yes' or 'no'.")
        continue

    # Discount priority rules and category determination
    if age < 6:
        category = "Free"
        discount_rate = 1.00
    elif age >= 65:
        category = "Senior"
        discount_rate = 0.50
    elif 6 <= age <= 12:
        category = "Child"
        discount_rate = 0.40
    elif age <= 25 and is_student:
        category = "Student"
        discount_rate = 0.30
    else:
        category = "Standard"
        discount_rate = 0.00

    final_price = base_price * (1 - discount_rate)

    # Sale output
    print(f"{name_input}: {final_price:.2f} TRY ({category})")

    # Update summary statistics
    total_tickets += 1
    total_revenue += final_price
    if final_price == 0.0:
        free_tickets += 1

# Summary report
if total_tickets == 0:
    print("No tickets sold.")
else:
    avg_price = total_revenue / total_tickets
    print("\n--- Sales Summary ---")
    print(f"Total Tickets Sold   : {total_tickets}")
    print(f"Total Revenue        : {total_revenue:.2f} TRY")
    print(f"Average Ticket Price : {avg_price:.2f} TRY")
    print(f"Free Tickets Count   : {free_tickets}")

