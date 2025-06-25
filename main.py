import requests
import json
import csv
import time
import openpyxl

# Load configuration
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

USERNAME = config["username"]
PATTERN = config["pattern"].lower()
EXPORT_EXCEL = config.get("output_excel", True)
EXPORT_CSV = config.get("output_csv", False)
MAX_PER_REQUEST = config.get("max_per_request", 500)
UPLOADS_ONLY = config.get("uploads_only", True)

print(f"Fetching uploads by '{USERNAME}'...")

S = requests.Session()
URL = "https://commons.wikimedia.org/w/api.php"

uploads = []
UC_CONTINUE = ""

while True:
    params = {
        "action": "query",
        "format": "json",
        "list": "usercontribs",
        "ucuser": USERNAME,
        "uclimit": MAX_PER_REQUEST,
        "ucprop": "title|comment|tags|timestamp|flags",
    }
    if UC_CONTINUE:
        params["uccontinue"] = UC_CONTINUE

    response = S.get(URL, params=params)
    data = response.json()

    for contrib in data.get("query", {}).get("usercontribs", []):
        comment = contrib.get("comment", "").lower()
        tags_list = contrib.get("tags", [])
        tags_string = ", ".join(tags_list).lower()
        title = contrib["title"]
        timestamp = contrib["timestamp"]

        if UPLOADS_ONLY and "new" not in contrib:
            continue

        if PATTERN in comment or PATTERN in tags_string:
            uploads.append([timestamp, title, comment, tags_string])

    if "continue" in data:
        UC_CONTINUE = data["continue"]["uccontinue"]
        time.sleep(0.5)  # Be kind to the API
    else:
        break

print(f"\nFound {len(uploads)} matching contributions with pattern '{PATTERN}'.")

filename_base = f"uploads_{USERNAME}_{PATTERN}"

# Export to Excel
if EXPORT_EXCEL:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Filtered Uploads"
    ws.append(["Timestamp", "Title", "Comment", "Categories"])
    for row in uploads:
        ws.append(row)
    wb.save(f"{filename_base}.xlsx")
    print(f"Saved Excel to {filename_base}.xlsx")

# Export to CSV
if EXPORT_CSV:
    with open(f"{filename_base}.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Title", "Comment", "Categories"])
        writer.writerows(uploads)
    print(f"Saved CSV to {filename_base}.csv")
