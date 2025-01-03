pip install pdfminer.six
  
import re

from pdfminer.high_level import extract_pages, extract_text

text = extract_text("xxxxxx")
texto_filtrado = re.sub(r'[^\w\s]', '', text)  
print(texto_filtrado)
