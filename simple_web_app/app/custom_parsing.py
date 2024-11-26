import os
import requests
import datetime
import pdfplumber
from markdownify import markdownify

# ====================================================================|=======:
def download_pdf_to_markdown(url,save_outputs=False): 
    # Get the current date and time
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
    # Define file names with timestamp
    pdf_filename = f"document_{timestamp}.pdf"
    markdown_filename = f"document_{timestamp}.md"

    # 1. Download the PDF
    url = "https://arxiv.org/pdf/2410.03960v1"
    response = requests.get(url)
    with open(pdf_filename, "wb") as f:
        f.write(response.content)

    # 2. Parse the PDF to extract text
    markdown_text = ""
    with pdfplumber.open(pdf_filename) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                markdown_text += text + "\n\n"

    # 3. Convert to Markdown and save to a file
    markdown_output = markdownify(markdown_text)
    with open(markdown_filename, "w") as f:
        f.write(markdown_output)

    print(f"PDF saved as: {pdf_filename}")
    print(f"Markdown saved as: {markdown_filename}")
    if not save_outputs: 
        os.remove(pdf_filename)
        os.remove(markdown_filename)
    return markdown_output

# ====================================================================|=======:
if __name__ == "__main__": 
    url = "https://arxiv.org/pdf/2410.03960v1"
    download_pdf_to_markdown(url)

