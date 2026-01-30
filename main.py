import pandas as pd
import numpy as np

# =========================
# Configuration déclarative
# =========================

COLUMN_CONFIG = {
    "Admission HR": {
        "type": "scalar",
        "template": "Patient admitted with a heart rate of {value} bpm"
    },
    "Admission SBP": {
        "type": "scalar",
        "template": "systolic blood pressure of {value} mmHg",
        "prefix": "and"
    },
    "Glucose level": {
        "type": "scalar",
        "template": "glucose level of {value} mmol/L",
        "group": "biology"
    },
    "Cholesterol level": {
        "type": "scalar",
        "template": "cholesterol level of {value} mg/dL",
        "group": "biology"
    },
    "smoker": {
        "type": "boolean",
        "true": "The patient is a smoker",
        "false": "The patient is a non-smoker"
    }
}

# =========================
# text generation
# =========================

def generate_patient_text(row, config=COLUMN_CONFIG):
    sentences = []
    groups = {}

    for col, rules in config.items():
        value = row.get(col)

        if pd.isna(value):
            continue

        if rules["type"] == "scalar":
            text = rules["template"].format(value=value)

            if "group" in rules:
                groups.setdefault(rules["group"], []).append(text)
            else:
                prefix = rules.get("prefix", "")
                sentences.append(f"{prefix} {text}".strip())

        elif rules["type"] == "boolean":
            if value in [1, True, "yes", "Yes"]:
                sentences.append(rules["true"])
            else:
                sentences.append(rules["false"])

    for group_texts in groups.values():
        sentences.append("His " + " and ".join(group_texts))

    return ". ".join(sentences) + "."

# =========================
# Main — Demo
# =========================

def main():
    #sample dataset
    data = [
        {
            "Admission HR": 82,
            "Admission SBP": 120,
            "Glucose level": 5.6,
            "Cholesterol level": 180,
            "smoker": "yes"
        },
        {
            "Admission HR": 95,
            "Admission SBP": np.nan,
            "Glucose level": np.nan,
            "Cholesterol level": 210,
            "smoker": "no"
        },
        {
            "Admission HR": np.nan,
            "Admission SBP": np.nan,
            "Glucose level": 6.1,
            "Cholesterol level": np.nan,
            "smoker": np.nan
        }
    ]

    df = pd.DataFrame(data)

    df["clinical_text"] = df.apply(generate_patient_text, axis=1)

    for i, text in enumerate(df["clinical_text"], 1):
        print(f"Patient {i}:")
        print(text)
        print("-" * 60)

if __name__ == "__main__":
    main()
