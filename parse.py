import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os
import glob
from tqdm import tqdm

# get all pdf files from inputs folder
pdf_files = glob.glob("inputs/*.pdf")

# process each pdf file with progress bar
for pdf_path in tqdm(pdf_files, desc="processing pdfs", unit="file"):
    # get filename without extension for output naming
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = f"outputs/{base_name}.txt"
    
    # convert pdf pages to images
    pages = convert_from_path(pdf_path)
    
    # extract text from all pages with progress bar
    all_text = ""
    for i, page in enumerate(tqdm(pages, desc=f"parsing {base_name}", unit="page", leave=False)):
        text = pytesseract.image_to_string(page)
        all_text += f"Page {i+1}:\n{text}\n\n"
    
    # save extracted text to output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(all_text)
    
    print(f"✓ saved text from {base_name} to {output_path}")

print("🎉 processing complete!")

