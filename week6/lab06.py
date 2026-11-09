branches = ("Software", "Design", "Marketing")

all_students = []

student1 = ["  Ahmet Yilmaz  ".strip(), ["Software"]]
student2 = [" Zeynep Demir ".strip(), ["Design", "Marketing"]]
student3 = ["Mehmet Kaya  ".strip(), ["Software", "Design"]]

all_students.append(student1)
all_students.append(student2)
all_students.append(student3)

print("--- Initial Student List ---")
print(all_students)
print("-" * 40)

president_student = ["Caner President".strip(), ["Software", "Design", "Marketing"]]
all_students.insert(0, president_student)

total_count = len(all_students)
print(f"Total Registered Students: {total_count}")
print("-" * 40)

for student in all_students:
    if student[0] == "Mehmet Kaya":
        all_students.remove(student)
        break

removed_student = all_students.pop()
print(f"Last student who left the system: {removed_student[0]}")
print("-" * 40)

all_students.append(["Burak Tan".strip(), ["Design"]])

sorted_temporary = sorted(all_students)
print("Temporarily Sorted List (sorted):")
print(sorted_temporary)
print("\nProof That Original List Has Not Changed (Original List):")
print(all_students)
print("-" * 40)

all_students.sort()
print("Permanently Sorted Main List (sort):")
print(all_students)
