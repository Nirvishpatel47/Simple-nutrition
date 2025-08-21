# Nutrition Tracker and Calorie Calculator
This Python script is a simple, command-line-based nutrition and health tracker. It allows you to log your daily food intake, calculate your BMR (Basal Metabolic Rate), view nutritional summaries, and visualize your data.

# Features
User Registration: Add and save your personal information (name, weight, height, age).

## BMR Calculation: 
Calculates your Basal Metabolic Rate for both men and women.

## Nutrient Reporting: 
Provides a detailed report on the recommended daily intake for various nutrients like protein, fiber, vitamins, and minerals.

## Food Logging: 
Add single or multiple food items to a daily log, which is stored in an Excel file.

## Data Retrieval: 
View your nutrition data by specific dates or see a summary of your intake for the day.

## Data Visualization: 
Generates various plots (scatter, bar, box, line) using matplotlib and seaborn to help you visualize your nutritional data and gain insights.

## Food Information: 
Look up detailed nutritional information for specific food items.

## Data Management:
Remove rows from your data log.

# Setup Instructions
To get this project up and running on your local machine, follow these steps.

## Prerequisites
You'll need to have Python installed on your system. This project also relies on several Python libraries. You can install them all at once using pip.

Bash:

`pip install pandas matplotlib seaborn openpyxl`
openpyxl is necessary for reading and writing Excel files (.xlsx).

## File Structure
This is the required directory structure for the program to work correctly.

Your_Project_Folder/
├── Data.txt
├── Nutrition.json
├── Nutri.xlsx
└── Your_Python_Script_Name.py
Data.txt: This plain text file stores your user information (name, weight, height, age). The script automatically creates it if it doesn't exist.

Nutrition.json: This JSON file contains the nutritional data for various food items. You should have a file with this name containing all the nutritional information.

Nutri.xlsx: This Excel file will be created by the program to store your food log entries.

# How to Run
Make sure all the required files (Data.txt, Nutrition.json, Nutri.xlsx, and the Python script) are in the same directory.

Open your command-line interface (e.g., Terminal, Command Prompt).

Navigate to the directory where you saved the files.

Run the script with the following command:

Bash:

`python Your_Python_Script_Name.py`
The program's main menu will then be displayed, and you can interact with it by entering the corresponding numbers.

# How to Use
The program operates via a simple menu-driven interface in your terminal. Here's a brief breakdown of the main functions:

Add food: Log a single food item.

Add multiple food: Log several food items in one session.

Add food to yesterday: Log food for the previous day.

See the data: View your logged data. You can see the whole file, a specific date, or today's data.

See Files locations and info: Get information about the files and libraries used.

Remove Rows: Delete log entries from the Excel file.

Nutritional Info of Food: Search and see the nutritional details of a food item.

Get the data...: Sum up nutritional values for a specific date.

Get the graph: Visualize your data using different types of charts.

User Entry: Enter or update your personal information.

Exit: Exit the program.
