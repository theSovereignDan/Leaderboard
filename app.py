from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from score_processor import read_scores # import the read_scores function from score_processor.py
from calculate_leaderboard import calculate_leaderboard # import the calculate_leaderboard function from calculate_leaderboard.py
@app.route('/')
def home_page():
    return render_template('leaderboard.html') # renders the leaderboard.html template to display the leaderboard

@app.route('/leaderboard-data') # endpoint to get the leaderboard data for the javascript script to use to handle the loading and rendering of the leaderboard as the user scrolls 
def get_leaderboard_data():
    
    scores = read_scores() 

    leaderboard_data = calculate_leaderboard(scores) # sets leaderboard data to the result of the calculate_leaderboard function

    page = request.args.get('page', 1, type=int) 
    per_page = 20 
    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = leaderboard_data[start:end]

    return jsonify(paginated_data)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
