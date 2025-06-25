# CommonsContributionsFilter

**Pattypan Upload Checker for Wikimedia Commons**  
This tool checks your Wikimedia Commons uploads for a given pattern (e.g. `"pattypan"`) in the edit summary and exports the matching uploads to Excel or CSV.

---

## Features

- Filters your Commons contributions by edit summary or tag text
- Outputs results to `.xlsx` (Excel) and/or `.csv`
- Useful for checking batch uploads (e.g. Pattypan, GLAMwiki Toolset)

---

## How to Use

## 1. Clone this repository

```bash
git clone https://github.com/bjhoareAM/CommonsContributionsFilter.git
cd CommonsContributionsFilter
```

## 2. Install required Python libraries
```bash
pip install requests openpyxl'
```

## 3. Create a config.json file in the root folder
```json
{
  "username": "YourWikimediaUsername",        // Your Commons username (case-sensitive)
  "pattern": "pattypan",                      // Text to search for in the upload comment
  "output_excel": true,                       // Set to true to export to Excel (.xlsx)
  "output_csv": false,                        // Set to true to export to CSV
  "max_per_request": 500,                     // API batch size (max = 500)
  "uploads_only": true                        // If true, limits to new uploads (not edits)
}
```
Note: The pattern is case-insensitive. "pattypan", "Pattypan" and "PATTYPAN" will all match.

## 4. Run the script
```bash
python main.py
If matches are found, an Excel and/or CSV file will be generated with the filename:
uploads_YourWikimediaUsername_pattypan.xlsx
```

## Output Columns
* Timestamp — Upload time
* Title — File title on Commons
* Comment — Edit summary
* Categories — Any tags (e.g. openrefine-3.7, OAuth) associated with the upload

