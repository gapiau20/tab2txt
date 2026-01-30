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
