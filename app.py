import json
import csv

countries = [
    {"name": "Noruega", "song": "Queen of kings", "artist": "Alessandra"},
    {"name": "Malta", "song": "Dance (our own party)", "artist": "The Busker"},
    {"name": "Serbia", "song": "Samo mí se spava", "artist": "Luke Black"},
    {"name": "Letonia", "song": "Sudden lights", "artist": "Sudden Lights"}
]

def save_votes(votes):
    with open('votes.json', 'w') as file:
        json.dump(votes, file)

def load_votes():
    try:
        with open('votes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def generate_csv(votes):
    csv_data = ''
    csv_data += 'País,Puntuación\n'
    for vote in votes:
        csv_data += f"{vote['country']},{str(vote['score'])}\n"
    return csv_data

def save_csv(csv_data):
    with open('resultados.csv', 'w') as file:
        file.write(csv_data)

if __name__ == '__main__':
    pass
