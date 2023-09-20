import fitz

pdf_document = "test_task.pdf"
doc = fitz.open(pdf_document)

page1 = doc.load_page(0)
page1text = page1.get_text()

# валидируем ключи
expected_keys = ["PN", "SN", "DESCRIPTION", "LOCATION", "CONDITION", "RECEIVER#", "UOM", "EXP DATE", "PO",
                 "CERT SOURCE", "REC.DATE", "MFG", "BATCH#", "DOM", "REMARK", "LOT#", "TAGGED BY", "Qty", "NOTES"]

# пустой словарь для дальнейшего заполнения
extracted_data = {}

# Разделим полученный текст на строки и пройдемся по каждой строчке циклом и вложенным циклом
lines = page1text.split("\n")
for line in lines:
    for key in expected_keys:
        if key in line:
            # Разделить строку на ключ и значение
            parts = line.split(key)
            if len(parts) > 1:
                # Тут извлечь значение и убрать лишние символы и пробелы
                value = parts[1].strip(":").strip()
                # Значения в некоторых ключах выводятся неправильно, например  "BATCH#" : ": 1", поэтому пришлось добавить срез
                if value.startswith(": "):
                    value = value[2:]
                extracted_data[key] = value

print(extracted_data)
