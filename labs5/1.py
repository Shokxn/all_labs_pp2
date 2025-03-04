import re
import json

file_path = "C:\\Users\\Huawei\\Documents\\GitHub\\all_labs_pp2\\labs5\\row.txt"
with open(file_path, "r", encoding="utf-8-sig") as file:
    data = file.read()

cashier = re.search(r'Кассир\s+(.+)', data)
cashier = cashier.group(1) if cashier else ""
receipt_number = re.search(r'Чек №(\d+)', data)
receipt_number = receipt_number.group(1) if receipt_number else ""
date = re.search(r'Время:\s+([\d:.\s]+)', data)
date = date.group(1) if date else ""
total = re.search(r'ИТОГО:\s+([\d\s]+,\d+)', data)
total = float(total.group(1).replace(" ", "").replace(",", ".")) if total else 0.0
vat = re.search(r'в т\.ч\. НДС 12%:\s+([\d\s]+,\d+)', data)
vat = float(vat.group(1).replace(" ", "").replace(",", ".")) if vat else 0.0
fiscal_sign = re.search(r'Фискальный признак:\s+(\d+)', data)
fiscal_sign = fiscal_sign.group(1) if fiscal_sign else ""

items = []
pattern = re.compile(r'\d+\.\n(.+?)\n(\d+,\d+)\s*x\s*([\d\s]+,\d+)\n([\d\s]+,\d+)')

for match in pattern.findall(data):
    name, quantity, unit_price, total_price = match
    items.append({
        "Название": name.strip(),
        "Количество": float(quantity.replace(",", ".")),
        "Цена за единицу": float(unit_price.replace(" ", "").replace(",", ".")),
        "Общая стоимость": float(total_price.replace(" ", "").replace(",", "."))
    })

receipt_json = {
    "Кассир": cashier,
    "Чек №": receipt_number,
    "Дата": date,
    "Товары": items,
    "Итого": total,
    "НДС 12%": vat,
    "Фискальный признак": fiscal_sign
}

with open("receipt.json", "w", encoding="utf-8") as json_file:
    json.dump(receipt_json, json_file, ensure_ascii=False, indent=4)

print(json.dumps(receipt_json, ensure_ascii=False, indent=4))