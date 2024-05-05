import csv
import emoji
from collections import Counter
import pandas as pd

def remove_emojis(text):
    return ''.join(c for c in text if c not in emoji.EMOJI_DATA)

with open('src/heyBankOriginal.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)

    for row in rows:
        row[2] = remove_emojis(row[2])

with open('src/HeyBankCleaned.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

def get_top_words(csv_file):
    df = pd.read_csv(csv_file)
    text = ' '.join(df['tweet'])
    words = text.split()
    word_counts = Counter(word for word in words if len(word) > 4)
    top_20_words = word_counts.most_common(10)
    
    with open('src/topWords.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Frequency'])
        writer.writerows(top_20_words)

def get_top_time(csv_file):
    df = pd.read_csv(csv_file)
    time = df['time']
    time_counts = Counter(time)
    top_20_time = time_counts.most_common(10)
    
    with open('src/topTime.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Time', 'Frequency'])
        writer.writerows(top_20_time)

get_top_words('src/heyBankTweet.csv')
get_top_time('src/heyBankOriginal.csv')
