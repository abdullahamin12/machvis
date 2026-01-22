import pandas as pd
import json
import os

# ==================================================
#  CSV TO JSON CONVERTER
#  Turns your spreadsheet into the System Dictionary
# ==================================================

INPUT_FILE = "data/final_set_dict.csv"  # Make sure your file is named this!
OUTPUT_FILE = "data/vocational_dict.json"

def convert():
    print(f"Reading {INPUT_FILE}...")
    
    try:
        # Read the CSV
        df = pd.read_csv(INPUT_FILE)
        
        # Check if columns exist
        if "German" not in df.columns or "English" not in df.columns:
            print("[ERROR] CSV must have 'German' and 'English' columns.")
            return

        # Remove duplicates (Keep the first valid translation found)
        # This is important because JSON cannot have duplicate keys
        df = df.drop_duplicates(subset=["German"], keep="first")
        
        # Convert to Dictionary {German: English}
        vocational_dict = pd.Series(df.English.values, index=df.German).to_dict()
        
        # Save as JSON
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(vocational_dict, f, indent=4, ensure_ascii=False)
            
        print(f"[SUCCESS] converted {len(vocational_dict)} terms.")
        print(f"Saved to: {OUTPUT_FILE}")
        print("You can now run 'main_pipeline.py' to use this new brain.")

    except FileNotFoundError:
        print(f"[ERROR] Could not find {INPUT_FILE}. Did you put it in the 'data' folder?")

if __name__ == "__main__":
    convert()