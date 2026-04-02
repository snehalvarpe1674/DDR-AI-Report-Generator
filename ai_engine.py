KEYWORDS = ["leak", "crack", "temperature", "moisture", "damage", "hotspot"]

def extract_points(text):
    lines = text.split("\n")
    points = []

    for line in lines:
        line = line.strip()
        if len(line) > 20:
            if any(k in line.lower() for k in KEYWORDS):
                points.append(line)

    return list(set(points))[:15]


def generate_ddr(inspection_text, thermal_text):

    inspection_points = extract_points(inspection_text)
    thermal_points = extract_points(thermal_text)

    combined = list(set(inspection_points + thermal_points))

    # Sections
    summary = "\n".join(combined[:3]) if combined else "Not Available"

    observations = "\n".join([f"- {p}" for p in combined]) if combined else "Not Available"

    if combined:
        root_cause = "Possible reasons include structural damage, water leakage, or thermal inefficiencies."
        severity = "Medium - Issues detected but not critical. Further inspection recommended."
        actions = "Repair damaged areas, fix leakage, and perform detailed inspection."
    else:
        root_cause = severity = actions = "Not Available"

    additional_notes = "This report is generated using a rule-based AI system."

    missing_info = "Detailed measurements or exact locations: Not Available"

    report = f"""
1. Property Issue Summary
{summary}

2. Area-wise Observations
{observations}

3. Probable Root Cause
{root_cause}

4. Severity Assessment (with reasoning)
{severity}

5. Recommended Actions
{actions}

6. Additional Notes
{additional_notes}

7. Missing or Unclear Information
{missing_info}
"""

    return report