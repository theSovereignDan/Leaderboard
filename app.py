from flask import Flask, render_template, request

app = Flask(__name__)

# Import for handling reading JSON data from the scores file
from services.json_file_handler import read_scores_json_file 

# Leaderboard processing: Calculating leaderboard data, filtering results, and generating leaderboard search result page messages
from services.leaderboard.leaderboard_processor import calculate_leaderboard_data 
from services.leaderboard.leaderboard_filtering import filter_leaderboard 
from services.leaderboard.leaderboard_message_generator import generate_leaderboard_search_result_message

# User submissions processing: Calculating user submission data and generating user submission search result messages
from services.user_submissions.user_submissions_processor import calculate_user_submissions_data 
from services.user_submissions.user_submissions_message_generator import generate_user_submissions_search_result_message

@app.route('/')
def home_page():
    # This endpoint displays the main leaderboard page (along with the sidebar) when the root URL is accessed
    # or is accessed by clicking on the "All scores" link from the sidebar.
    # It reads the scores JSON file, calculates the leaderboard data
    # and then renders the 'leaderboard.html' template and passes the necessary data to the template
    # it then sets which_leaderboard to "all" to specify which leaderboard to display to the html template
    # finally, it renders the 'leaderboard.html' template and passes the necessary data to the template for all the scores to display

    scores = read_scores_json_file() 

    leaderboard_data = calculate_leaderboard_data(scores) 

    which_leaderboard = "all"

    return render_template('leaderboard.html', leaderboard_data=leaderboard_data, which_leaderboard=which_leaderboard) 

@app.route('/top20scores') 
def top20scores():
    # This endpoint is accessed when the user clicks on the "Top 20 Scores" link from the sidebar.
    # The endpoint reads the scores JSON file, calculates the leaderboard data
    # and then slices the first 20 entries from the leaderboard data to get the top 20 scores
    # then sets which_leaderboard to "top" to specify which leaderboard to display to the html template
    # Finally, it renders the 'leaderboard.html' template and passes the necessary data to the template for the top 20 scores to display

    scores = read_scores_json_file() 

    leaderboard_data = calculate_leaderboard_data(scores) 
    
    top_20_data = leaderboard_data[:20]

    which_leaderboard = "top"

    return render_template('leaderboard.html', leaderboard_data=top_20_data, which_leaderboard=which_leaderboard) 


@app.route('/worst20scores') 
def worst20scores():
    # This endpoint reads the scores JSON file, calculates the leaderboard data
    # and then sorts the leaderboard data by 'overall score' in ascending order to get the worst 20 scores
    # It then slices the first 20 entries from the sorted leaderboard data to get the worst 20 scores
    # then sets which_leaderboard to "worst" to specify which leaderboard to display to the html template
    # Finally, it renders the 'leaderboard.html' template and passes the necessary data to the template for the worst 20 scores to display
    scores = read_scores_json_file()  

    leaderboard_data = calculate_leaderboard_data(scores)  

    sorted_leaderboard_data = sorted(leaderboard_data, key=lambda x: x['overall score'])

    worst_20_data = sorted_leaderboard_data[:20]

    which_leaderboard = "worst"
    
    return render_template('leaderboard.html', leaderboard_data=worst_20_data, which_leaderboard=which_leaderboard) 

@app.route('/search') 
def search():
    # This endpoint renders the search html template when the button to access the search page on side bar is clicked
    # Or when you click back from the result page (when the user clicks back button) if was no results  
    return render_template('search.html') 

@app.route('/result') 
def result():
    # This endpoint is accessed when the user submits the search form (and they have filled in all required fields correctly)

    # this gets all the parameters (stored in the URL) which were passed through 
    # from what was inputed on search form and stores them in a dictionary
    # it has to ensure values are there because sometimes it might be empty because different dropdown options were selected 
    params = {
    'name': request.args.get('name') if request.args.get('name') != '' else None,
    'score_filter': request.args.get('scoreFilter') if request.args.get('scoreFilter') != None else None,
    'score_threshold': request.args.get('scoreThreshold') if request.args.get('scoreThreshold') else None,
    'score_threshold_low': request.args.get('scoreThresholdLow') if request.args.get('scoreThresholdLow') else None,
    'score_threshold_high': request.args.get('scoreThresholdHigh') if request.args.get('scoreThresholdHigh') else None,
    'rank_filter': request.args.get('rankFilter') if request.args.get('rankFilter') != None else None,
    'rank_threshold': request.args.get('rankThreshold') if request.args.get('rankThreshold') else None,
    'rank_threshold_low': request.args.get('rankThresholdLow') if request.args.get('rankThresholdLow') else None,
    'rank_threshold_high': request.args.get('rankThresholdHigh') if request.args.get('rankThresholdHigh') else None
    }

    # this works out what message to display on the results page based on the search parameters 
    # the message is usually around either what name was searched for or what filters were applied
    message = generate_leaderboard_search_result_message(params)

    # this converts any of the params values that were strings of numbers into integers
    params_withStrToInts = {
        'name': params['name'],  
        'score_filter': params['score_filter'], 
        'score_threshold': int(params['score_threshold']) if params['score_threshold'] is not None else None,
        'score_threshold_low': int(params['score_threshold_low']) if params['score_threshold_low'] is not None else None,
        'score_threshold_high': int(params['score_threshold_high']) if params['score_threshold_high'] is not None else None,
        'rank_filter': params['rank_filter'], 
        'rank_threshold': int(params['rank_threshold']) if params['rank_threshold'] is not None else None,
        'rank_threshold_low': int(params['rank_threshold_low']) if params['rank_threshold_low'] is not None else None,
        'rank_threshold_high': int(params['rank_threshold_high']) if params['rank_threshold_high'] is not None else None,
    }

    # this reads the scores JSON file, calculates the leaderboard data
    # then filters the leaderboard data based on the search parameters 
    # and then renders the 'result.html' template and passes the necessary data to the template for the filtered leaderboard data to display
    # it also includes the message generated from the search parameters in the template for display to the user
    scores = read_scores_json_file()  

    leaderboard_data = calculate_leaderboard_data(scores)

    filtered_leaderboard_data = filter_leaderboard(leaderboard_data, params_withStrToInts)

    return render_template('result.html', filtered_leaderboard_data=filtered_leaderboard_data, message=message)

@app.route('/findbyuser') 
def find_by_user():
    # This endpoint renders the find by user html template when the button to access the find by user 
    # (also known as the search user submissions page) on side bar is clicked
    return render_template('findbyuser.html')


@app.route('/user-submissions') 
def user_submissions():
    # This endpoint is accessed when the user submits the search form on the find by user page
    # which  also known as the (search user submissions page) and they have filled in all required fields correctly)


    # It then gets all the parameters (stored in the URL) which were passed through 
    # from what was inputed on the find by user (search user submissions) page form and store them 
    # in different variables
    name = request.args.get('name')
    sort = request.args.get('sort')
    order = request.args.get('order')
    qualifiedorall = request.args.get('qualifiedorall')

    # It then read the scores JSON file, calculates the user submissions data (whilst using the filters and checking that the user exists)
    # then generates the message to display on the user submissions page based on the parameters 
    # it then renders the 'usersubmissions.html' template and passes the necessary data to the template 
    # for the specified user's submissions data to display
    scores = read_scores_json_file() 
    
    user_submissions_data = calculate_user_submissions_data(scores, name, sort, order, qualifiedorall)

    message = generate_user_submissions_search_result_message(sort, order, qualifiedorall)
    
    return render_template('usersubmissions.html', user_submissions_data=user_submissions_data, message=message, name=name)

if __name__ == '__main__':
    app.run(debug=True, port=5015)
