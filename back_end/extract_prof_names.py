import fitz
import re
import os

def extract_text_from_pdf(pdf_path):
    text_list = []
    pdf_document = fitz.open(pdf_path)
    
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        
        text = page.get_text()
        text_list.append(text)
    
    pdf_document.close()
    return text_list

folder_path='pdfs'
text=""
dictionary=('Ed', 'Fizica', 'Ghidare', 'Engleza', 'Gh', 'Proiect')

for filename in os.listdir(folder_path):
    file_path=os.path.join(folder_path, filename)

    if os.path.isfile(file_path):   
        text_from_pdf=extract_text_from_pdf(file_path)
        text+=text_from_pdf[0]

name_pattern=re.compile(r'\b[A-Z]\.\s*[A-Z][a-z]+\b')
matches=name_pattern.findall(text)

clean_list=[name.replace('\\n', ' ').replace('\n', ' ').strip() for name in matches]
clean_list=[name.replace(' ', '').replace('.', '. ').strip() for name in clean_list]

names=list(set(clean_list))
names.sort()

for name in names:
    if name.split(' ')[1] in dictionary:
        names.remove(name)

with open("prof_names.txt", "w") as file:
    for name in names:
        file.write(f'{name}|{clean_list.count(name) + clean_list.count(name.replace(" ", ""))}\n')
