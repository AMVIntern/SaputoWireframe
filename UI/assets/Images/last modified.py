import os
from datetime import datetime

# =====================================
# ENTER FOLDER PATH HERE
# =====================================

folder_path = r"E:\AMV\Saputo\Wireframe\UI\assets\Images"

# =====================================
# SUPPORTED IMAGE EXTENSIONS
# =====================================

image_extensions = (".jpg", ".jpeg", ".png", ".bmp")

# =====================================
# CHECK IF PATH EXISTS
# =====================================

if not os.path.exists(folder_path):
    print("Folder path does not exist.")
    exit()

# =====================================
# LOOP THROUGH ALL FILES
# =====================================

for root, dirs, files in os.walk(folder_path):

    for file in files:

        # Check image extension
        if file.lower().endswith(image_extensions):

            # Full file path
            file_path = os.path.join(root, file)

            try:

                # Get modified timestamp
                modified_time = os.path.getmtime(file_path)

                # Convert timestamp to readable format
                readable_time = datetime.fromtimestamp(
                    modified_time
                ).strftime("%Y-%m-%d %H:%M:%S")

                # Print result
                print(f"File: {file}")
                print(f"Modified Date: {readable_time}")
                #print(f"Path: {file_path}")
                print("-" * 60)

            except Exception as e:

                print(f"Error reading file: {file_path}")
                print(e)

print("Done.")