import os
import shutil

# Define categories based on file extensions
file_categories = {
    "Documents": [".txt", ".docx", ".pdf"],
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "WordFiles": [".docx"],
    "PDFs": [".pdf"]
}

# Base path of your folder on the desktop
base_path = r"C:\Users\PC\OneDrive\Desktop\CodeALphaAutomationProject"

# Function to sort files into categories
def organize_files():
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1].lower()
            # Check file extension and move to respective category
            for folder, extensions in file_categories.items():
                if file_extension in extensions:
                    folder_path = os.path.join(base_path, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(item_path, folder_path)
                    print(f"Moved {item} to {folder}")
                    break
    print("File organization complete.")

# Function to clean up CSV files
def clean_csv(csv_filename):
    csv_path = os.path.join(base_path, csv_filename)
    if os.path.exists(csv_path):
        # Reading and cleaning CSV without using pandas
        with open(csv_path, 'r') as file:
            lines = file.readlines()

        # Removing empty lines or duplicates
        cleaned_data = list(dict.fromkeys([line.strip() for line in lines if line.strip()]))

        # Saving cleaned data to a new file
        cleaned_csv_path = csv_path.replace(".csv", "_cleaned.csv")
        with open(cleaned_csv_path, 'w') as cleaned_file:
            for line in cleaned_data:
                cleaned_file.write(f"{line}\n")

        print(f"Cleaned CSV saved as {cleaned_csv_path}")
    else:
        print(f"{csv_filename} not found.")

# Function to delete unnecessary temp files
def remove_temp_files():
    temp_folder = os.path.join(base_path, "Temp")
    if os.path.exists(temp_folder):
        for item in os.listdir(temp_folder):
            item_path = os.path.join(temp_folder, item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                    print(f"Deleted file {item}")
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"Deleted folder {item}")
            except Exception as e:
                print(f"Error deleting {item}: {e}")
        print("Temporary files cleared.")
    else:
        print("Temp folder not found.")

# Menu to interact with the script
def menu():
    while True:
        print("\nSelect an option:")
        print("1. Organize files")
        print("2. Clean a CSV file")
        print("3. Remove temp files")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            organize_files()
        elif choice == '2':
            csv_filename = input("Enter the CSV filename (with extension): ")
            clean_csv(csv_filename)
        elif choice == '3':
            remove_temp_files()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the menu function
menu()
