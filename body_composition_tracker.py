import pandas as pd
from tabulate import tabulate
import os
from datetime import date

DATA_FOLDER = "body_composition_data"
FIELDS = ["Date", "Weight (kg)", "Height (cm)", "Body Fat (%)", "Birth Year"]

def initialize_data_folder():
    if not os.path.exists(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)

def get_person_file(person_name):
    return os.path.join(DATA_FOLDER, f"{person_name.lower().replace(' ', '_')}_data.csv")

def initialize_data_file(file_path, height, birth_year):
    if not os.path.isfile(file_path):
        with open(file_path, "w") as file:
            file.write(",".join(FIELDS) + "\n")
        # Save height and birth year for the person when initializing the data file
        entry = f"{date.today().isoformat()},,{height},,{birth_year}\n"
        with open(file_path, "a") as file:
            file.write(entry)

def calculate_age(birth_year):
    today = date.today()
    return today.year - birth_year

def display_data(person_name):
    file_path = get_person_file(person_name)
    if not os.path.exists(file_path):
        print("No data found for this person.")
        return

    df = pd.read_csv(file_path)
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Check if "Height (cm)" and "Birth Year" are present in the DataFrame
    if "Height (cm)" not in df or "Birth Year" not in df:
        print("Height or birth year data missing. Please initialize the data with height and birth year.")
        return

    height = "NA"
    birth_year = "NA"

    if not df.empty:
        height = df[df["Date"] == df["Date"].max()]["Height (cm)"].values[0]  # Get the last recorded height
        birth_year = df[df["Date"] == df["Date"].max()]["Birth Year"].values[0]

    if height == "NA" or birth_year == "NA":
        print("Height or Birth year information is not available, initialize the data again. ")
        return
    
    # Calculate age based on birth year and display it in the DataFrame
    df["Birth Year"] = pd.to_numeric(birth_year, errors='coerce')
    df["Age"] = calculate_age(int(birth_year))


    # Calculate and display BMI, BMR, and body age
    df["BMI"] = df["Weight (kg)"] / ((height / 100) ** 2)
    df["BMR"] = 10 * df["Weight (kg)"] + 6.25 * height - 5 * df["Age"] + 5
    df["Body Age"] = 0.1685 * df["BMI"] + 0.0385 * df["BMI"] * df["Age"] - 5.292
    df["Today"] = df["Date"]
    
    print("\nAdditional Information:")
    print(tabulate(df[["Today", "Age", "BMI", "BMR", "Body Age"]], headers='keys', tablefmt='psql'))

def add_entry(person_name, weight, body_fat):
    file_path = get_person_file(person_name)
    if not os.path.exists(file_path):
        print(f"No data found for {person_name}. Please initialize the data first.")
        return

    today = date.today().isoformat()
    df = pd.read_csv(file_path)

    height = "NA"
    birth_year = "NA"

    if not df.empty:
        height = df[df["Date"] == df["Date"].max()]["Height (cm)"].values[0]  # Get the last recorded height
        birth_year = df[df["Date"] == df["Date"].max()]["Birth Year"].values[0]

    entry = f"{today},{weight},{height},{body_fat},{birth_year}\n"
    with open(file_path, "a") as file:
        file.write(entry)

def main():
    initialize_data_folder()

    while True:
        print("\nBody Composition Tracker")
        print("1. View Progress")
        print("2. Initialize Data")
        print("3. Add Entry")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            person_name = input("Enter person's name: ")
            display_data(person_name)
        elif choice == "2":
            person_name = input("Enter person's name: ")
            try:
                height = float(input("Enter height (cm): "))
                birth_year = int(input("Enter date of birth (year): "))
                file_path = get_person_file(person_name)
                initialize_data_file(file_path, height, birth_year)
                print(f"Data for {person_name} initialized successfully!")
            except ValueError:
                print("Invalid input. Please enter numeric values for height and birth year.")
        elif choice == "3":
            person_name = input("Enter person's name: ")
            try:
                weight = float(input("Enter weight (kg): "))
                body_fat = float(input("Enter body fat percentage: "))
                add_entry(person_name, weight, body_fat)
                print("Entry added successfully!")
            except ValueError:
                print("Invalid input. Please enter numeric values for weight and body fat.")
        elif choice == "4":
            print("Exiting the Body Composition Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
