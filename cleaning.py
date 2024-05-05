import csv
import emoji
import pandas as pd
from collections import Counter


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

df = pd.read_csv('/HeyBank.csv')
df=df.drop(columns=['date', 'time'])
df.to_csv('/HeyBank.csv', index=False)
df.head()

def get_top_words(csv_file):
    df = pd.read_csv(csv_file)
    
    text = ' '.join(df['tweet'])
    
    words = text.split()
    
    word_counts = Counter(word for word in words if len(word) > 4)
    
    top_20_words = word_counts.most_common(10)
    
    with open('top_20_words.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Frequency'])
        writer.writerows(top_20_words)

get_top_words('HeyBank.csv')