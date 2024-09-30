import json
def read_scores_json_file():
    with open('data/scores.json', 'r') as file:
        return json.load(file)