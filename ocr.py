import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image_path):
    result = reader.readtext(image_path, detail=0, paragraph=True)
    return " ".join(result)