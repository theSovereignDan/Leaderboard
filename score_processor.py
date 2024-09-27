import json
def read_scores():
    with open('scores.json', 'r') as file:
        return json.load(file)