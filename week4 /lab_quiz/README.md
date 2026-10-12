# Lab 04: Savings Planner
-Test Run 
  - Input: Starting balance = 3000, Deposit = 500, Rate = 1.0, Goal = 3000.
  - Expected: Goal met immediately, 0 months elapsed, no table rows printed.
- **Adjustment Made:**
  - In initial testing, entering an initial balance already equal to or greater than the goal still ran month 1 through the loop. Added an upfront condition before the table header to exit early with 0 months elapsed and prevent table output.
- **Error Validation Test:**
  - Tested negative values (`-10`) on deposit and goal inputs, verifying that the `while` loop re-prompts appropriately until positive numbers are provided.
