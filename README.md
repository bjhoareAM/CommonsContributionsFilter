Pattypan Upload Checker for Wikimedia Commons
This tool checks your Wikimedia Commons uploads for a given pattern (e.g. "pattypan") in the edit summary and exports the matching uploads to Excel or CSV.

Features:
Filters your Commons contributions by edit summary text

Outputs results to .xlsx (Excel) and/or .csv

Useful for checking batch uploads (e.g. Pattypan, GLAMwiki Toolset)

How to Use:
Clone this repository

Install required Python libraries:

bash
Copy
Edit
pip install requests openpyxl
Create a config.json file in the root folder:

jsonc
Copy
Edit
{
  "username": "YourWikimediaUsername",         // Your Commons username (case-sensitive)
  "pattern": "pattypan",                        // Text to search for in the upload comment
  "output_excel": true,                         // Set to true to export to Excel (.xlsx)
  "output_csv": false,                          // Set to true to export to CSV
  "max_per_request": 500                        // API batch size (max = 500)
}
Note: The pattern is case-insensitive. "pattypan", "Pattypan" and "PATTYPAN" will all match.

Run the script

bash
Copy
Edit
python main.py
The script will save your results in the project folder as .xlsx and/or .csv, depending on your settings.