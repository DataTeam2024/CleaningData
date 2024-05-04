import csv
import emoji

def remove_emojis(text):
    # Remove emojis from the text
    return ''.join(c for c in text if c not in emoji.EMOJI_DATA)

# Abre el archivo CSV para lectura y escritura
with open('HeyBank.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)

    # Procesa todas las filas en la columna número 3
    for row in rows:
        row[2] = remove_emojis(row[2])

# Escribe los cambios de nuevo en el archivo CSV
with open('HeyBank.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
