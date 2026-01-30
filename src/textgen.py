import pandas as pd


# =========================
# dict generation
# =========================
def row_to_dict(row:pd.Series):
    return row.to_dict()
# =========================
# text generation
# =========================
def generate_patient_text(row, config:dict):
    sentences = []
    groups = {}

    for col, rules in config.items():
        value = row[col]

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

