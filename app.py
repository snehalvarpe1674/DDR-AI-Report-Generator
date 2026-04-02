from flask import Flask, render_template, request, send_file
import os

from extract import extract_pdf_data
from ai_engine import generate_ddr
from report_generator import attach_images
from utils import detect_conflicts

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    inspection_file = request.files["inspection"]
    thermal_file = request.files["thermal"]

    inspection_path = os.path.join(UPLOAD_FOLDER, inspection_file.filename)
    thermal_path = os.path.join(UPLOAD_FOLDER, thermal_file.filename)

    inspection_file.save(inspection_path)
    thermal_file.save(thermal_path)

    # Extract
    inspection_text, inspection_imgs = extract_pdf_data(inspection_path, "inspection")
    thermal_text, thermal_imgs = extract_pdf_data(thermal_path, "thermal")

    # Conflict detection
    conflicts = detect_conflicts(inspection_text, thermal_text)

    # Generate report
    report = generate_ddr(inspection_text, thermal_text)

    if conflicts:
        report += "\n\nConflicts Detected:\n"
        for c in conflicts:
            report += f"- {c}\n"

    # Attach images
    final_report = attach_images(report, inspection_imgs, thermal_imgs)

    # Save output
    os.makedirs("outputs", exist_ok=True)
    output_path = "outputs/final_report.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_report)

    return render_template("result.html", report=final_report)

@app.route("/download")
def download():
    return send_file("outputs/final_report.txt", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)