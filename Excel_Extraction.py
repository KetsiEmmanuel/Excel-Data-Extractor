import pandas as pd

def extract_data(file_path, sheet_names, cell_ranges):
    try:
        for sheet_name in sheet_names:
            # Read the Excel file for each sheet name
            df = pd.read_excel(file_path, sheet_name=sheet_name)

            # Extract and print the data for each cell range
            for cell_range in cell_ranges:
                selected_data = df.loc[cell_range]
                print(f"Extracted Data from {sheet_name} at specified cells {cell_range}:")
                print(selected_data)
                print("\n")  # Add a newline for better separation

                # You can perform further data processing or analysis here

    except Exception as e:
        print(f"Error: {e}")

# Allow users to input file paths and sheet names
file_paths = []
while True:
    file_path = input("Enter the path to your Excel file (or 'done' to finish): ")
    if file_path.lower() == 'done':
        break

    # Replace non-breaking space with regular space in file path
    file_path = file_path.replace('\xa0', ' ')

    file_paths.append(file_path)

# Allow users to input sheet names
sheet_names_input = input("Enter sheet names (comma-separated): ")
sheets_to_extract = [sheet.strip() for sheet in sheet_names_input.split(',')]

# Allow users to input cell ranges (e.g., A1:B3, C5, D8:E10)
cell_ranges_input = input("Enter cell ranges (comma-separated): ")
cell_ranges = [cell_range.strip() for cell_range in cell_ranges_input.split(',')]

# Process each file path
for file_path in file_paths:
    extract_data(file_path, sheets_to_extract, cell_ranges)
