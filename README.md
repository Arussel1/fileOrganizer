# Python File Organizer

This Python script organizes files in a directory based on their extensions into categorized folders. A product from a newbie trying to script and automation with python

## Features

- **Automatically organizes files** into categories such as Images, Documents, Archives, and various code files (JS, TS, React, HTML, Python).
- **Customizable categories**: Easily modify or add new file categories based on your needs.
- **Cross-platform**: Works on Windows, macOS, and Linux.

## File Categories

The script currently sorts files into the following categories:

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`
- **Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`
- **Archives**: `.zip`, `.rar`, `.tar`, `.gz`
- **JS/TS**: `.ts`, `.js`
- **React**: `.jsx`, `.tsx`
- **HTML**: `.html`
- **Python**: `.py`

## Installation

1. **Clone the repository** or download the script directly:

   ```bash
   git clone https://github.com/yourusername/fileOraganizer
   cd fileOraganizer
2. **Ensure you have Python 3 installed** on your system. You can check your version by running:
   ```bash
   python3 --version
   ```
## Usage

1. **Run the script** in the directory you want to organize:
    ```bash
    python3 organizer.py
    ```

## Customizing Categories

To customize the file categories or add new ones, modify the file_categories dictionary in the script:

    file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "JS/TS": [".ts", ".js"],
    "React": [".jsx", ".tsx"],
    "HTML": [".html"],
    "Python": [".py"] 
    }
## Contributing

Feel free to fork this repository, make changes, and submit a pull request. Any improvements or additional features are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.