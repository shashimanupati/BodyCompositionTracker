# Body Composition Tracker

The Body Composition Tracker is a Python script that allows you to track and analyze body composition data, including weight, body fat percentage, height, and birth year. It provides functionality to initialize data for a person, add new entries, and view progress over time.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.x
- pandas library
- tabulate library

You can install the required libraries using the following command:

```
pip install pandas tabulate
```

## How to Use

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

```
python body_composition_tracker.py
```

## Features

### 1. View Progress

Choose option 1 to view the progress of a specific person. The script will display a table with their recorded body composition data, including weight, height, body fat percentage, age, BMI, BMR, and body age.

### 2. Initialize Data

Choose option 2 to initialize data for a new person. The script will prompt you to enter the person's name, height (in centimeters), and birth year (year of birth). It will create a new CSV file for the person in the `body_composition_data` folder and store the provided data.

### 3. Add Entry

Choose option 3 to add a new entry for an existing person. The script will prompt you to enter the person's name, weight (in kilograms), and body fat percentage. It will append this new entry to the person's data file.

### 4. Exit

Choose option 4 to exit the Body Composition Tracker.

## Note

- If the person's data file does not exist when trying to view progress or add an entry, the script will notify you that no data is found for that person. In such cases, initialize data for the person first.

- If "Height (cm)" or "Birth Year" data is missing when trying to view progress, the script will ask you to initialize the data with height and birth year.

- The BMI (Body Mass Index), BMR (Basal Metabolic Rate), and body age are calculated and displayed based on the recorded data.

- The script uses the `date.today()` function to get the current date, so make sure your system's date is accurate.

## Data Storage

All data is stored in CSV files within the `body_composition_data` folder. Each person has a separate CSV file, and new entries are appended to their respective files.

## Contributing

If you find any issues with the script or have suggestions for improvement, feel free to open an issue or submit a pull request.

---

Enjoy tracking your body composition data with the Body Composition Tracker! If you have any questions or need assistance, don't hesitate to reach out. Happy tracking!
