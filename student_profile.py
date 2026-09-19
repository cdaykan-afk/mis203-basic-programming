"""
Course: MIS203 - Basic Programming
Week 1: Interactive Student Profile Generator
"""

# --- Header & Welcome ---
print("=" * 50)
print("     🎓 WELCOME TO THE STUDENT PROFILE PORTAL     ")
print("=" * 50)
print("Please enter your details below:\n")

# --- Inputs with basic formatting ---
name = input("▸ Full Name        : ").strip().title()
age = input("▸ Age              : ").strip()
department = input("▸ Department       : ").strip().title()
career_goal = input("▸ Career Goal      : ").strip().capitalize()

# --- Stylized Card Output ---
print("\n" + "┌" + "─" * 48 + "┐")
print("│" + " STUDENT PROFILE CARD ".center(48) + "│")
print("├" + "─" * 48 + "┤")
print(f"│  • Name       : {name:<30}│")
print(f"│  • Age        : {age:<30}│")
print(f"│  • Department : {department:<30}│")
print(f"│  • Goal       : {career_goal:<30}│")
print("├" + "─" * 48 + "┤")
print(f"│  Status: Active Student | MIS203 Program       │")
print("└" + "─" * 48 + "┘")

# Closing message
print(f"\n✨ Good luck on your journey towards becoming a {career_goal}, {name}!\n")
