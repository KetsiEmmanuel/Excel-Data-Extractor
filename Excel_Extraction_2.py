import pandas as pd

def extract_data(file_path, sheet_names):
    try:
        for sheet_name in sheet_names:
            # Read the Excel file for each sheet name
            df = pd.read_excel(file_path, sheet_name=sheet_name)

            # Extract and print the data
            print(f"Extracted Data from {sheet_name}:")
            print(df)
            print("\n")  # Add a newline for better separation

            # You can perform further data processing or analysis here

    except Exception as e:
        print(f"Error: {e}")

# Example usage with specific file_path and user-provided inputs
file_path = input("Enter the path to your Excel file: ")

# Allow users to input sheet names
sheet_names_input = input("Enter sheet names (comma-separated): ")
sheets_to_extract = [sheet.strip() for sheet in sheet_names_input.split(',')]

extract_data(file_path, sheets_to_extract)