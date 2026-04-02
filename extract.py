import fitz
import os

OUTPUT_IMG_DIR = "outputs/images"
os.makedirs(OUTPUT_IMG_DIR, exist_ok=True)

def extract_pdf_data(pdf_path, prefix):
    doc = fitz.open(pdf_path)

    text = ""
    images = []

    for page_num, page in enumerate(doc):
        text += page.get_text()

        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)

            img_bytes = base_image["image"]
            img_name = f"{prefix}_{page_num}_{img_index}.png"
            img_path = os.path.join(OUTPUT_IMG_DIR, img_name)

            with open(img_path, "wb") as f:
                f.write(img_bytes)

            images.append(img_path)

    return text, images