# Python File Organizer 📂

A simple Python automation tool that searches for files with a specific extension inside a folder (including subfolders) and moves them to another folder.

## Features 🚀

- Search files recursively using `os.walk()`
- Move files from one folder to another
- Filter files by extension (`.jpg`, `.png`, `.txt`, etc.)
- Detect duplicate filenames
- Rename duplicate files
- Skip duplicate files
- Count the number of moved files
- Handle invalid source and destination folders

## Technologies Used 🛠️

- Python 3
- os module
- shutil module
- pathlib module

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-file-organizer.git
```

2. Open the project folder:

```bash
cd python-file-organizer
```

3. Run the program:

```bash
python file_tools.py
```

## Example

Input:

```text
Enter the Folder: Desktop/test1
Enter destination folder: Documents/test2
Enter file extension: .jpg
```

Output:

```text
Moving file:
C:\Users\USER\Desktop\test1\cars.jpg

file moved!

5 files moved successfully!
```

## Project Structure

```text
python-file-organizer/

│── file_tools.py
│── README.md
```

## Future Improvements

- Automatic file renaming (`photo_1.jpg`, `photo_2.jpg`)
- GUI interface using Tkinter
- Support for multiple extensions
- Copy mode
- Delete mode
- Logging system

## Author

Atharv
