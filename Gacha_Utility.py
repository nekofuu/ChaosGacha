import os
import re
import pandas as pd
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

SOURCE_DIR = "gachafiles" # The source for the upstream files
OUTPUT_DIR = "out"
OUTPUT_FILE = "gacha.xlsx"

def read_from_file(filename):
    data = []
    path = os.path.join(SOURCE_DIR, filename)
    try:
        with open(path, 'r') as file:
            for line in file:
                numberPrefix = r'^(\d+\.\s*)'
                match = re.match(numberPrefix, line) # Checks if the line starts with a number: "23." or "167. "
                if match:
                    entry = {}
                    parts = re.sub(numberPrefix, '', line).strip().split(',') # Gets parts without heading
                    entry["Name"] = parts[0]
                    entry["Rarity"] = float(parts[1])
                    data.append(entry)
                else:
                    if "Description" not in data[-1]:
                        poundPrefix = r'^(#\s*)'
                        desc = re.sub(poundPrefix, '', line) # Set description while removing the # prefix
                        data[-1]["Description"] = desc.rstrip()
                    else:
                        # There aren't currently any multi-line descriptions, so if this triggers
                        # then either that has changed, or there's an error somewhere.
                        print(f"Description found while non-heading line detected for entry '{data[-1]["Name"]}' in {filename}")
        return data
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except PermissionError:
        messagebox.showerror("Error", "Permission denied to access gachafiles directory.")
    
def write_to_spreadsheet(output, data):
    try:
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            for cat in data:
                df = pd.DataFrame(data[cat])
                df.to_excel(writer, sheet_name=cat, header=False, index=False, startrow=1) # Skip header row
                workbook = writer.book
                worksheet = writer.sheets[cat]

                # Cell formatting
                headerFormat = workbook.add_format({
                    "bold": True,
                    "valign": "center"
                })
                nameFormat = workbook.add_format({
                    "align": "center",
                    "valign": "vcenter",
                    "text_wrap": True
                })
                rarityFormat = workbook.add_format({
                    "align": "center",
                    "valign": "vcenter",
                    "num_format": "0.0"
                })
                descriptionFormat = workbook.add_format({
                    "text_wrap": True,
                    "valign": "top"
                })

                # Conditional formatting for Rarities
                conditionalFormatting = {
                    "trashFormat": {
                        "type": "cell",
                        "criteria": "between",
                        "minimum": 0.0,
                        "maximum": 0.9,
                        "format": workbook.add_format({"bg_color": "#f9cb9c"})
                    },
                    "commonFormat": {
                        "type": "cell",
                        "criteria": "between",
                        "minimum": 1.0,
                        "maximum": 1.9,
                        "format": workbook.add_format({"bg_color": "#74573e"})
                    },
                    "uncommonFormat": {
                        "type": "cell",
                        "criteria": "between",
                        "minimum": 2.0,
                        "maximum": 2.9,
                        "format": workbook.add_format({"bg_color": "#acb9b8"})
                    },
                    "rareFormat": {
                        "type": "cell",
                        "criteria": "between",
                        "minimum": 3.0,
                        "maximum": 3.9,
                        "format": workbook.add_format({"bg_color": "#00ff00"})
                    },
                    "eliteFormat": {
                        "type": "cell",
                        "criteria": "between",
                        "minimum": 4.0,
                        "maximum": 4.9,
                        "format": workbook.add_format({"bg_color": "#4a86e8"})
                    },
                    "epicFormat": {
                        "type": "cell",
                        "criteria": "between",
                        "minimum": 5.0,
                        "maximum": 5.9,
                        "format": workbook.add_format({"bg_color": "#9900ff"})
                    },
                    "legendaryFormat": {
                        "type": "cell",
                        "criteria": "between",
                        "minimum": 6.0,
                        "maximum": 6.9,
                        "format": workbook.add_format({"bg_color": "#f1c232"})
                    },
                    "mythicalFormat": {
                        "type": "cell",
                        "criteria": "between",
                        "minimum": 7.0,
                        "maximum": 7.9,
                        "format": workbook.add_format({"bg_color": "#ff00ff"})
                    },
                    "divineFormat": {
                        "type": "cell",
                        "criteria": "between",
                        "minimum": 8.0,
                        "maximum": 8.9,
                        "format": workbook.add_format({"bg_color": "#ff9900"})
                    },
                    "transcendentFormat": {
                        "type": "cell",
                        "criteria": "between",
                        "minimum": 9.0,
                        "maximum": 9.9,
                        "format": workbook.add_format({"bg_color": "#ff0000"})
                    }
                }

                # Set header row now
                for col, value in enumerate(df.columns.values):
                    worksheet.write(0, col, value, headerFormat)

                # First pass of formatting data
                worksheet.set_column("A2:A", 30, nameFormat)
                worksheet.set_column("B2:B", 10, rarityFormat)
                worksheet.set_column("C2:C", 85, descriptionFormat)

                # Second pass / rarity conditional formatting
                for format in conditionalFormatting:
                    worksheet.conditional_format("B2:B1048576", conditionalFormatting[format])
    except PermissionError:
        messagebox.showerror("Error", "Permission denied to access the file.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occured: {e}")

def convert_to_spreadsheet():
    if os.path.exists(SOURCE_DIR):
        files = []
        data = {}
        for file in os.listdir(SOURCE_DIR):
            if file.endswith(".txt"):
                files.append(file)
        if files:
            ext = r'(\.txt)$'
            for file in files:
                key = re.sub(ext, '', file)
                data[key] = read_from_file(file)

            output = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                title="Save As",
                                                filetypes=(("Excel Workbook", "*.xlsx"),),
                                                initialdir=".",
                                                initialfile="gacha")
            if output:
                write_to_spreadsheet(output, data)
        else:
            print(f"No text files found in {SOURCE_DIR}.")
    else:
        print(f"Source directory not found: {SOURCE_DIR}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gacha Utility")
    root.resizable(False, False)
    root.configure(bg="#e6e6e6")
    root.geometry("300x200")

    frame = tk.Frame(root, bg=root["bg"])
    frame.place(relx=0.5, rely=0.5, anchor="center")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "TButton",
        font=(("Segoe UI", "Helvetica", "Arial"), 12, "bold"),
        background="#5a4bad",
        foreground="white",
        padding=(12, 12),
        relief="flat",
        focusthickness=0,
        focuscolor="none"
    )

    style.map(
        "TButton",
        background=[
            ("pressed", "#6657bb"),
            ("active", "#5244a0")
            
        ],
        foreground=[
            ("disabled", "#AAAAAA")
        ]
    )

    convertToButton = ttk.Button(frame, text="Convert Data to Spreadsheet", command=convert_to_spreadsheet, style="TButton")
    convertToButton.pack(pady=10, expand=True, fill="x")

    root.mainloop()