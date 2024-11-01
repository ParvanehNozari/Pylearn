def calculate_average_gpa():
    grades = []
    
    while True:
        user_input = input("Enter grade (or type 'exit' to finish): ")
        
        if user_input.lower() == 'exit':
            break
        
        try:
            grade = float(user_input)
            grades.append(grade)
        except ValueError:
            print("Please enter a valid number for the grade.")
    
    if grades:
        average_gpa = sum(grades) / len(grades)
        print(f"The average GPA is: {average_gpa:.2f}")
    else:
        print("No grades were entered.")

calculate_average_gpa()
