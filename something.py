pip install pdfminer.six
  
import re

from pdfminer.high_level import extract_pages, extract_text

text = extract_text("xxxxxxxxxx")
texto_filtrado = re.sub(r'[^\w\s./;,\\]', '', text)

ocorrencias = [m.start() for m in re.finditer('XXXXXXX', texto_filtrado)]

for i in range(len(ocorrencias) - 1):
    inicio = ocorrencias[i] + len('XXXXXXX')
    fim = ocorrencias[i + 1]
    texto_XXXXXXX = texto_filtrado[inicio:fim].strip()
    print(f"XXXXXXX {i + 1}:\n{texto_XXXXXXX}\n")
