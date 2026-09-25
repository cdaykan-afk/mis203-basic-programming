total_score = 0
student_count = 0

while True:
    name = input("Enter student name (or q to quit): ")

    if name.lower() == "q":
        break

    try:
        score = float(input("Enter score: "))
    except ValueError:
        print("Invalid score. Please enter a number between 0 and 100.\n")
        continue

    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.\n")
        continue

   
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    
    formatted_score = int(score) if score.is_integer() else score
    print(f"-> {name}: {formatted_score} ({grade})\n")

    total_score += score
    student_count += 1


print()
if student_count > 0:
    average_score = total_score / student_count
    print("=" * 36)
    print("           SUMMARY REPORT           ")
    print("=" * 36)
    print(f" Total Students : {student_count}")
    print(f" Average Score  : {average_score:.2f} / 100")
    print("=" * 36)
else:
    print("-" * 36)
    print(" [!] No students entered.")
    print("-" * 36)
