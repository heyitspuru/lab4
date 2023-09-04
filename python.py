# Define the Employee data as a list of dictionaries
employee_data = [
    {"Employee ID": "161E90", "Name": "Rajan", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himani", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jay", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tej", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000}
]

# Function to sort the employee data based on the chosen parameter
def sort_employee_data(parameter):
    if parameter == 1:
        return sorted(employee_data, key=lambda x: x["Age"])
    elif parameter == 2:
        return sorted(employee_data, key=lambda x: x["Name"])
    elif parameter == 3:
        return sorted(employee_data, key=lambda x: x["Salary (PM)"])
    else:
        return employee_data

# Ask the user to choose the sorting parameter
print("Choose a sorting parameter:")
print("1. Age")
print("2. Name")
print("3. Salary")
choice = int(input("Enter your choice (1/2/3): "))

# Sort and print the data based on the chosen parameter
sorted_data = sort_employee_data(choice)
print("\nSorted Employee Data:")
for employee in sorted_data:
    print(f"Employee ID: {employee['Employee ID']}, Name: {employee['Name']}, Age: {employee['Age']}, Salary (PM): {employee['Salary (PM)']}")