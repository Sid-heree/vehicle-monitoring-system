import easyocr

reader = easyocr.Reader(['en'])

def read_text(image):
    return reader.readtext(image)