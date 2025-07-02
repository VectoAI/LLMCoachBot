
from docx import Document

def load_docx_text(file):
    doc = Document(file)
    full_text = '\n'.join([para.text for para in doc.paragraphs if para.text.strip()])
    return full_text
