import pandas as pd
import numpy as np

from src.textgen import generate_patient_text
from src.config import parseYML
# =========================
# Configuration 
# =========================
COLUMN_CONFIG=parseYML('tabular_dataset\\cardio_config.yaml')



# =========================
# Main — Demo
# =========================

def main():
    #sample dataset
    config=COLUMN_CONFIG
    
    df=pd.read_csv('tabular_dataset\\cardio.csv')
    df["clinical_text"] = df.apply(lambda x:generate_patient_text(x,config), axis=1)

    for i, text in enumerate(df["clinical_text"], 1):
        print(f"Patient {i}:")
        print(text)
        print("-" * 60)

if __name__ == "__main__":
    main()
