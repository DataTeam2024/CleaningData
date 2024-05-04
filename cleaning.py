import csv
import emoji

def remove_emojis(text):
    return ''.join(c for c in text if c not in emoji.EMOJI_DATA)

with open('HeyBank.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)

    for row in rows:
        row[2] = remove_emojis(row[2])

with open('HeyBank.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
