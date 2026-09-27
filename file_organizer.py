import os
import shutil

print("====================================")
print("       FILE ORGANIZER")
print("====================================")

folder_path = input("Enter folder path to organize: ").strip()

if not os.path.exists(folder_path):
    print("Folder does not exist!")
else:
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".doc"],
        "Excel": [".xlsx", ".xls", ".csv"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Music": [".mp3", ".wav"]
    }

    organized_count = 0

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file_name)[1].lower()
            category = "Others"

            for folder_name, extensions in file_categories.items():
                if extension in extensions:
                    category = folder_name
                    break

            destination_folder = os.path.join(folder_path, category)
            os.makedirs(destination_folder, exist_ok=True)
            destination_path = os.path.join(destination_folder, file_name)

            if not os.path.exists(destination_path):
                shutil.move(file_path, destination_path)
                print(f"Moved: {file_name} -> {category}")
                organized_count += 1
            else:
                print(f"Skipped: {file_name} (already exists)")

    print("\n====================================")
    print("File organization completed!")
    print("Total files organized:", organized_count)
    print("====================================")
