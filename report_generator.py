def attach_images(report, inspection_imgs, thermal_imgs):

    section = "\n\n---\n\n### Images Section\n"

    if inspection_imgs:
        section += "\nInspection Images:\n"
        for img in inspection_imgs:
            section += f"{img}\n"
    else:
        section += "\nInspection Images: Image Not Available\n"

    if thermal_imgs:
        section += "\nThermal Images:\n"
        for img in thermal_imgs:
            section += f"{img}\n"
    else:
        section += "\nThermal Images: Image Not Available\n"

    return report + section