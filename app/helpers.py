import re
from PyPDF2 import PdfReader

def read_pdf(file_path):
    reader = PdfReader(file_path)
    content = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            content += page_text + " "

    return content


def split_into_chunks(text, max_words=400, overlap=50):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []

    current_chunk = []
    current_count = 0

    for sentence in sentences:
        words = sentence.split()

        if current_count + len(words) > max_words:
            chunks.append(" ".join(current_chunk))
            current_chunk = current_chunk[-overlap:]
            current_count = len(current_chunk)

        current_chunk.extend(words)
        current_count += len(words)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
