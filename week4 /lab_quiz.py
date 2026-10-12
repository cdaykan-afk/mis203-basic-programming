"""
Lab 04: Monthly Savings Planner
Simulates month-by-month compound savings growth with input validation.
"""
def get_positive_float(prompt: str) -> float:
    """Prompt user repeatedly until a strictly positive float (> 0) is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Error: Value must be strictly greater than 0. Please try again.")
        except ValueError:
            print("Error: Invalid numeric input. Please enter a valid number.")

def get_non_negative_float(prompt: str) -> float:
    """Prompt user repeatedly until a non-negative float (>= 0) is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Error: Value cannot be negative. Please try again.")
        except ValueError:
            print("Error: Invalid numeric input. Please enter a valid number.")
def main():
    print("=== Monthly Savings Planner ===\n")

  
    starting_balance = get_non_negative_float("Enter starting balance: ")
    monthly_deposit = get_positive_float("Enter monthly deposit: ")
    interest_rate = get_non_negative_float("Enter monthly interest rate (%): ")
    savings_goal = get_positive_float("Enter savings goal: ")

    balance = starting_balance
    total_interest = 0.0

    print()  

   
    if balance >= savings_goal:
        print("Savings goal is already met by the starting balance! No simulation needed.")
        print("-" * 50)
        print(f"Goal reached: Yes (0 months)")
        print(f"Final balance: ${balance:.2f}")
        print(f"Total interest earned: ${total_interest:.2f}")
        return

   
    print(f"{'Month':<8}{'Interest Earned':<18}{'New Balance':<15}")
    print("-" * 41)

    months_elapsed = 0
    goal_reached = False

   
    for month in range(1, 61):
        months_elapsed = month

       
        month_interest = balance * (interest_rate / 100.0)
        total_interest += month_interest

       
        balance += month_interest + monthly_deposit

        
        print(f"{month:<8}${month_interest:<17.2f}${balance:<14.2f}")
ak
        if balance >= savings_goal:
            goal_reached = True
            break

    
    print("-" * 41)
    if goal_reached:
        print(f"Goal reached: Yes, in {months_elapsed} month(s).")
    else:
        print(f"Goal reached: No, goal of ${savings_goal:.2f} was not reached within 60 months.")

    print(f"Final balance: ${balance:.2f}")
    print(f"Total interest earned: ${total_interest:.2f}")


if __name__ == "__main__":
    main()
