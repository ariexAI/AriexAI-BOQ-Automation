import pytesseract
from pdf2image import convert_from_path
from services.drawing_ai_service import detect_dimensions


# Tesseract Location
pytesseract.pytesseract.tesseract_cmd = r"C:\tessa\Tesseract-OCR\tesseract.exe"


def detect_footing_sizes(file_path):

    try:

        # Convert PDF → Images using Poppler
        images = convert_from_path(
            file_path,
            dpi=300,
            poppler_path=r"C:\poppler\Release-25.12.0-0\poppler-25.12.0\Library\bin"
        )

        full_text = ""

        # OCR each page
        for img in images:

            text = pytesseract.image_to_string(img)

            full_text += text + "\n"

        print("===== OCR TEXT =====")
        print(full_text[:1500])


        detected = detect_dimensions(full_text)

        return detected

    except Exception as e:

        return {"error": str(e)}
