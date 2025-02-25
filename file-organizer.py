import os
import shutil

# Define file categories and their respective folders
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
}

# Folder to organize (change this to your test folder path)
DOWNLOADS_FOLDER = "C:/Users/USER/Documents"

def organize_files():
    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)

        # Ignore directories
        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(filename)[1].lower()

        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category_path = os.path.join(DOWNLOADS_FOLDER, category)

                # Create category folder if it doesn't exist
                if not os.path.exists(category_path):
                    os.makedirs(category_path)

                # Move file to the appropriate folder
                shutil.move(file_path, os.path.join(category_path, filename))
                print(f"Moved {filename} to {category}")
                break  # Stop checking once a match is found

if __name__ == "__main__":
    organize_files()
    print("File organization complete!")
