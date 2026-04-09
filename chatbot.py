import csv

def get_result(marks: int) -> str:
    if marks < 33:
        return "FAIL "
    elif marks < 50:
        return "PASS - Third Division"
    elif marks < 60:
        return "PASS - Second Division"
    else:
        return "PASS - First Division "

def chatbot():
    print(" Welcome to Student Result Chatbot")
    print("Type student name to check result")
    print("Type 'exit' to quit\n")

    while True:
        name = input("You: ").strip()
        if name.lower() == "exit":
            print("Bot: Goodbye ")
            break
        if not name:
            print("Bot: Please enter a valid name!\n")
            continue

        try:
            with open("students_names_only.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                results = []

                for row in reader:
                    if name.lower() in row.get("Name", "").lower():  
                        marks = int(row.get("Marks", 0))
                        result = get_result(marks)
                        results.append({
                            "Name": row.get("Name", ""),
                            "Marks": marks,
                            "Result": result
                        })

                if results:
                    print("\nBot: 🎓 Matching Students Found:\n")
                    for student in results:
                        print(f"Name   : {student['Name']}")
                        print(f"Marks  : {student['Marks']}")
                        print(f"Status : {student['Result']}")
                        print("------------------------")
                else:
                    print("Bot: No student found!\n")

        except FileNotFoundError:
            print("Bot: CSV file not found! Check file location.\n")
            break

chatbot()