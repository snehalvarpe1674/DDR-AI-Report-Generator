def detect_conflicts(inspect_text, thermal_text):
    conflicts = []

    if "leak" in inspect_text.lower() and "no moisture" in thermal_text.lower():
        conflicts.append("Leak reported but thermal shows no moisture")

    if "high temperature" in thermal_text.lower() and "normal" in inspect_text.lower():
        conflicts.append("Thermal shows high temperature but inspection says normal")

    return conflicts