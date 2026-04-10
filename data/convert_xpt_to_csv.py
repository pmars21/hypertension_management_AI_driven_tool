import os
import pandas as pd
from pathlib import Path

def convert_missing_xpt_to_csv(xpt_dir, csv_dir):
    """
    Converts .xpt files in xpt_dir to .csv format in csv_dir.
    Skips files that already have a corresponding .csv file in the target directory.
    """
    xpt_path = Path(xpt_dir)
    csv_path = Path(csv_dir)
    
    # Ensure csv directory exists
    csv_path.mkdir(parents=True, exist_ok=True)
    
    if not xpt_path.exists():
        print(f"Error: Directory {xpt_dir} does not exist.")
        return
        
    for xpt_file in xpt_path.glob('*.xpt'):
        # Target CSV file
        csv_file = csv_path / (xpt_file.stem + '.csv')
        
        if not csv_file.exists():
            print(f"Converting {xpt_file.name} to CSV...")
            try:
                # Read the SAS XPORT file
                df = pd.read_sas(xpt_file, format='xport')
                # Save to CSV
                df.to_csv(csv_file, index=False)
                print(f"Successfully created {csv_file.name}")
            except Exception as e:
                print(f"Failed to convert {xpt_file.name}: {e}")
        else:
            print(f"Skipping {xpt_file.name}, {csv_file.name} already exists.")

if __name__ == "__main__":
    # Base paths
    base_dir = Path(r"c:\Users\pablo\Desktop\Master\TFM")
    xpt_folder = base_dir / "data" / "xpt"
    csv_folder = base_dir / "data" / "csv"
    
    print(f"Checking for .xpt files in {xpt_folder}...")
    convert_missing_xpt_to_csv(xpt_folder, csv_folder)
    print("Process finished.")
